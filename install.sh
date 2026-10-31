#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
MODE="${MODE:-}"
DRY_RUN=0
AUTO_START=0

usage() {
  cat <<'EOF'
Uso: bash install.sh [--mode docker|local] [--auto-start] [--dry-run]

Opções:
  --mode docker     Usa Docker Compose para subir a aplicação.
  --mode local      Cria um ambiente virtual local e instala dependências.
  --auto-start      Configura início automático no boot do host, quando possível.
  --dry-run         Apenas mostra o que seria executado sem alterar o sistema.
  -h, --help        Mostra esta ajuda.

Se nenhum modo for informado, o script tenta detectar o ambiente e pede uma escolha
quando estiver em terminal interativo.
EOF
}

prompt_mode() {
  if [[ -t 0 ]]; then
    read -r -p "Escolha o modo de instalação [docker/local]: " MODE
    MODE="${MODE:-local}"
  else
    MODE="local"
  fi
}

run_cmd() {
  if [[ "$DRY_RUN" -eq 1 ]]; then
    echo "+ $*"
    return 0
  fi

  "$@"
}

ensure_env_file() {
  if [[ -f "$SCRIPT_DIR/.env" ]]; then
    return 0
  fi

  if [[ "$DRY_RUN" -eq 1 ]]; then
    echo "+ cp \"$SCRIPT_DIR/.env_default\" \"$SCRIPT_DIR/.env\""
    echo "Arquivo .env seria criado a partir de .env_default. Ajuste os valores locais antes de iniciar."
    return 0
  fi

  cp "$SCRIPT_DIR/.env_default" "$SCRIPT_DIR/.env"
  echo "Arquivo .env criado a partir de .env_default. Ajuste os valores locais antes de iniciar."
}

setup_local() {
  if ! command -v python3 >/dev/null 2>&1; then
    echo "Python 3 não encontrado. Instale o Python 3.11+ antes de continuar."
    exit 1
  fi

  ensure_env_file

  if [[ ! -d "$SCRIPT_DIR/.venv" ]]; then
    run_cmd python3 -m venv "$SCRIPT_DIR/.venv"
  fi

  local pybin="$SCRIPT_DIR/.venv/bin/python"
  local pipbin="$SCRIPT_DIR/.venv/bin/pip"

  run_cmd "$pybin" -m pip install --upgrade pip
  run_cmd "$pybin" -m pip install -r "$SCRIPT_DIR/requirements.txt"

  if [[ "$AUTO_START" -eq 1 ]]; then
    local launcher_dir="$HOME/.local/bin"
    local launcher_path="$launcher_dir/glpi-ai-support"
    mkdir -p "$launcher_dir"
    cat > "$launcher_path" <<EOF
#!/usr/bin/env bash
cd "$SCRIPT_DIR"
exec "$pybin" -m uvicorn main:app --host 0.0.0.0 --port 8000
EOF
    chmod +x "$launcher_path"

    if [[ "$(uname -s)" == "Linux" ]] && command -v crontab >/dev/null 2>&1; then
      local cron_entry="@reboot $launcher_path >> $HOME/glpi-ai-support.log 2>&1"
      (crontab -l 2>/dev/null || true; echo "$cron_entry") | crontab -
      echo "Registro de inicialização adicionado ao crontab do usuário."
    else
      echo "Inicialização automática não foi configurada automaticamente neste ambiente."
      echo "Você pode usar o launcher em $launcher_path manualmente."
    fi
  fi

  echo "Ambiente local preparado."
  echo "Para iniciar manualmente:"
  echo "  cd $SCRIPT_DIR && .venv/bin/python -m uvicorn main:app --host 0.0.0.0 --port 8000"
}

setup_docker() {
  if command -v docker >/dev/null 2>&1; then
    if docker compose version >/dev/null 2>&1; then
      echo "Docker Compose encontrado."
      run_cmd docker compose up --build -d
      echo "A aplicação foi iniciada com Docker Compose."
      echo "Acesse: http://localhost:8000"
      return 0
    fi
  fi

  if command -v docker-compose >/dev/null 2>&1; then
    echo "Docker Compose legado encontrado."
    run_cmd docker-compose up --build -d
    echo "A aplicação foi iniciada com Docker Compose legado."
    echo "Acesse: http://localhost:8000"
    return 0
  fi

  echo "Docker não foi encontrado no ambiente. Instale o Docker e tente novamente."
  exit 1
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --mode)
      MODE="${2:-}"
      shift 2
      ;;
    --auto-start)
      AUTO_START=1
      shift
      ;;
    --dry-run)
      DRY_RUN=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Opção desconhecida: $1"
      usage
      exit 1
      ;;
  esac
done

if [[ -z "$MODE" ]]; then
  prompt_mode
fi

case "$MODE" in
  docker)
    setup_docker
    ;;
  local)
    setup_local
    ;;
  *)
    echo "Modo inválido: $MODE. Use docker ou local."
    exit 1
    ;;
esac

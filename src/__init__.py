
from pathlib import Path

from src.util.load_env import load_env_vars

ENV_PATH = Path(__file__).parent / "env"

# Init env
ENV = load_env_vars(str(ENV_PATH / ".env"))


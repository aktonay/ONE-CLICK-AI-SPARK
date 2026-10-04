from pathlib import Path
import subprocess
try:
    import tomllib
except ImportError:
    import toml as tomllib
from typing import Dict, Any

APP_NAME = "one-click-ai"
CONFIG_DIR = Path.home() / ".config" / APP_NAME
CONFIG_FILE = CONFIG_DIR / "config.toml"


def get_git_user() -> str:
    """Attempt to get the git global user name."""
    try:
        result = subprocess.run(
            ["git", "config", "--global", "user.name"],
            capture_output=True,
            text=True,
            check=False,
        )
        return result.stdout.strip()
    except Exception:
        return ""


def load_config() -> Dict[str, Any]:
    """Load configuration from the local config file."""
    if not CONFIG_FILE.exists():
        return {}
    try:
        with open(CONFIG_FILE, "rb") as f:
            return tomllib.load(f)
    except Exception:
        return {}


def save_config(
    github_username: str,
    dockerhub_username: str,
    default_llm_provider: str = "openai",
    default_vector_store: str = "faiss",
):
    """Save configuration to the local config file."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    content = f"""[user]
github_username = "{github_username}"
dockerhub_username = "{dockerhub_username}"
default_llm_provider = "{default_llm_provider}"
default_vector_store = "{default_vector_store}"
"""
    with open(CONFIG_FILE, "w") as f:
        f.write(content)


def get_config_value(key: str, default: str = "") -> str:
    """Get a specific config value from the [user] table."""
    config = load_config()
    return config.get("user", {}).get(key, default)

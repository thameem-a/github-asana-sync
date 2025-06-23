import os
from pathlib import Path

from dotenv import dotenv_values


def load_env_vars(env_file: str) -> dict[str, str]:
    """
    Load environment variables from a .env file and store them in a dictionary.
    Environment variables take precedence over .env file values.

    Args:
        env_file (str): The path to the .env file.

    Returns:
        dict[str, str]: A dictionary containing the environment variables.
    """
    env = dotenv_values(dotenv_path=Path(env_file))
    validated_vars: dict[str, str] = {}
    for key, val in env.items():
        # First check environment variables
        try:
            val = os.environ[key]
        except KeyError:
            # If not in environment, use .env value
            if not val:
                raise EnvironmentError(f"Missing required environment variable: {key}")
        validated_vars[key] = val
    return validated_vars
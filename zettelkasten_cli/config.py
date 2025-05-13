from pathlib import Path
import os

# Paths
ZETTELKASTEN_ROOT = Path(os.environ.get("ZETTELKASTEN", ""))
INBOX_PATH = ZETTELKASTEN_ROOT / "+"

# File settings
MAX_TITLE_LENGTH = 80

# Prompts
PROMPT_TITLE = "Enter the title of the note"

# Commands
EDITOR_COMMAND = "nvim"

# Only use default arguments if environment variable is not set
NVIM_ARGS = os.environ.get("ZETTELKASTEN_NVIM_ARGS") or "+ normal Gzzo"

# Only use default commands if environment variable is not set
nvim_cmds = os.environ.get("ZETTELKASTEN_NVIM_COMMANDS")
if not nvim_cmds:
    raise EnvironmentError("ZETTELKASTEN_NVIM_COMMANDS is not set.")
NVIM_COMMANDS = nvim_cmds.split(",")


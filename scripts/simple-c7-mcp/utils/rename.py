import os
from pathlib import Path

# Get the project root (parent of utils/)
SCRIPT_PATH = Path(__file__).resolve()
PROJECT_ROOT = SCRIPT_PATH.parent.parent
os.chdir(PROJECT_ROOT)

# Configuration
OLD_DIR_NAME = "python_template"
OLD_BIN_NAME = OLD_DIR_NAME.replace("_", "-")
NEW_DIR_NAME = "c7_mcp"
NEW_BIN_NAME = "c7-mcp"


def replace_in_file(filepath, old, new):
    """Replace text in file if it's a text file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        new_content = content.replace(old, new)
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {filepath}")
    except (UnicodeDecodeError, PermissionError):
        pass


def rename_if_matches(path, old, new):
    """Rename path if it contains old name."""
    dirname, basename = os.path.split(path)
    if old in basename:
        new_path = os.path.join(dirname, basename.replace(old, new))
        os.rename(path, new_path)
        print(f"Renamed: {path} -> {new_path}")
        return new_path
    return path


# Collect all files and directories (excluding this script and hidden dirs)
all_files, all_dirs = [], []
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    for f in files:
        filepath = os.path.join(root, f)
        # Skip this script
        if Path(filepath).resolve() == SCRIPT_PATH:
            continue
        all_files.append(filepath)
    all_dirs.extend(os.path.join(root, d) for d in dirs)

# Replace content in text files
for filepath in all_files:
    replace_in_file(filepath, OLD_DIR_NAME, NEW_DIR_NAME)
    replace_in_file(filepath, OLD_BIN_NAME, NEW_BIN_NAME)

# Rename files (deepest first)
for filepath in sorted(all_files, key=lambda x: x.count(os.sep), reverse=True):
    filepath = rename_if_matches(filepath, OLD_DIR_NAME, NEW_DIR_NAME)
    rename_if_matches(filepath, OLD_BIN_NAME, NEW_BIN_NAME)

# Rename directories (deepest first)
for dirpath in sorted(all_dirs, key=lambda x: x.count(os.sep), reverse=True):
    dirpath = rename_if_matches(dirpath, OLD_DIR_NAME, NEW_DIR_NAME)
    rename_if_matches(dirpath, OLD_BIN_NAME, NEW_BIN_NAME)

# Rename the project root directory itself
if OLD_DIR_NAME in PROJECT_ROOT.name:
    new_root = PROJECT_ROOT.parent / PROJECT_ROOT.name.replace(OLD_DIR_NAME, NEW_DIR_NAME)
    os.rename(PROJECT_ROOT, new_root)
    print(f"Renamed project root: {PROJECT_ROOT} -> {new_root}")

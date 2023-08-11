import os
import shutil
from pathlib import Path

IGNORE_DIRS = [
    "__pycache__",
    "venv",
    "build",
    "dist",
    ".git",
    ".mypy_cache",
    "__pypackages__",
    ".pdm-build",
    ".ruff_cache",
    ".pytest_cache",
    ".coverage",
]


def copy_and_replace(src: str, dst: str, old_word: str, new_word: str) -> None:
    """Copy a file from src to dst and replace old_word with new_word"""

    # Remove the dst directory if it exists
    if os.path.exists(dst):
        shutil.rmtree(dst)

    # Copy the src directory to dst
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns(*IGNORE_DIRS))
    # shutil.copytree(src, dst)

    # Walk through all the files in the dst directory
    for path, dirs, files in os.walk(dst):
        for file in files:
            # Read the file
            file_path = Path(path, file)
            # print(file_path)
            with open(file_path, "rt", encoding="utf-8") as f:
                try:
                    s = f.read()
                # we don't care about non unicode files
                except UnicodeDecodeError:
                    continue

            # Replace the target string
            if old_word not in s:
                continue
            s = s.replace(old_word, new_word)

            # Write the file out again
            with open(file_path, "wt", encoding="utf-8") as f:
                f.write(s)

    # Delete the tests and selfcookie directories
    shutil.rmtree(Path(dst, "tests"))
    shutil.rmtree(Path(dst, "selfcookie"))

    for dir in os.listdir(Path(src, "default")):
        source_dir = Path(src, "default", dir)
        dir = dir.replace(old_word, new_word)
        target_dir = Path(dst, dir)
        shutil.copytree(source_dir, target_dir)

    os.chdir(dst)
    os.system("git init")
    os.system("pdm release")
    # shutil.copytree(Path(src, "default"), dst)

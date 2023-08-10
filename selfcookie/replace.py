import fnmatch
import os
import shutil
from pathlib import Path


def get_gitignore_patterns(gitignore_path: str) -> list[str]:
    patterns = []
    with open(gitignore_path, "r") as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):
                patterns.append(line)
    return patterns


def copy_non_ignored_files(
    source_directory: str,
    target_directory: str,
    word_to_replace: str | None = None,
    replacement_word: str | None = None,
) -> None:
    gitignore_path = ".gitignore"
    gitignore_patterns = get_gitignore_patterns(gitignore_path)

    for root, _, files in os.walk(source_directory):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, source_directory)

            if not any(fnmatch.fnmatch(relative_path, pattern) for pattern in gitignore_patterns):
                target_path = os.path.join(target_directory, relative_path)
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                shutil.copy2(file_path, target_path)
                print(f"Copied {relative_path} to {target_path}")

                if word_to_replace and replacement_word:
                    data = Path(target_path).read_text()
                    data = data.replace(word_to_replace, replacement_word)
                    Path(target_path).write_text(data)

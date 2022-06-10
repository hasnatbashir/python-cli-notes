"""Contains core functionality of notes."""

from config import config
import os


notes_dir = config["notes_dir"]


def create_new_note(name: str):
    if os.path.exists(f"{notes_dir}/{name}.txt"):
        raise ValueError("Note already exists.")
    with open(f"{notes_dir}/{name}.txt", 'w') as f:
        f.write("")


def add_content_to_note(name: str, content: str):
    if not os.path.exists(f"{notes_dir}/{name}.txt"):
        raise ValueError("Note does not exist.")
    with open(f"{notes_dir}/{name}.txt", 'a') as f:
        f.write(content)


def list_all_notes() -> list:
    files = []
    for file in os.listdir(notes_dir):
        if file.endswith('.txt'):
            files.append(file)
    return files


def get_notes_content(name: str) -> str:
    if not os.path.exists(f"{notes_dir}/{name}.txt"):
        raise ValueError("Note does not exist.")
    with open(f"{notes_dir}/{name}.txt", 'r') as file:
        notes_data = file.read()
    return notes_data
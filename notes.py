from config import config
import os
notes_dir = config["notes_dir"]


def create_new_note(name: str):
    with open(f"{notes_dir}/{name}.txt", 'w') as f:
        f.close()


def add_content_to_note(name: str, content: str):
    with open(f"{notes_dir}/{name}.txt", 'a') as f:
        f.write(content)


def list_all_notes() -> list:
    files = []
    for file in os.listdir(notes_dir):
        if file.endswith('.txt'):
            files.append(file)
    return files
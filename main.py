import typer
from app import setup_app
from config import config
from notes import create_new_note, add_content_to_note, list_all_notes
app = typer.Typer()
@app.command()
def create_note(name: str):
    try:
        create_new_note(name=name)
        typer.echo(f"created note {name}")
    except:
        typer.echo(f"error creating new note.")

@app.command()
def append_to_note(name: str, content: str):
    try:
        add_content_to_note(name=name, content=content)
        typer.echo(f"Added content to note {name}")
    except:
        typer.echo(f"error adding content to note.")

@app.command()
def list_notes():
    for i, note in enumerate(list_all_notes):
        typer.echo(f"{i+1}, {note}")


if __name__ == "__main__":
    setup_app(config=config)
    app()
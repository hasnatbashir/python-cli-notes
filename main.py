import typer
from app import setup_app
from config import config
from notes import create_new_note, add_content_to_note, \
    list_all_notes, get_notes_content
app = typer.Typer()
@app.command()
def create_note(name: str):
    try:
        create_new_note(name=name)
        typer.echo(f"created note {name}")
    except ValueError as e:
        typer.echo(f"Error: {e}")
    except:
        typer.echo(f"Error creating new note.")

@app.command()
def append_to_note(name: str, content: str):
    try:
        add_content_to_note(name=name, content=content)
        typer.echo(f"Added content to note {name}")
    except ValueError as e:
        typer.echo(f"Error: {e}")
    except:
        typer.echo(f"Error adding content to note.")

@app.command()
def list_notes():
    try:
        lst_of_notes = list_all_notes()
        if len(lst_of_notes) < 1:
            typer.echo(f"No notes.")
        for i, note in enumerate(lst_of_notes):
            typer.echo(f"{i+1}. {note}")
    except:
        typer.echo(f"Error showing notes.")

@app.command()
def show_content(name: str):
    try:
        typer.echo(get_notes_content(name=name))
    except ValueError as e:
        typer.echo(f"Error: {e}")
    except:
        typer.echo("Error showing content.")



if __name__ == "__main__":
    setup_app(config=config)
    app()
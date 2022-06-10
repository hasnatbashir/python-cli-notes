from typer.testing import CliRunner
from main import app

runner = CliRunner()


def test_create_note():
    result = runner.invoke(app, ["create-note", "demo"])
    assert result.exit_code == 0
    assert "created note demo" in result.stdout

def test_append_to_note():
    result = runner.invoke(app, ["append-to-note", "demo", "some content"])
    assert result.exit_code == 0
    assert "Added content to note demo" in result.stdout

def test_show_content():
    result = runner.invoke(app, ["show-content", "demo"])
    assert result.exit_code == 0
    assert "some content" in result.stdout

def test_list_notes():
    result = runner.invoke(app, ["list-notes"])
    assert result.exit_code == 0
    assert "1. demo.txt" in result.stdout
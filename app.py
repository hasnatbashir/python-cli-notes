import os
import typer
def setup_app(config):
    
    if not os.path.isdir(config['notes_dir']):
        os.mkdir(config["notes_dir"])
    
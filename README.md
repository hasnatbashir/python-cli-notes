# python-cli-notes
Python CLI based app to take notes

## Run app

App command format
```
python main.py [command] [param1] [param2] ...
```
List of available commands
```
python main.py create-note note_name
python main.py append-to-note note_name "content"
python main.py list-notes
python main.py show-content note_name
```

## Project Setup

To setup python environment
```
pip install -r requirements.txt
```

To execute tests.
```
pytest tests/
```

**Note:** Tests are failing since there is no mocking for file system calls can be contributed for future work.

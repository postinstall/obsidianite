# Obsidianite

A simple Python package to process Obsidian Markdown Notes.

## Features
- Load, process, and save Obsidian-compatible Markdown notes
- Parse YAML front matter and note content
- Work with collections of notes in a directory

## Installation

This project uses [uv](https://github.com/astral-sh/uv) for dependency management and installation.

To install the project dependencies, run:

```bash
uv sync
```

Or, if you want to install the project in editable mode:

```bash
uv pip install -e .
```

## Testing

To run the tests, use:

```bash
uv run pytest -v
```

## Usage Example

```python
from obsidianite import Note, Notes

# Load a single note
note = Note.load('path/to/note.md')
print(note.title)
print(note.content)

# Load all notes in a directory
notes = Notes('path/to/vault')
print(notes)
```

## Project Structure

- `src/obsidianite/note.py`   - Note class for single note operations
- `src/obsidianite/notes.py`  - Notes class for collections of notes
- `src/tests/`                - Test suite

## License

MIT License

## Disclaimer

This project was created for my own private use and is shared in the hope that it may be useful to others. 
Please note that it is not a classic open source project with maintainers, ticket systems, or guaranteed fixes.
If you would like additional features or changes, feel free to fork the repository and adapt it to your needs.
Enjoy using it as-is!

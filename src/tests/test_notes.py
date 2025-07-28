import os
from pathlib import Path
from obsidianite import Notes, Note

def test_notes_creation() -> None:
    """
    Test the creation of a Notes collection from a directory and verify its contents.
    Asserts that the notes attribute is a list, contains two notes, and that the first note is an instance of Note.
    """
    notes = Notes(os.path.join(Path(__file__).parent, "data/vault"))
    assert isinstance(notes.notes,list)
    assert len(notes.notes) == 2
    assert isinstance(notes.notes[0],Note)
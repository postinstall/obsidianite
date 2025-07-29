import os
from pathlib import Path
from obsidianite import Notes, Note


def test_notes_creation() -> None:
    """
    Test the creation of a Notes collection from a directory and verify its contents.
    Asserts that the notes attribute is a list, contains two notes, and that the first note is an instance of Note.
    """
    notes = Notes(os.path.join(Path(__file__).parent, "data/vault"))
    assert isinstance(notes.notes, list)
    assert len(notes.notes) == 2
    assert isinstance(notes.notes[0], Note)


def test_has_tags_and_has_any_tags():
    """
    Test the has_tags and has_any_tags methods of the Notes class.
    Assumes the test vault contains notes with tags 'test', 'foo', and 'bar'.
    """
    notes = Notes(os.path.join(Path(__file__).parent, "data/vault"))
    notes_with_both = notes.has_tags(['test', 'data'])
    for note in notes_with_both:
        assert set(['test', 'data']).issubset(set(note.tags()))
    notes_with_any = notes.has_any_tags(['test', 'data'])
    for note in notes_with_any:
        assert set(['test', 'data']) & set(note.tags())


def test_filter_properties():
    """
    Test the filter method of the Notes class by filtering for specific properties.
    Expects that all returned notes have the required properties.
    Also checks that filtering for a non-existent property returns an empty result.
    """
    notes = Notes(os.path.join(Path(__file__).parent, "data/vault"))
    filtered = notes.filter(kind="test")
    for note in filtered:
        assert note.properties.get("kind") == "test"
    assert notes.filter(foo="bar") == []


def test_has_combined():
    """
    Test the has method of the Notes class, which combines tag and property filtering.
    Checks that only notes with all specified tags and properties are returned.
    """
    notes = Notes(os.path.join(Path(__file__).parent, "data/vault"))
    filtered = notes.has(tags=["test"], kind="test")
    for note in filtered:
        assert "test" in note.tags()
        assert note.properties.get("kind") == "test"
    assert notes.has(tags=["notag"], foo="bar") == []

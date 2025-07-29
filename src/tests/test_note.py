from obsidianite import Note
import os


def test_note_creation() -> None:
    """
    Test the creation of a Note object and verify its attributes.
    Returns:
        Note: The created Note object.
    """
    note = Note("test", "# Test", {"kind": "test"}, ".")
    assert note.content == "# Test"
    assert note.properties == {"kind": "test"}
    assert note.title == "test"
    assert note.path == "."


def test_note_save() -> None:
    """
    Test saving a Note object to a markdown file and check if the file exists.
    """
    note = Note("test", "# Test", {"kind": "test"}, ".")
    note.save()
    assert os.path.exists(os.path.join(note.path, note.title + ".md"))


def test_note_load() -> None:
    """
    Test loading a Note object from a markdown file and verify its attributes.
    """
    note = Note.load("test.md")
    assert note.content == "# Test"
    assert note.properties == {"kind": "test"}
    assert note.title == "test"
    assert note.path == "."


def test_note_render() -> None:
    """
    Test rendering a Note object to a markdown string with YAML front matter.
    """
    note = Note("test", "# Test", {"kind": "test"}, ".")
    assert note.render() == "---\nkind: test\n---\n# Test"


def test_note_cleanup() -> None:
    """
    Test cleanup by removing the test markdown file and verifying its removal.
    """
    os.remove("test.md")
    assert not os.path.exists("test.md")

def test_note_tags() -> None:
    """
    Test extracting tags from a Note object.
    """
    note = Note("test", "# Test #tag1 #tag2", {"tags": ["tag3"]}, ".")
    tags = note.tags()
    assert "tag1" in tags
    assert "tag2" in tags
    assert "tag3" in tags
    assert len(tags) == 3  # Ensure no duplicates
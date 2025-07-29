from pathlib import Path
from .note import Note

class Notes:
    def __init__(self, filepath: str):
        """
        Initialize the Notes collection by loading all markdown (.md) files from the given directory path.
        Args:
            filepath (str): The path to the directory containing markdown files.
        Raises:
            FileNotFoundError: If the provided directory does not exist.
        """
        self.notes = []
        p = Path(filepath)
        if not p.exists():
            raise FileNotFoundError(f"Datei nicht gefunden: {filepath}")
        md_files = list(p.rglob("*.md"))
        for md_file in md_files:
            self.notes.append(Note.load(md_file.__str__()))

    def __repr__(self) -> str:
        """
        Return a string representation of all notes in the collection.
        Returns:
            str: A string with each note's dump output separated by newlines.
        """
        return "\n".join([note.dump() for note in self.notes])

    def has_tags(self, tags):
        """
        Return a list of notes that contain all of the specified tags.
        Args:
            tags (list or set): Tags to filter notes by.
        Returns:
            list: Notes that contain all specified tags.
        """
        return [note for note in self.notes if set(tags).issubset(set(note.tags()))]

    def has_any_tags(self, tags):
        """
        Return a list of notes that contain any of the specified tags.
        Args:
            tags (list or set): Tags to filter notes by.
        Returns:
            list: Notes that contain at least one of the specified tags.
        """
        return [note for note in self.notes if set(tags) & set(note.tags())]

    def filter(self, **properties):
        """
        Return a generator of notes that match all specified properties.
        Args:
            **properties: Arbitrary keyword arguments representing note properties and their expected values.
        Returns:
            generator: Notes that match all specified properties.
        """
        return [note for note in self.notes if all(note.properties.get(k) == v for k, v in properties.items())]

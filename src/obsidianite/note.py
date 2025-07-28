import os
from typing import Any
from yaml import safe_dump, safe_load
from pathlib import Path
from json import dumps


class Note:
    """
    Represents a single note with title, content, properties, and file path.
    """

    def __init__(
        self, title: str, content: str, properties: dict[str, Any], path: str = "."
    ):
        """
        Initialize a Note instance.
        Args:
            title (str): The title of the note.
            content (str): The main content of the note.
            properties (dict[str, Any]): Metadata properties of the note.
            path (str, optional): The directory path of the note. Defaults to ".".
        """
        self.title = title
        self.content = content
        self.properties = properties
        self.path = path

    def __repr__(self) -> str:
        """
        Return a string representation of the note (JSON format).
        Returns:
            str: JSON string of the note's data.
        """
        return self.dump()

    def dump(self) -> str:
        """
        Dump the note's data as a JSON string.
        Returns:
            str: JSON string of the note's data.
        """
        return dumps(
            {
                "title": self.title,
                "path": self.path,
                "properties": self.properties,
                "content": self.content.strip(),
            },
            indent=2,
            ensure_ascii=False,
        )

    def render(self) -> str:
        """
        Render the note as a markdown string with YAML front matter.
        Returns:
            str: Markdown string with YAML front matter and content.
        """
        return f"---\n{safe_dump(self.properties).strip()}\n---\n{self.content.strip()}"

    def save(self, filepath: str | None = None) -> None:
        """
        Save the note to a markdown file.
        Args:
            filepath (str|None, optional): The file path to save the note. If None, uses the note's title and path.
        """
        if not filepath:
            filepath = os.path.join(self.path, self.title + ".md")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(self.render())

    @classmethod
    def load(cls, filepath: str) -> "Note":
        """
        Load a note from a markdown file.
        Args:
            filepath (str): The path to the markdown file.
        Returns:
            Note: The loaded Note instance.
        Raises:
            FileNotFoundError: If the file does not exist.
        """
        p = Path(filepath)
        if not p.exists():
            raise FileNotFoundError(f"Datei nicht gefunden: {filepath}")
        title = p.stem
        parent_path = p.parent.__str__()
        with open(filepath, encoding="utf-8") as f:
            md_text = f.read()
            if md_text.startswith("---"):
                parts = md_text.split("---", 2)
                if len(parts) >= 3:
                    _, yaml_block, content = parts
                    properties = safe_load(yaml_block.strip())
                    return cls(title, content.strip(), properties, parent_path)
            return cls(title, md_text, {}, parent_path)

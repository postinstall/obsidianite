from obsidianite import Notes

notes = Notes("tests/data/vault")
for note in notes.notes:
  print(note.path, note.title, note.tags())
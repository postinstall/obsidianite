from obsidianite import Notes

notes = Notes("tests/data/vault")
for note in notes.has_tags(['random']):
  print(note.fullpath(), note.tags())
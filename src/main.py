from obsidianite import Note, insert_string_after_heading



# Lade die Notiz
note = Note.load("tests/data/vault/folder/data.md")

# Füge nach einem H2-Heading mit dem Titel "Links" den Text "- TEst" ein
new_content = insert_string_after_heading(note.content, "## Links", "- blubb")

# Optional: Ausgabe oder speichern
print(new_content)
# note.content = new_content
# note.save()

from obsidianite import Notes, insert_string_after_heading, parse_link



def main():
    notes = Notes("D:/Cloud/Nextcloud.W11/Vault/Recording/Projects/Neuroticfish/")
    for note in notes.filter(kind=["song"], status="released"):
        artist = note.properties.get("artist")
        title = note.title
        release = note.properties.get("releases")[0]
        album = parse_link(release)
        print(artist, title, album, note.properties.get("status"))


if __name__ == "__main__":
    main()
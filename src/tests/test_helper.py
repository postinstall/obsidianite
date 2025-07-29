from obsidianite import insert_string_after_heading, parse_link


def test_insert_string_after_heading():
    """
    Test insert_string_after_heading by inserting a string after a heading of any level.
    """
    content = "# Title\nSome intro\n\n## Links\nOld content\n\n## Other\n"
    result = insert_string_after_heading(content, "## Links", "- Inserted item")
    assert "## Links\n- Inserted item" in result
    result2 = insert_string_after_heading(content, "# Title", "Paragraph after title")
    assert "# Title\nParagraph after title" in result2
    result3 = insert_string_after_heading(content, "### NotThere", "Should not appear")
    assert "Should not appear" not in result3

def test_parse_link():
    """Test the parse_link function with various Obsidian link formats."""
    assert parse_link("[[Note]]") == "Note"
    assert parse_link("[[Note|Alias]]") == "Alias"
    assert parse_link("No links here") == "No links here"

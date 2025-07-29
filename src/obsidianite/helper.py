import re

def insert_string_after_heading(content: str, heading: str, insert: str) -> str:
    """
    Insert a string after a heading with the given level and title.
    Args:
        content (str): The markdown content.
        heading (str): The heading, e.g. '## Links' or '# Title'.
        insert_str (str): The string to insert after the heading.
    Returns:
        str: The modified markdown content.
    """
    match = re.match(r'^(#+)\s+(.*)$', heading)
    if match:
      hashes, title = match.groups()
      pattern = r'(^' + ('#' * len(hashes)) + r' +' + re.escape(title) + r'.*?$)'
      replacement = r"\1\n" + insert
      return re.sub(pattern, replacement, content, flags=re.MULTILINE)
    else:
      return content

def parse_link(text: str) -> str:
    """
    Parses a string for an Obsidian-style link ([[...]]). If the string is not a link, returns the string as is.
    If the link contains a '|', returns only the part after the '|'.
    Args:
        text (str): The input string.
    Returns:
        str: The parsed link or the original string.
    """
    match = re.match(r"^\[\[([^\]|]+)(?:\|([^\]]+))?\]\]$", text)
    if match:
        if match.group(2):
            return match.group(2)
        return match.group(1)
    return text

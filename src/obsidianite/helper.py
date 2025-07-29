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

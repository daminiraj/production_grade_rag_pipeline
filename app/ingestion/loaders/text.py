import logfire

def parse_text(file_path: str) -> str:
    """
    Load text from a file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The content of the text file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except Exception as e:
        logfire.error(f"Failed to load text from {file_path}: {e}")
        raise
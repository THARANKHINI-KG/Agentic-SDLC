from pathlib import Path
from langchain.tools import tool


@tool
def get_python_guidelines() -> str:
    """
    Returns Python coding guidelines.
    """

    return Path(
        "Python_Guidelines.md"
    ).read_text(
        encoding="utf-8"
    )
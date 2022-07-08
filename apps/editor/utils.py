import uuid
from typing import List


def formatted_markdown(markdown: str):
    # markdown: str = "".join(str(markdown).split("\n")).replace("\r", "$//$")
    result = {}
    for i in str(markdown).split("\n"):
        result[str(uuid.uuid4())] = i

    return result

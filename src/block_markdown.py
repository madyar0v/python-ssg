import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"


def markdown_to_blocks(markdown):
    return [line.strip() for line in markdown.split("\n\n") if line != ""]


def block_to_block_type(block):
    lines = block.split("\n")
    # Heading
    if len(lines) == 1 and re.match("^#{1,6} \w+", block):
        return block_type_heading

    # Code
    if block[:3] == block[-3:] == "```":
        return block_type_code

    # Quote, ul, ol
    quote, ul, ol = True, True, True
    for i, line in enumerate(lines):
        if not re.match("^> \w+", line):
            quote = False
        if not re.match("^[\*,\-] \w+", line):
            ul = False
        if not re.match(f"^{i + 1}. \w+", line):
            ol = False

    if quote:
        return block_type_quote
    if ul:
        return block_type_ulist
    if ol:
        return block_type_olist
    return block_type_paragraph

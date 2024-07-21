import unittest
from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_code,
    block_type_olist,
    block_type_ulist,
    block_type_quote,
    block_type_heading,
    block_type_paragraph,
)


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        actual = markdown_to_blocks(markdown)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertEqual(actual, expected)

    def test_markdown_to_blocks_miltiple_empty_lines(self):
        markdown = """# This is a heading


This is a paragraph of text. It has some **bold** and *italic* words inside of it.


* This is the first list item in a list block
* This is a list item
* This is another list item"""

        actual = markdown_to_blocks(markdown)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertEqual(actual, expected)

    def test_markdown_to_blocks_no_empty_lines(self):
        markdown = """# This is a heading
This is a paragraph of text. It has some **bold** and *italic* words inside of it."""
        actual = markdown_to_blocks(markdown)
        expected = [
            "# This is a heading\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it."
        ]
        self.assertEqual(actual, expected)

    def test_block_to_block_type_heading_1(self):
        markdown = "# This is a heading"
        actual = block_to_block_type(markdown)
        expected = block_type_heading
        self.assertEqual(actual, expected)

    def test_block_to_block_type_heading_3(self):
        markdown = "### This is a heading"
        actual = block_to_block_type(markdown)
        expected = block_type_heading
        self.assertEqual(actual, expected)

    def test_block_to_block_type_heading_6(self):
        markdown = "###### This is a heading"
        actual = block_to_block_type(markdown)
        expected = block_type_heading
        self.assertEqual(actual, expected)

    def test_block_to_block_type_heading_7(self):
        markdown = "####### This is not a heading"
        actual = block_to_block_type(markdown)
        expected = block_type_paragraph
        self.assertEqual(actual, expected)

    def test_block_to_block_type_code_oneline(self):
        markdown = "```This is code```"
        actual = block_to_block_type(markdown)
        expected = block_type_code
        self.assertEqual(actual, expected)

    def test_block_to_block_type_code_multiline(self):
        markdown = """```This is multiline
        code```"""
        actual = block_to_block_type(markdown)
        expected = block_type_code
        self.assertEqual(actual, expected)

    def test_block_to_block_type_quote(self):
        markdown = "> One line quote"
        actual = block_to_block_type(markdown)
        expected = block_type_quote
        self.assertEqual(actual, expected)

    def test_block_to_block_type_quote_multiline(self):
        markdown = """> Multi line quote\n> Second line"""
        actual = block_to_block_type(markdown)
        expected = block_type_quote
        self.assertEqual(actual, expected)

    def test_block_to_block_type_unordered_list_one_el(self):
        markdown = "* first elemenent"
        actual = block_to_block_type(markdown)
        expected = block_type_ulist
        self.assertEqual(actual, expected)

    def test_block_to_block_type_unordered_list_multiple_el(self):
        markdown = """* first elemenent\n* Second element"""
        actual = block_to_block_type(markdown)
        expected = block_type_ulist
        self.assertEqual(actual, expected)

    def test_block_to_block_type_ordered_list_one_el(self):
        markdown = "1. first elemenent"
        actual = block_to_block_type(markdown)
        expected = block_type_olist
        self.assertEqual(actual, expected)

    def test_block_to_block_type_ordered_list_multiple_el(self):
        markdown = "1. first elemenent\n2. second element"
        actual = block_to_block_type(markdown)
        expected = block_type_olist
        self.assertEqual(actual, expected)

    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* list\n* items"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)

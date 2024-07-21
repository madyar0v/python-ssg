import unittest
from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_italic,
    text_type_code,
    text_type_bold,
    text_type_image,
    text_type_link,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode("This is text with a **bolded** word and **another**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bolded", text_type_bold),
                TextNode(" word and ", text_type_text),
                TextNode("another", text_type_bold),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual(
            [
                TextNode("bold", text_type_bold),
                TextNode(" and ", text_type_text),
                TextNode("italic", text_type_italic),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes,
        )

    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        actual_extracted = extract_markdown_images(text)
        expected_extracted = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(actual_extracted, expected_extracted)

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        actual_extracted = extract_markdown_links(text)
        expected_extracted = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(actual_extracted, expected_extracted)

    def test_extract_markdown_images_unclosed_alt(self):
        text = "This is text with a ![rick roll(https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        try:
            extract_markdown_images(text)
        except Exception as e:
            self.assertEqual(type(e), ValueError)

    def test_extract_markdown_links_unclosed_url(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev"
        try:
            extract_markdown_links(text)
        except Exception as e:
            self.assertEqual(type(e), ValueError)

    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        actual_split = split_nodes_link([node])
        expected_split = [
            TextNode("This is text with a link ", text_type_text),
            TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode(
                "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(actual_split, expected_split)

    # def test_split_nodes_link_not_closed(self):
    #     node = TextNode(
    #         "This is text with a link [to boot dev(https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    #         text_type_text,
    #     )
    #     try:
    #         split_nodes_link([node])
    #     except Exception as e:
    #         self.assertEqual(type(e), ValueError)
    #
    # def test_split_nodes_image_not_closed(self):
    #     node = TextNode(
    #         "This is text with a image ![to boot dev(https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    #         text_type_text,
    #     )
    #     try:
    #         split_nodes_image([node])
    #     except Exception as e:
    #         self.assertEqual(type(e), ValueError)

    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an image ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
            text_type_text,
        )
        actual_split = split_nodes_image([node])
        expected_split = [
            TextNode("This is text with an image ", text_type_text),
            TextNode("to boot dev", text_type_image, "https://www.boot.dev"),
            TextNode(" and ", text_type_text),
            TextNode(
                "to youtube", text_type_image, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(actual_split, expected_split)

    def test_split_nodes_image_no_text(self):
        node = TextNode(
            "",
            text_type_text,
        )
        actual_split = split_nodes_image([node])
        expected_split = []
        self.assertEqual(actual_split, expected_split)

    def test_split_nodes_image_no_images(self):
        node = TextNode(
            "This is text with no image",
            text_type_text,
        )
        actual_split = split_nodes_image([node])
        expected_split = [
            TextNode("This is text with no image", text_type_text),
        ]
        self.assertEqual(actual_split, expected_split)

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected = [
            TextNode("This is ", text_type_text),
            TextNode("text", text_type_bold),
            TextNode(" with an ", text_type_text),
            TextNode("italic", text_type_italic),
            TextNode(" word and a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" and an ", text_type_text),
            TextNode("obi wan image", text_type_image, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", text_type_text),
            TextNode("link", text_type_link, "https://boot.dev"),
        ]
        actual = text_to_textnodes(text)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

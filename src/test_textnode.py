import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    text_node_to_html_node,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", text_type_text, "https://google.com")
        node2 = TextNode("This is a text node", text_type_text, "https://google.com")
        self.assertEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", text_type_text, "https://google.com")
        node2 = TextNode("This is a text node", text_type_text, "https://boot.dev")
        self.assertNotEqual(node, node2)

    def test_not_eq_url_none(self):
        node = TextNode("This is a text node", text_type_text, "https://google.com")
        node2 = TextNode("This is a text node", text_type_text)
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node2", text_type_text)
        self.assertNotEqual(node, node2)

    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node_type_text(self):
        node = TextNode("Text of type text", text_type_text)
        leafnode = text_node_to_html_node(node)
        self.assertEqual(leafnode.__repr__(), "LeafNode(None, Text of type text, None)")

    def test_text_node_to_html_node_type_bold(self):
        node = TextNode("Text of type bold", text_type_bold)
        leafnode = text_node_to_html_node(node)
        self.assertEqual(leafnode.__repr__(), "LeafNode(b, Text of type bold, None)")

    def test_text_node_to_html_node_type_italic(self):
        node = TextNode("Text of type italic", text_type_italic)
        leafnode = text_node_to_html_node(node)
        self.assertEqual(leafnode.__repr__(), "LeafNode(i, Text of type italic, None)")

    def test_text_node_to_html_node_type_code(self):
        node = TextNode("Text of type code", text_type_code)
        leafnode = text_node_to_html_node(node)
        self.assertEqual(leafnode.__repr__(), "LeafNode(code, Text of type code, None)")

    def test_text_node_to_html_node_type_link(self):
        node = TextNode("Text of type link", text_type_link)
        leafnode = text_node_to_html_node(node)
        self.assertEqual(leafnode.__repr__(), "LeafNode(a, Text of type link, {'href': ''})")

    def test_text_node_to_html_node_type_image(self):
        node = TextNode("Text of type image", text_type_image)
        leafnode = text_node_to_html_node(node)
        self.assertEqual(leafnode.__repr__(), "LeafNode(img, , {'src': 'image URL', 'alt': 'alt text'})")


if __name__ == "__main__":
    unittest.main()

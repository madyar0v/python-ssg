from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(tag=None, value=text_node.text)
        case "bold":
            return LeafNode(tag="b", value=text_node.text)
        case "italic":
            return LeafNode(tag="i", value=text_node.text)
        case "code":
            return LeafNode(tag="code", value=text_node.text)
        case "link":
            return LeafNode(tag="a", value=text_node.text, props={"href": ""})
        case "image":
            return LeafNode(tag="img", value="", props={"src": "image URL", "alt": "alt text"})
        case _:
            raise Exception("Unknown node type!")


# def main():
#     nodes = [
#         TextNode("1 This is text with a `code block` word 1", text_type_text),
#         TextNode("`2 This is text with a `code block word 2", text_type_text),
#         TextNode("3 This is text with a `code block word 3`", text_type_text),
#     ]
#
#     new_nodes = split_nodes_delimiter(nodes, "`", text_type_code)
#     for node in new_nodes:
#         print(node.__repr__())
#         print("_____________________")
#

#main()

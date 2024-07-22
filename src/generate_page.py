import os
from markdown_to_html import markdown_to_html_node


def generate_page(from_path, template_path, dest_path):
    print("Generating page...")
    print(f" * {from_path} {template_path} -> {dest_path}")
    with open(from_path, "r") as f:
        markdown_text = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    node = markdown_to_html_node(markdown_text)
    html = node.to_html()

    title = extract_title(markdown_text)
    template = template.replace("{{ Ttitle }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(template)


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No title found")

import os
from static_copy import static_copy, clear_directory
from generate_page import generate_page

static_dir = "./static"
public_dir = "./public"
content_dir = "./content"
template_path = "./template.html"


def main():
    clear_directory(public_dir)
    static_copy(static_dir, public_dir)
    generate_page(
        os.path.join(content_dir, "index.md"),
        template_path,
        os.path.join(public_dir, "index.html"),
    )


main()

import os
from static_copy import static_copy, clear_directory
from generate_page import generate_pages_recursive

static_dir = "./static"
public_dir = "./public"
content_dir = "./content"
template_path = "./template.html"


def main():
    clear_directory(public_dir)
    static_copy(static_dir, public_dir)
    generate_pages_recursive(content_dir, template_path, public_dir)


main()

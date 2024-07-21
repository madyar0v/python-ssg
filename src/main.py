import os
from static_copy import static_copy, clear_directory

static_dir = os.path.relpath('./static', start=os.curdir)
public_dir = os.path.relpath('./public', start=os.curdir)


def main():
    clear_directory(public_dir)
    static_copy(static_dir, public_dir)


main()

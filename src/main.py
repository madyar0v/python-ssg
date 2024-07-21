import os
import shutil


STATIC_DIR = os.path.relpath('./static', start=os.curdir)
PUBLIC_DIR = os.path.relpath('./public', start=os.curdir)


def main():
    print(os.listdir(PUBLIC_DIR))
    print("Clearing public dir...")
    shutil.rmtree(PUBLIC_DIR)
    print(os.listdir(PUBLIC_DIR))


main()

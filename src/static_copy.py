import os
import shutil


def clear_directory(dir):
    if os.path.isdir(dir):
        print(f"Clearing out {dir} directory")
        shutil.rmtree(dir)
        create_directory(dir)
    else:
        print(f"{dir} not found. Creating...")
        create_directory(dir)


def create_directory(dir):
    os.mkdir(dir)
    os.chmod(dir, 0o755)


def static_copy(src, dst):
    if not os.path.exists(dst):
        create_directory(dst)

    for src_item in os.listdir(src):
        src_path = os.path.join(src, src_item)
        dst_path = os.path.join(dst, src_item)
        if os.path.isfile(src_path):
            print(f"Copying {src_path} into {dst}")
            shutil.copy(src_path, dst_path)
        else:
            static_copy(src_path, dst_path)

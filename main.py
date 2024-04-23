import os
import shutil


def delete_pycache(directory):
    for root, dirs, files in os.walk(directory):
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            shutil.rmtree(pycache_path)
            print(f"Deleted {pycache_path}")


# Replace '.' with the path of the directory where you want to start deleting __pycache__ folders
delete_pycache(".")

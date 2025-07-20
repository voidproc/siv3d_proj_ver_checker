import os

def list_files(root_dir, extensions):
    """指定されたディレクトリ以下のすべてのファイルをリストアップする"""
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                yield os.path.join(dirpath, filename)

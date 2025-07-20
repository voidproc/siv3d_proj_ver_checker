import os
import re
from .list_files import list_files


def extract_versions_from_content(content, regex):
    """文字列から正規表現に一致するバージョンをすべて抽出する"""
    return set(match.group(1) for match in regex.finditer(content))


def extract_versions_from_file(file_path, regex):
    """単一のファイルからバージョンを抽出する"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return extract_versions_from_content(content, regex)
    except Exception as e:
        print(f'Error reading {file_path}: {e}')
        return set()


def extract_versions_from_files(root_dir, extensions, search_pattern):
    result = []
    regex = re.compile(search_pattern)

    for file_path in list_files(root_dir, extensions):
        ver_set = extract_versions_from_file(file_path, regex)
        if ver_set:
            rel_path = os.path.relpath(file_path, root_dir)
            result.append({
                'relative_path': rel_path,
                'versions': ver_set
            })
    
    return result

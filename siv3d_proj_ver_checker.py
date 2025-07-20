import io
import itertools
import os
import re
from collections import Counter
import sys

TARGET_EXTENSIONS = ['.vcxproj']
SEARCH_PATTERN = r'\$\(\s*SIV3D_([0-9]+_[0-9]+_[0-9]+)\s*\)'


def list_target_files(root_dir, extensions):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                yield os.path.join(dirpath, filename)


def extract_versions_from_content(content, regex):
    return set(match.group(1) for match in regex.finditer(content))


def extract_versions_from_file(file_path, regex):
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

    for file_path in list_target_files(root_dir, extensions):
        ver_set = extract_versions_from_file(file_path, regex)
        if ver_set:
            rel_path = os.path.relpath(file_path, root_dir)
            result.append({
                'relative_path': rel_path,
                'versions': ver_set
            })
    
    return result


def version_key(ver_str):
    return tuple(int(x) for x in ver_str.split('_'))


def get_folder_path_from_args():
    if len(sys.argv) < 2:
        print("使い方: python your_script.py <フォルダパス>")
        print("例: python your_script.py /path/to/your/folder")
        return None

    folder_path = sys.argv[1]

    if not os.path.exists(folder_path):
        print(f"エラー: 指定されたパス '{folder_path}' は存在しません。")
        return None
    if not os.path.isdir(folder_path):
        print(f"エラー: 指定されたパス '{folder_path}' はフォルダではありません。")
        return None

    return folder_path


if __name__ == '__main__':
    root_dir = get_folder_path_from_args()
    vers = extract_versions_from_files(root_dir, TARGET_EXTENSIONS, SEARCH_PATTERN)

    for item in vers:
        print(f'{item["relative_path"]}: {", ".join(item["versions"])}')

    version_sets = map(lambda item: item["versions"], vers)
    all_versions = itertools.chain.from_iterable(version_sets)
    version_counter = Counter(all_versions)

    for version in sorted(version_counter.keys(), key=version_key):
        print(f'{version}: {version_counter[version]}')

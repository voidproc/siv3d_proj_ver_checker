import itertools
import os
import sys
from collections import Counter

from .config import TARGET_EXTENSIONS, SEARCH_PATTERN
from .extract_versions import extract_versions_from_files
from .utils import version_key


def get_folder_path_from_args():
    if len(sys.argv) < 2:
        print("使い方: siv3d-checker <フォルダパス>")
        return None

    folder_path = sys.argv[1]

    if not os.path.exists(folder_path):
        print(f"エラー: 指定されたパス '{folder_path}' は存在しません。")
        return None

    if not os.path.isdir(folder_path):
        print(f"エラー: 指定されたパス '{folder_path}' はフォルダではありません。")
        return None

    return folder_path


def main():
    root_dir = get_folder_path_from_args()
    if root_dir:
        vers = extract_versions_from_files(root_dir, TARGET_EXTENSIONS, SEARCH_PATTERN)

        for item in vers:
            print(f'{item["relative_path"]}: {", ".join(item["versions"])}')

        version_sets = map(lambda item: item["versions"], vers)
        all_versions = itertools.chain.from_iterable(version_sets)
        version_counter = Counter(all_versions)

        for version in sorted(version_counter.keys(), key=version_key):
            print(f'{version}: {version_counter[version]}')


if __name__ == '__main__':
    main()

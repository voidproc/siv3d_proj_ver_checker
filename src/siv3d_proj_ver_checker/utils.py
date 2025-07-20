def version_key(ver_str):
    """バージョン文字列（例: '0_6_6'）をソート可能なタプルに変換する"""
    return tuple(int(x) for x in ver_str.split('_'))

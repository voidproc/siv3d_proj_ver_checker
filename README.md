# Siv3D Project Version Checker

このツールは、指定されたディレクトリ内にある C++ プロジェクトファイル（`*.vcxproj`）を検索し、使用されている [Siv3D](https://siv3d.github.io/) のバージョンを一覧表示します。

プロジェクトごとにどのバージョンの Siv3D が使われているかを確認したり、複数のプロジェクトで利用されているバージョンを統一したりする際に役立ちます。

## 主な機能

指定されたディレクトリ以下を再帰的に検索し、見つかったプロジェクトファイル内から `$(SIV3D_X_Y_Z)` のような形式で記述された Siv3D のバージョン番号を抽出します。その後、以下を出力します。

- プロジェクトファイルごとに検出されたバージョン
- 各バージョンについて、使用されているプロジェクトの数

## インストール

このリポジトリをクローンします。

```
git clone https://github.com/voidproc/siv3d_proj_ver_checker.git
cd siv3d_proj_ver_checker
```

次に、以下のコマンドでインストールします。`siv3d-checker` コマンドが使えるようになります。

```
pip install .
```

## 使い方

インストール後、ターミナルで以下のコマンドを実行します。

```
siv3d-checker <検索したいディレクトリのパス>
```

## 出力例

```
path\to\project1\project1.vcxproj: 0_6_5
path\to\project2\project2.vcxproj: 0_6_6
path\to\project3\project3.vcxproj: 0_6_5
0_6_5: 2
0_6_6: 1
```

## 動作環境

- Python 3.12 で動作確認
- 外部ライブラリへの依存はありません。
- 開発環境では [uv](https://github.com/astral-sh/uv) を使用しています。

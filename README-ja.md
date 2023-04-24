# PDF分割ツール

このPythonスクリプトは、指定されたページ数でPDFファイルを複数のファイルに分割し、指定されたディレクトリに保存するツールです。

## 必要なもの

- Python 3.x
- pypdfライブラリ

pypdfライブラリは、pipを使用してインストールできます:

```
pip install pypdf
```

## 使い方

```
python split_pdf.py <input_file> <output_dir> [page_range]
```

- `input_file`: 入力PDFファイルの名前
- `output_dir`: 出力ディレクトリの名前
- `page_range`: (オプション) 1つの出力ファイルに含まれるページ数。デフォルトは20です。

使用例:

```
python split_pdf.py input.pdf output_folder 10
```

これにより、`input.pdf`ファイルが10ページごとに複数のファイルに分割され、`output_folder`に保存されます。

## 機能

`split_pdf_file()`関数は、次の3つの引数を取ります:

- `input_file`: 入力PDFファイルの名前。
- `output_dir`: 出力ディレクトリの名前。
- `page_range`: 1つの出力ファイルに含まれるページ数。デフォルトは20です。

この関数は、作成された出力ファイルの数を返します。

スクリプトでは、pypdfライブラリを使用して、入力PDFファイルを読み取り、出力ファイルの数を計算し、出力ファイルを保存します。出力ファイルは、入力ファイル名と数値の接尾辞を使用して命名されます。

出力ディレクトリが存在しない場合は、作成されます。

## ライセンス

このスクリプトはMITライセンスの下で提供されています。
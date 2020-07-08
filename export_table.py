#!/usr/bin/python
# -*- coding: utf-8 -*-
"""PDFから表を抽出

Examples:

    ::

        $ python export_table.py test.pdf 1
"""

import pandas as pd
import tabula
import sys
import os

def print_debug(dfs):
    """デバッグ情報表示
    Args
        dfs (list):
    Returns: none
    """

    print(type(dfs))
    for df in dfs:
        print(df)

def main():
    """メイン関数
        Returns: none
    """

    args = sys.argv
    pdf_file_path = args[1]
    page_number = args[2]
    pdf_file_basename = os.path.basename(pdf_file_path)
    excel_file_path = pdf_file_basename + ".xlsx"

    # lattice=Trueでテーブルの軸線でセルを判定
    dfs = tabula.read_pdf(pdf_file_path, lattice=True, pages = page_number)

    print_debug(dfs)
    df = dfs[0]
    df.to_excel(excel_file_path, index=None)

if __name__ == '__main__':
    main()

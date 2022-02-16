import os
from functools import reduce

from typing import List

from drawfunction.main import draw
from drawfunction.fibonacci import fib


def generate_latex_table(table: List[List[str]]) -> str:
    def generate_style():
        return reduce(
            lambda first, second: f'{first}|{second}',
            map(lambda _: 'c', table[0]),
        )

    def generate_content():
        return reduce(
            str.__add__,
            map(
                lambda row: str.join(' & ', row) + ' \\\\\n',
                table
            )
        )

    return f'\\begin{{tabular}}{{{generate_style()}}}\n' \
           f'\\hline\n' \
           f'{generate_content()}' \
           f'\\hline\n' \
           f'\\end{{tabular}}\n'


def generate_picture():
    draw(fib)
    return f'\\includegraphics[width=\\linewidth]{{{"artifacts/tree.png"}}}\n'


def embed_content(content: str) -> str:
    return f'\\documentclass{{article}}\n' \
           f'\\usepackage{{graphicx}}\n' \
           f'\\begin{{document}}\n' \
           f'{content}' \
           f'\\end{{document}}\n'


if __name__ == "__main__":
    table = generate_latex_table(
        [
            ['1', '2', '3'],
            ['4', '5', '6'],
        ]
    )
    picture = generate_picture()
    content = ''.join([table, picture])

    with open("artifacts/result.tex", "w") as file:
        file.write(embed_content(content))

    os.system(f"pdflatex -output-directory=artifacts artifacts/result.tex")
    os.system(f"rm artifacts/result.aux artifacts/result.log")

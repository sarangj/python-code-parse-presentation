import argparse
import ast
import tokenize

import astpretty
import libcst


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--e', dest='example', required=True)
    args = parser.parse_args()
    example = args.example
    if example == 'tokenizer':
        run_tokenizer()
    elif example == 'ast':
        run_ast()
    elif example == 'cst':
        run_cst()


def run_tokenizer():
    with open('example.py', 'r') as f:
        for token in tokenize.generate_tokens(f.readline):
            print(token)


def run_ast():
    with open('example.py', 'r') as f:
        src = f.read()

    astpretty.pprint(ast.parse(src))


def run_cst():
    with open('example.py', 'r') as f:
        src = f.read()

    print(libcst.parse_module(src))


if __name__ == '__main__':
    main()

"""
NOTE: Do not modify this file unless you want to change the name
      of the main.py file. Then it is necessary to adapt the import.
"""

from permedcoe import invoker
from build_model_from_genes.main import invoke


def main():
    invoker(invoke)  # Does automatically the parameter parsing


if __name__ == "__main__":
    main()

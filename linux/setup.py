import os

from shutil import copyfile
from pathlib import PosixPath


def main(args):
    print("Running Linux specific environment setup...")
    # os.system("chsh -s $(which zsh)")
    print("Overwriting zshrc")
    copyfile(PosixPath("./linux/zshrc"), PosixPath("~/.zshrc").expanduser())


def after(args):
    os.system("python3 ~/.vim/bundle/YouCompleteMe/install.py --all")

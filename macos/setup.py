from shutil import copyfile
from pathlib import PosixPath


def main(args):
    print("Running MacOS specific environment setup...")
    print("Overwriting zshrc")
    copyfile(PosixPath("./macos/zshrc"), PosixPath("~/.zshrc").expanduser())

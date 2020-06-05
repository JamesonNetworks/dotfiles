from shutil import copyfile
from pathlib import PosixPath
import os


def installFonts(args):
    print("Install PowerLine Fonts from: https://github.com/powerline/fonts")
    


def main(args):
    print("Running MacOS specific environment setup...")
    print("Overwriting zshrc")
    copyfile(PosixPath("./macos/zshrc"), PosixPath("~/.zshrc").expanduser())
    installFonts(args=args)


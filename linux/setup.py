import os


def main(args):
    print("Running Linux specific environment setup...")
    #os.system("chsh -s $(which zsh)")
    print("Overwriting zshrc")
    copyfile(PosixPath("./linux/zshrc"), PosixPath("~/.zshrc").expanduser())


def after(args):
    os.system("cd ~/.vim/bundle/YouCompleteMe")
    os.system("python3 install.py --all")

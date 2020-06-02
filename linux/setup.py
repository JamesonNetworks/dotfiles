import os


def main(args):
    print("Running Linux specific environment setup...")
    #os.system("chsh -s $(which zsh)")


def after(args):
    os.system("cd ~/.vim/bundle/YouCompleteMe")
    os.system("python3 install.py --all")

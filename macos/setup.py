from shutil import copyfile

def main(args):
	print("Running MacOS specific environment setup...")
    print("Overwriting zshrc")
    copyfile(PosixPath("./macos/zshrc"), PosixPath("~/.zshrc").expanduser())

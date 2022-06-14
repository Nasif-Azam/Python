from pathlib import Path
# Absolute Path {Import from computer}
path = Path("D:\\Game")
print(path.exists())


# Relative Path {Import from python projects}
# path = Path("Package")
# print(path.exists())

# path = Path("Emails")
# path.mkdir()  # To create a directory
# path.rmdir()  # To remove a directory

# path = Path()
# for directory in path.glob("*"):
#     print(directory)

# path = Path()
# for files in path.glob("*.py"):
#     print(files)

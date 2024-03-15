import os


def remove_unused_files():
    if "{{ cookiecutter.dependency_manager }}" != "pip":
        os.remove("requirements.txt")
        os.remove("requirements-dev.txt")
    if "{{ cookiecutter.use_sqlfluff }}" == "no":
        os.remove(".sqlfluff")


if __name__ == "__main__":
    remove_unused_files()

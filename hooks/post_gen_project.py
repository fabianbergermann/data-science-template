import os
import shutil


def remove_unused_files():
    if "{{ cookiecutter.dependency_manager }}" != "pip":
        os.remove("requirements.txt")
        os.remove("requirements-dev.txt")
    if "{{ cookiecutter.use_sqlfluff }}" == "no":
        os.remove(".sqlfluff")
    if "{{ cookiecutter.use_github_actions }}" == "no":
        shutil.rmtree(".github")


if __name__ == "__main__":
    remove_unused_files()

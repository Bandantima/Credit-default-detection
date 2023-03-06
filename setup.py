from setuptools import find_packages,setup
from typing import List

requirement_file_name = "requirements.txt"

def get_requirements()->List[str]:
    with open(requirement_file_name) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]

        if "-e ." in requirement_list:
            requirement_list.remove("-e .")

    return requirement_list

setup(
    name = "Credit",
    version = "0.0.1",
    description='This is a industry level Project',
    author = "Antima Band",
    author_email = "antimapatel02@gmail.com",
    packages = find_packages(), 
    install_requires = get_requirements(),
)
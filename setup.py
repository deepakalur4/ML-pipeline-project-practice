from setuptools import find_packages,setup
from typing import List


def get_pack(file_path:str)->list:
    '''
    This function will return the list of packages in requirements.txt file
    '''
    with open(file_path,"r")  as file_obj:
        pack=file_obj.readlines()
        return [i.replace("\n","") for i in pack if i not in "-e ."]

setup(
    name="ML End to End pipeline",
    version="0.0.0.0",
    author="Deepak S Alur",
    author_email="Deepaka;lur4@gmail.com",
    packages=find_packages(),
    install_requires=get_pack("requirements.txt")

)

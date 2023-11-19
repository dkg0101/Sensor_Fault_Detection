from setuptools import find_packages,setup
from typing import List

REQUIREMENT_FILE_NAME = "requirements.txt"
HYPEN_E_DOT = '-e .'


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mentioned in requirements.txt file 
    """
    requirements=[]
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirements = requirement_file.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        
        if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)


    return requirements


setup (
    name ='sensor',
    version='0.0.1',
    author='dhananjay gurav',
    author_email='dkgurav0101@gmail.com',
    packages= find_packages(),
    install_requires=get_requirements_list()
)



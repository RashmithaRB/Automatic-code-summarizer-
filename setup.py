from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the function of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='Automatic Code Sumarization',
    version='0.0.1',
    author='Namratha,Pratheeksha,Rashmitha',
    author_email='nm788186@gmail.com,pratheekshasudhir@gmail.com,nnm22is126@nmamit.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
      
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ")for req in requirements]

        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
setup(
name='mlproject',
version='0.0.1',
anthor='Xuehan CAI',
author_email='scyxc5@nottingham.edu.cn',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
    
    
)
'''
The setup.py file is an essential part of packing and distributing python projects.
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    '''
    This function will return list of requirements
    '''
    hypen_e_dot = '-e .'
    requirement_list:list[str] = []
    try:
        with open('requirements.txt','r') as file:
            # Read lines from file
            lines = file.readlines()
            # Process each line 
            for line in lines:
                requirement = line.strip()
                # Ignore the empty lines and also -e .
                if requirement and requirement != hypen_e_dot:
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found')
    
    return requirement_list

setup(
    name = "NetworkSecurity",
    version = '0.0.1',
    author = 'HardikJain',
    author_email = 'hj791983@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements()
)
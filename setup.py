from setuptools import find_packages, setup
from typing import List

HYP_E_DOT = '-e .'
def get_req(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    req = []
    with open(file_path) as f_obj:
        req = f_obj.readlines()
        req = [r.replace("\n", "") for r in req]

        if HYP_E_DOT in req:
            req.remove(HYP_E_DOT)
    
    return req

setup(
    name="mlops_train_O1",
    version='0.0.1',
    author='BSNDAN',
    author_email='dan.busnach@gmail.com'
    packages=find_packages(),
    include_requires=get_req('requirements.txt')
)
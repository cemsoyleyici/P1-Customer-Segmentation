from setuptools import find_packages, setup

HYPEN_E_DOT = "-e."
def get_requirements(filename:str)->list:
    """Read the requirements file and return the list of requirements

    Args:
        filename (str): name of the requirements file

    Returns:
        list: list of requirements as string
    """
    with open(filename, 'r') as f:
        requirements = f.read().splitlines()
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
        return requirements

__version__ = "0.1.0"

REPO_NAME = "P1-Customer-Segmentation"
SRC_REPO = "Customer_Segmentation"
AUTHOR_USER_NAME = "cemsoyleyici"
AUTHOR_EMAIL = "soyleyicicem@gmail.com"

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A package for customer segmentation",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}".format(AUTHOR_USER_NAME=AUTHOR_USER_NAME, REPO_NAME=REPO_NAME),
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    
)
from setuptools import find_packages, setup


def get_requirements() -> list[str]:

    requirements_list = []


    return requirements_list

setup(

    name = "Disease_Detection",
    version = "0.0.1",
    author = "Aditya",
    author_email = "adityajain1175@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
    
)
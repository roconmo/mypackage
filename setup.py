from setuptools import setup, find_packages
from pathlib import Path
from typing import List

def get_install_requires() -> List[str]:
    """Returns requirements.txt parsed to a list"""
    fname = Path(__file__).parent / 'requirements.txt'
    targets = []
    if fname.exists():
        with open(fname, 'r') as f:
            targets = f.read().splitlines()
    return targets

if __name__ == '__main__':

    VERSION = '1.0.0' 
    DESCRIPTION = 'license'
    LONG_DESCRIPTION = 'Data Reference for Data Analysis'

    project = "dr4da_package"

    setup(
        name=project, 
        python_requires='==3.9.13',
        version=VERSION,
        author="equipo_enel",
        author_email="<equipo@email.com>",
        description=DESCRIPTION,
        url='https://github.com/roconmo/mypackage',
        install_requires=get_install_requires(),
    )

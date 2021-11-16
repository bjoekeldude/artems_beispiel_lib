from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Artems-Loesungs-Lib'
LONG_DESCRIPTION = 'Libary mit Funktionen die Artems Problem loesen.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="avhelper", 
        version=VERSION,
        author="Stephan Bökelmann",
        author_email="sb@gruppe.ai",
        scripts=[],
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], 
        url="",
        
        keywords=['python', 'debugging'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: POSIX",
        ]
)

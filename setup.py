from setuptools import setup
from setuptools import find_namespace_packages

# code referenced from : https://github.com/areed1192/sigma-coding

# Load the README file.
with open(file="README.md", mode="r") as readme_handle:
    long_description = readme_handle.read()

setup(
    

    # Define the library name, this is what is used along with `pip install`.
    name='group18',

    # Define the author of the repository.
    author='group18 ',

    # Define the Author's email, so people know who to reach out to.
    author_email='palashjhamb7@gmail.com',

    # Define the version of this library.
    # Read this as
    #   - MAJOR VERSION 0
    #   - MINOR VERSION 1
    #   - MAINTENANCE VERSION 0
    version='0.1.0',

    # Here is a small description of the library
    description='A python solution that is being built as part of SE course.',

    # Long description but that will just be README
    long_description=long_description,

    # This will specify that the long description is MARKDOWN.
    long_description_content_type="text/markdown",

    # URL for source code
    url='https://github.com/niharncsu/group18-HW1',

    # These are the dependencies the library needs in order to run.
    install_requires=[
 	'pytest==7.1.2',
	'testpath==0.5.0'
    ],


    # Specifying the python version necessary to run this library.
    python_requires='>=3.6',

    # Additional classifiers that give some characteristics about the solution
    classifiers=[

        # I can say what phase of development my library is in.
        'Development Status :: 3 - Alpha',

        # Here I'll add the audience this library is intended for.
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
       

        # License that guides the library.
        'License :: Apache2.0',

        # Language that package was written in English.
        'Natural Language :: English',

        # operating system that this solution can use
        'Operating System :: OS Independent',

        # The version of Python that it uses.
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',

        # Here are the topics that the solution covers
        'Topic :: Software Development',
        'Topic :: Transportation'

    ]
)
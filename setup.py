
"""
To pack the dependancies for the user

Requirements : 
          1) pip install wheel

USAGE::
      python setup.py bdist_wheel

"""
# setup.py daily sdist bdist_egg

from setuptools import setup, find_packages

#if you wish to installl all the requirements along or else you can skip the below 
with open(requirements.txt) as f:
    reqrmnt=f.read()

requirements=reqrmnt.split('')

setup(
    name="HelloWorld",
    version="0.1",
    packages=find_packages(),
    # zip_safe=True,
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=requirements, ##['docutils>=0.3','paramiko','pywin32','colour'],#requirements
    # extras_require={
    #     'PDF':  ["ReportLab>=1.2", "RXP"],
    #     'reST': ["docutils>=0.3"],
    # }
    # entry_points={
    #     'console_scripts': [
    #         'snek = snek:main',
    #     ],
    # }

    author="Me",
    author_email="me@example.com",
    description="This is an Example Package",
    keywords="hello world example examples",

   
)

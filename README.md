# Python-pip-installable-package-using-setuptools
## Creating a python pip installable package using setuptools

It is very useful by creating your module/package and distribute across internet so that the developer only have to do "pip install modulename"
and the module will be installed in the environment.

The code has been uploaded for creating your pip installable python package.
### Creating whl file for
1) use this command to install wheel in your system "pip install wheel", if you are installing it in linux environment make sure to upgrade pip first and then try.
2) keep the above mentioned setup.py file outside of your packages(make sure you have __init__ files for every module) and run the command in the terminal "python setup.py bdist_wheel" to create pip installable package.

### Instaling in the system
After the above pip command it will generate a .whl file which is the main file. Just distribute it and run the .whl file using "pip install modulename.whl" and your module is ready to use in your python code.

import modulename and it will work


### Types of file you can create using setuptool:

Basically we can create two types of file using setuptools
    1) .tar.gz file (Traball file)
    2) .whl file
    
So question is which one is better for installation? here is the answer below
    
  a) Python needs a package format that is easier to install than sdist. Python's sdist packages are defined by and require the distutils and setuptools build systems, running arbitrary code to build-and-install, and re-compile, code just so it can be installed into a new virtualenv. This system of conflating build-install is slow, hard to maintain, and hinders innovation in both build systems and installers.

  b) Wheel attempts to remedy these problems by providing a simpler interface between the build system and the installer. The wheel binary package format frees installers from having to know about the build system, saves time by amortizing compile time over many installations, and removes the need to install a build system in the target environment
  
So the winner is .whl file ofcourse
#### Advantages of .whl file:
• Faster installation for pure python and native C extension packages.

• Avoids arbitrary code execution for installation. (Avoids setup.py)

• Installation of a C extension does not require a compiler on Windows or OS X.

• Allows better caching for testing and continuous integration.

• Creates .pyc files as part of installation to ensure they match the python interpreter used.

• More consistent installs across platforms and machines.


You can do much more, to know more about just go for this below link:
    https://setuptools.readthedocs.io/en/latest/setuptools.html#id4
    
 """
 """

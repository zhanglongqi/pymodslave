#Usage : python setup*.py py2exe --includes sip

from distutils.core import setup
import py2exe

setup(
    # The first three parameters are not required, if at least a
    # 'version' is given, then a versioninfo resource is built from
    # them and added to the executables.
    version = "0.3.6",
    description = "pyModSlave stand alone exe",
    name = "pyModSlaveQt",

    # targets to build
    windows= ["pyModSlaveQt.py"],
    )

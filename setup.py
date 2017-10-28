#!/usr/bin/env python3

from setuptools import setup

setup(  name             = "lxc-ps",
        version          = "0.2.6",
        scripts          = [ "lxc-ps" ],
        install_requires = [ "psutil" ],
        author           = "Jens John",
        author_email     = "jjohn@2ion.de",
        description      = "An implementation of lxc-ps(1) for LXC 1.x and 2.x against liblxc",
        license          = "GPL3",
        keywords         = "lxc lxc-ps ps",
        url              = "https://github.com/2ion/lxc-ps",
        classifiers      = [
                "Development Status :: 5 - Production/Stable",
                "Operating System :: POSIX :: Linux",
                "Environment :: Console",
                "Topic :: System :: Systems Administration",
                "Programming Language :: Python :: 3 :: Only",
                "Programming Language :: Python :: 3.4",
                "Programming Language :: Python :: 3.5",
                "Programming Language :: Python :: 3.6",
        ]
)

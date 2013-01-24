import os
import sys
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyblinkm",
    version = "0.1.0",
    author = "Thomas Sileo",
    author_email = "thomas.sileo@gmail.com",
    description = "Drive a BlinkM with Python via I2C using python-smbus on Raspberry Pi.",
    license = "MIT",
    keywords = "blinkm led i2c smbus rpi raspberry",
    url = "https://github.com/tsileo/pyblinkm",
    py_modules=['pyblinkm'],
    long_description= read('README.rst'),
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Communications",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    scripts=["pyblinkm.py"],
    zip_safe=False,
)
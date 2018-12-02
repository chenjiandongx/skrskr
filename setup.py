from setuptools import setup

NAME = "skr"
VERSION = "0.1.0"
URL = "https://github.com/chenjiandongx/skrskr"
AUTHOR = "chenjiandongx"
AUTHOR_EMAIL = "chenjiandongx@qq.com"
LICENSE = "MIT"
REQUIRES = ["pywin32"]
MODULES = ["skr"]
DESC = "SkrSkr in Python."

setup(
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    name=NAME,
    version=VERSION,
    license=LICENSE,
    install_requires=REQUIRES,
    url=URL,
    py_modules=MODULES,
    description=DESC,
    entry_points={"console_scripts": ["skr=skr:main"]},
)

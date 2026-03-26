from setuptools import setup, find_packages
from io import open


def read(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


setup(
    name="mongoforge",
    version="1.1.0",
    description="Magic filters for MongoDB",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Fsoky",
    author_email="cyberuest0x12@gmail.com",
    url="https://github.com/Fsoky/mongoforge",
    keywords="mongodb pymongo utils",
    packages=find_packages()
)
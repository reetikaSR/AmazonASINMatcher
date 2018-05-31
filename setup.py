from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='AmazonASINMatcher',
    version='1.1',
    description='A project to get the product details on Amazon',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='reetikaS',
    packages=['AmazonASINMatcher'],
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License"]
)

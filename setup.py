import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), "README.md")).read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="cookbook3",
    url="https://github.com/gregwa1953/CookbookV3/",
    version="3.0.0",
    author="Greg Walters",
    author_email="r+thedesignatedgeek@gmail.com",
    description="Python package, Cookbook program",
    keywords="python recipes scraper cookbook recipes tkinter ttk",
    scripts=['cookbook3.py'],
    long_description=README,
    install_requires=[
        "recipe_scrapers>=5.6.0",
        "requests>=2.19.1",
        "Pillow>=6.1.0",
        "tkcolorpicker>=2.1.3",
    ],
    packages=find_packages(),
    package_data={"": ["LICENSE"]},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        'Topic :: Internet :: WWW/HTTP',
    ],
    python_requires='>=3.7'
)

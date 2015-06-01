from setuptools import setup, find_packages

setup(
    name="Texas Holdem Poker",
    description="Solution to challenge 216 on https://reddit.com/r/dailyprogrammer",
    url="https://github.com/systemovich/dailyprogrammer/216_texasholdem",
    author="Geoffey van Wyk",
    version="0.1.0",
    keywords="dailyprogrammer python reddit",
    packages=find_packages(),
    entry_points={'console_scripts': ['texasholdem = games:main']},
)

from setuptools import setup, find_packages

from nospy.version import VERSION

setup(
    name='nospy',
    version=VERSION,
    description='A command-line utility for nostr',
    author='Micah Fullerton',
    author_email='plebeiusgaragicus@gmail.com',
    url='https://github.com/PlebeiusGaragicus/nospy',
    packages=find_packages(),
    install_requires=[
        # List your app's dependencies here
        'docopt',
        'bitcoin',
        'bech32',
        'nostr',
    ],
    classifiers=[
        # Choose classifiers from https://pypi.org/classifiers/
        # TODO:
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        'console_scripts': [
            'nospy=nospy:main',
        ],
    },
)

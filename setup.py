from setuptools import setup, find_packages

setup(
    name='PyMask',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'pymask=PyMask.cli:main',
        ],
    },
)


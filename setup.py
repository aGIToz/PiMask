from setuptools import setup, find_packages

setup(
    name='pimask',
    version='0.7',
    description='Dead simple image annotation tool to create binary mask via command line',
    author='Amitoz Azad',
    url='https://github.com/aGIToz/PiMask',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'pimask=pimask.cli:main',
        ],
    },
)


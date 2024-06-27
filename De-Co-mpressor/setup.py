from setuptools import setup

setup(
    name='compression-engine',
    version='0.1',
    description='A simple Compression Engine using Python and Tkinter',
    author='Sabelo Remember Ndlovu',
    author_email='sabelo.ndlovu@umuzi.org',
    packages=['compression_engine'],
    install_requires=[
        'tk',
    ],
    entry_points={
        'console_scripts': [
            'compression-engine=compression_engine.app:main',
        ],
    },
)

from setuptools import setup

setup(
    name='text-to-speech-converter',
    version='0.1',
    description='A simple Text to Speech converter using Python and Tkinter',
    author='Sabelo Remember Ndlovu',
    author_email='sabelo.ndlovu@umuzi.org',
    packages=['tts_converter'],
    install_requires=[
        'gtts',
        'tk',
    ],
    entry_points={
        'console_scripts': [
            'text-to-speech-converter=tts_converter.app:main',
        ],
    },
)



from setuptools import setup, find_packages

setup(
    name="videodownloader",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pytube",
        "moviepy"
    ],
    entry_points={
        'console_scripts': [
            'videodownloader=demo:main',  # Adjust if you have a main function
        ],
    },
    author="Sabelo Remember Ndlovu",
    author_email="sabelo.ndlovu@umuzi.org",
    description="A simple YouTube video downloader",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/SRSuccesTemusaNdlovu/Persinal_projects.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
from setuptools import setup

setup(
    name='qr-code-generator',
    version='0.1',
    description='A simple QR Code Generator using Python and Tkinter',
    author='Sabelo Remember Ndlovu',
    author_email='sabelo.ndlovu@umuzi.org',
    packages=['qr_code_generator'],
    install_requires=[
        'pyqrcode',
        'Pillow',
        'tk',
    ],
    entry_points={
        'console_scripts': [
            'qr-code-generator=qr_code_generator.app:main',
        ],
    },
)

from setuptools import setup

setup(
    name='detectify',
    version='0.1',
    description='A simple flask app that analyzes uploaded photos and provides precise bounding boxes around detected objects',
    author='Tarek Zaarour',
    author_email='tarek.zaarour@dell.com',
    packages=['detectify'],
    zip_safe=False
)
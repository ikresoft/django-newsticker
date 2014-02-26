import os.path
from setuptools import setup, find_packages

setup(
    name='django-newsticker',
    version='1.0',
    description='Django jquerynewsticker integration.',
    long_description=open('README.md', 'r').read(),
    author='Enver Bisevac',
    author_email='ikresoft@gmail.com',
    url='https://github.com/ikresoft/django-newsticker',
    packages=find_packages(),
    install_requires=[
        'Django',
    ],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 1",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)

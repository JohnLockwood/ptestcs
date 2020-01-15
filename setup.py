from setuptools import setup, find_packages

setup(
    name='ptestcs',
    version='0.2',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.md').read(),
    install_requires=['requests'],
    url='https://github.com/JohnLockwood/python-package-test',
    author='John Lockwood',
    author_email='john@codesolid.com'
)
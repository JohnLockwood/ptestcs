from setuptools import setup, find_packages

setup(
    name='python-package-test-codesolid',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='An example python package',
    long_description=open('README.md').read(),
    install_requires=['requests'],
    url='https://github.com/JohnLockwood/python-package-test',
    author='John Lockwood',
    author_email='john@codesolid.com'
)
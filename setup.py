from setuptools import setup, find_packages

setup(
    name='ptestcs',
    version='0.2',
    packages=['ptestcs'],
    license='MIT',
    description='An example python package',
    long_description=open('README.md').read(),
    install_requires=['requests'],
    url='https://github.com/JohnLockwood/ptestcs',
    author='John Lockwood',
    author_email='john@codesolid.com',
    package_dir={'ptestcs': 'ptestcs'}
)
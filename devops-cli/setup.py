from setuptools import setup, find_packages

setup(
    name='devops-cli',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'paramiko',
    ],
    entry_points='''
        [console_scripts]
        devops-cli=devops_cli:cli
    ''',
)
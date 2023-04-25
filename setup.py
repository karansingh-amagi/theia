from setuptools import setup, find_packages

setup(
    name='theia',
    version='0.1.0',
    description='A thin wrapper around Pulumi',
    author='Karan Singh',
    author_email='karan.singh@amagi.com',
    packages=find_packages(include=['theia', 'theia.*']),
    install_requires=[
        "arpeggio==2.0.0",
        "attrs==23.1.0",
        "dill==0.3.6",
        "grpcio==1.51.3",
        "parver==0.4",
        "protobuf==4.22.3",
        "pulumi==3.64.0",
        "pulumi-aws==5.37.0",
        "pulumi-gcp==6.54.0",
        "pyyaml==6.0",
        "semver==2.13.0",
        "six==1.16.0",
    ],
    setup_requires=['flake8'],
)

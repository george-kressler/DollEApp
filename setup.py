from setuptools import setup, find_packages

with open('README.md') as _f:
    _README_MD = _f.read()

_VERSION = '0.1'

setup(
    name='DollEApp',
    version=_VERSION,
    description='An app that allows a user to create images with a prompt.',
    long_description=_README_MD,
    classifiers=[
        # TODO: typing.
        "Typing :: Typed"
    ],
    url='https://github.com/george-kressler/DollEApp.git',
    download_url='https://github.com/.../.../tarball/{}'.format(_VERSION),  # TODO.
    author='George A. Kressler', 
    author_email='georgekressler@gmail.com',
    packages=find_packages(include=['project*']),  # TODO.
    test_suite="testing",
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
    install_requires=["neuraxle"],
    include_package_data=True,
    license='TODO',  # TODO: set your license string. 
    keywords='empty project TODO keywords'
)


from setuptools import setup, find_packages

with open('README.md') as _f:
    _README_MD = _f.read()

_VERSION = '0.1'

setup(
    name='DollEApp',
    version=_VERSION,
    description='An app that allows a user to create images with a prompt using OpenAI’s DALL-E.',
    long_description=_README_MD,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Graphics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    url='https://github.com/george-kressler/George-Kressler-Basic-Doll-E-API-Integration-Application.git',
    author='George A. Kressler',
    author_email='georgekressler@gmail.com',
    packages=find_packages(),
    install_requires=[
        'openai',
        'requests',
        'Pillow',
        'ttkthemes',
    ],
    python_requires='>=3.6',
    test_suite="tests",
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
    include_package_data=True,
    license='C00', 
    keywords='DALL-E, OpenAI, image generation, Tkinter GUI'
)
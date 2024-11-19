from setuptools import setup, find_packages

setup(
    name='pybandiger',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
        'pandas',
    ],
    author='Lansari Fedi',
    author_email='lansarifedi7@gmail.com',
    description='A data wrangling library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/LansariFedi/PyBandiger',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
from setuptools import setup, find_packages
import os


def read_file(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


def upload_to_pypi():
    os.system("twine upload dist/*")


setup(
    name='decoripy',
    version="0.0.1",
    author='Gioele Crispo',
    author_email='crispogioele@gmail.com',
    package_dir={'decoripy': 'decoripy'},
    packages=find_packages('.'),
    # scripts=['bin/script1', 'bin/script2'],
    url='https://github.com/gioelecrispo/decoripy.git',
    license='MIT',
    license_file='LICENSE',
    platform='any',
    description='Annotipy helps you making better decorators.',
    long_description=read_file('README.md'),
    install_requires=read_file('requirements.txt').splitlines(),
    python_requires='>=3',
    package_data={
        # '': ['package_data.dat'],
    },
    classifiers=[
        #   3 - Alpha; 4 - Beta; 5 - Production/Stable
        "Development Status :: 5 - Stable"
        "Intended Audience :: Developers"
        "License :: OSI Approved :: MIT License"
        "Operating System :: OS Independent"
        "Programming Language :: Python"
        "Programming Language :: Python :: 3"
        "Programming Language :: Python :: 3.1"
        "Programming Language :: Python :: 3.2"
        "Programming Language :: Python :: 3.3"
        "Programming Language :: Python :: 3.4"
        "Programming Language :: Python :: 3.5"
        "Programming Language :: Python :: 3.6"
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)

upload_to_pypi()


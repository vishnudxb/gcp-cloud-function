import os
import versioneer

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='func-example',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Google Cloud Function Example Repo.',
    long_description=read('README.md'),
    author='Vishnu Nair',
    author_email='me@vishnudxb.me',
    url='https://github.com/vishnudxb/gcp-cloud-function',
    packages=find_packages(exclude=['tests.*', 'tests', 'docs']),
    python_requires='>=3.6.*',
    include_package_data=True,
    zip_safe=True,
)

from distutils.core import setup

# Extract version number from resync/_version.py. Here we are very strict
# about the format of the version string as an extra sanity check.
# (thanks for comments in 
# http://stackoverflow.com/questions/458550/standard-way-to-embed-version-into-python-package )
import re
VERSIONFILE="i3f/_version.py"
verfilestr = open(VERSIONFILE, "rt").read()
match = re.search(r"^__version__ = '(\d\.\d.\d+(\.\d+)?)'", verfilestr, re.MULTILINE)
if match:
    version = match.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE))

setup(
    name='i3f',
    version=version,
    author='Simeon Warner',
    author_email='simeon.warner@cornel.edu',
    packages=['i3f'],
    scripts=[],
    classifiers=["Development Status :: 3 - Alpha",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: GPLv3",
                 "Operating System :: OS Independent", #is this true? know Linux & OS X ok
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 2.6",
                 "Programming Language :: Python :: 2.7",
                 "Topic :: Internet :: WWW/HTTP",
                 "Topic :: Software Development :: Libraries :: Python Modules",
                 "Environment :: Web Environment"],
    url='https://github.com/zimeon/i3f',
    license='LICENSE.txt',
    description='IIIF Image API library',
    long_description=open('README').read(),
)

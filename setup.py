from distutils.core import setup

setup(
    name='cwsync',
    version='0.1.0',
    author='M. H. Kiedrowski',
    author_email='hank@clockwork.net',
    platforms = ["Mac OS X"],
    packages=['autosync'],
    scripts=['bin/cwsync/cwsync'],
    url='http://clockwork.net/',
    license='LICENSE.txt',
    description='Keep a local directory synchronized with a remote directory',
    long_description=open('README.txt').read(),
    install_requires=[
        'pyobjc>=2.5.1',
    ]
)
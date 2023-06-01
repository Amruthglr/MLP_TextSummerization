import setuptools


__version__ = '0.0.0'

REPO_NAME = 'NLP_TextSummerization'
AUTOR_USER_NAME = 'AMRUTHGL'
SRC_REPO = 'textsummerizer'
AUTHOR_EMAIL = 'amruthglr@gmail.com'


setuptools.setup(
    name=SRC_REPO,
    version= __version__,
    author= AUTOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    package_dir= {"":"src"},
    packages = setuptools.find_packages(where='src')
)

from setuptools import setup, find_packages

try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "A Python package for creating a movie recommender system."

AUTHOR_NAME = 'Geetansh Nandraj'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='nandarajgeetansh@gmail.com',
    description='A python package used for creating a movie recommender system',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(where="src"),  # Automatically find packages in the `src` directory
    package_dir={"": "src"},  # Tell setuptools that packages are under `src`
    python_requires='>=3.11',
    install_requires=LIST_OF_REQUIREMENTS,
)
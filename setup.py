import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Personal Blog",
    version="0.0.1",
    author="Russell Schoen <Rusty7600@gmail.com>",
    description="A personal blog",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/r-schoen/flask_blog",
    packages=setuptools.find_packages(),
    python_requires=">=3.7"
)
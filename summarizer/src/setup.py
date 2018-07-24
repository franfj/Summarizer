import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="text_summarizer",
    version="0.0.4",
    author="Francisco Javier Rodrigo Gines",
    author_email="franjrg94@gmail.com",
    description="A text summarization package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/franfj/Summarizer",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "Development Status :: 4 - Beta  ",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)  ",
        "Operating System :: OS Independent",
    ),
)

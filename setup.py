from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="indpy-core",
    version="0.1.1",
    author="Harsh Gupta",
    author_email="harsh2125gupta@gmail.com",
    description="A comprehensive library for Indian Identity and Financial data validation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/harshgupta2125/Indpy",
    project_urls={
        "Bug Tracker": "https://github.com/harshgupta2125/Indpy/issues",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'indpy=indpy.cli:main',
        ],
    },
)

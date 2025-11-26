from setuptools import setup, find_packages

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="indpy",
    version="0.1.0",
    author="Harsh Gupta",
    author_email="harsh@example.com",  # Update this
    description="A comprehensive library for Indian Identity and Financial data validation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/indpy",
    project_urls={
        "Bug Tracker": "https://github.com/YOUR_USERNAME/indpy/issues",
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
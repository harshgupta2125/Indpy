from setuptools import setup, find_packages

setup(
    name="indpy",
    version="0.1.0",
    author="Harsh Gupta",
    description="Professional validation for Indian documents.",
    packages=find_packages(),
    
    # --- THIS IS THE NEW PART ---
    entry_points={
        'console_scripts': [
            'indpy=indpy.cli:main',
        ],
    },
    # ----------------------------
    
    python_requires='>=3.6',
)
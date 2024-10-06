from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name='mwwlean_email_scraper',
    description="A Python tool that extracts public email addresses from websites.",
    author='mwwlean',
    version='0.7',
    packages=find_packages(),
    install_requires=[
        'requests',     # Add requests as a dependency
        'pyfiglet',
    ],
    entry_points={
        "console_scripts":[
            "email_scraper = mwwlean_email_scraper:main",
        ],
    },
    long_description=description,
    long_description_content_type="text/markdown",
)

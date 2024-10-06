from setuptools import setup, find_packages

setup(
    name='mwwlean_email_scraper',
    author='Jan Leander',
    license="MIT",
    version='0.4',
    packages=find_packages(),
    install_requires=[
        'requests',     # Add requests as a dependency
        'pyfiglet',
    ],
    entry_points={
        "console_scripts":[
            "email_scraper = mwwlean_email_scraper:main",
        ],
    }
)
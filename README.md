![](assets/long_banner.png)

# Email Scraper

**Email Scraper** is a Python tool that extracts public email addresses from websites and saves them to a file for easy access. It is designed for developers and security researchers to quickly retrieve email data from a specified website.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)

## Features

- Extract public email addresses from any given website.
- Save extracted emails to a timestamped text file.
- Command-line interface for ease of use.

## Installation

### Using `pip`

1. Install the package from PyPI:

    ```bash
    pip install mwwlean-email-scraper
    ```

2. Verify the installation:

    ```bash
    email_scraper -h
    ```

   This should show you the help options if the installation was successful.

## Usage

### Command-Line Interface

Once installed, you can use the `email_scraper` command to extract emails from a website.

1. Extract emails from a website:

    ```bash
    email_scraper http://example.com
    ```

2. You can also run it in interactive mode:

    ```bash
    email_scraper
    ```

   It will prompt you to enter a URL, and you can type `exit` to quit.

### Help

To see all available commands and options:

```bash
email_scraper -h
```

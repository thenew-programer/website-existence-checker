# Website Existence Checker 

This project provides a Python script that reads a list of URLs from a CSV file, checks the existence of each website using HTTP HEAD requests, and writes the results to two separate files: one for working sites and another for non-working sites.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
    - [Using the Executable](#using-the-executable)
    - [Running from Source](#running-from-source)
3. [Usage](#usage)
4. [Dependencies](#dependencies)

## Features

- Reads a list of URLs from a CSV file.
- Checks the existence of each website using HTTP HEAD requests.
- Handles request exceptions gracefully.
- Outputs color-coded status updates to the console.
- Writes results to `working.txt` and `nworking.txt`.

## Installation

### Using the Executable

1. Download the executable file for your operating system from the [Releases](https://github.com/thenew-programer/website-existence-checker/releases) page.
2. Run the executable file:
    - On Windows: Double-click `website-existence-checker.exe`.
    - On macOS/Linux: Open a terminal and run `./website-existence-checker`.

### Running from Source

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/website-existence-checker.git
    cd website-existence-checker
    ```

2. Set up a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the script:
    ```bash
    python site_tester.py
    ```

## Usage

1. Prepare a CSV file containing the list of URLs you want to test.
2. Run the script and provide the filename when prompted.
3. The script will output the status of each URL and save the results in `working.txt` and `nworking.txt`.

- Example:
    ```bash
    Enter the name of the file: websites.csv
    https://example.com - status: 200 OK
    https://nonexistentwebsite.com - status: 400 FAIL
    ```
## Dependencies
The script requires the following Python packages:

- `requests`
- `csv`
- `time`
These dependencies are listed in the requirements.txt file.

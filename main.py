"""
Website Existence Checker Script
Copyright 2024 - Youssef Bouryal <youssefbouryal02@gmail.com>

This script reads a list of URLs from a CSV file, checks the existence of each website using HTTP HEAD requests,
and writes the results to two separate files: one for working sites and another for non-working sites.

Usage:
1. Place the list of URLs in a CSV file.
2. Run the script and provide the filename when prompted.
3. The script will output the status of each URL and save the results in 'working.txt' and 'nworking.txt'.

The script includes:
- File path validation to ensure the input file exists.
- URL preparation to format the URLs correctly.
- Error handling for request exceptions.
- Color-coded output for easy readability of the status.

"""
import os
import csv
import time
import requests
from requests.exceptions import RequestException


class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'


def get_filepath() -> str:
    """
    Prompt the user to enter the file path and validate its existence.

    Returns:
        str: Valid file path.
    """
    while True:
        file_path = input("Enter the name of the file: ")
        if os.path.isfile(file_path):
            return file_path
        else:
            print(f"{bcolors.FAIL}File: {file_path} doesn't exist")


def prepare_urls(file_path: str) -> list:
    """
    Read URLs from the CSV file and format them properly.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: List of formatted URLs.
    """
    urls = []
    with open(file_path, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')

        for row in csv_reader:
            tmp = str(row).replace("'", "").replace("]", "").replace("[", "")
            urls.append(f"https://{tmp}")

    return urls


def test_websites(urls: list) -> None:
    """
    Test the existence of websites and categorize them into working and non-working sites.

    Args:
        urls (list): List of URLs to be tested.
    """
    working_sites = []
    nworking_sites = []
    for url in urls:
        try:
            res = requests.head(url, timeout=10)
            if res.status_code >= 400:
                raise RequestException
            working_sites.append(url)
            print(f"{bcolors.OKGREEN}{url} - status: {res.status_code} OK")
        except RequestException:
            nworking_sites.append(url)
            print(f"{bcolors.FAIL}{url} - status: {res.status_code} FAIL")

        time.sleep(1)
    write_to_file("working.txt", working_sites)
    write_to_file("nworking.txt", nworking_sites)


def write_to_file(filename: str, urls: list) -> None:
    """
    Write the list of URLs to a file.

    Args:
        filename (str): Name of the file to write to.
        urls (list): List of URLs to be written.
    """
    with open(filename, 'w+') as f:
        for url in urls:
            f.write(url + '\n')


if __name__ == "__main__":
    file_path = get_filepath()
    urls = prepare_urls(file_path)
    test_websites(urls)

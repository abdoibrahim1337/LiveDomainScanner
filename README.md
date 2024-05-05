# LiveDomainScanner

## Introduction
LiveDomainScanner is a lightweight tool designed to quickly check the availability of web domains. It assists pentesters, security professionals, and web developers in efficiently assessing the live status of multiple domains, thereby saving time and effort during security assessments and testing.

## Features
- **Domain Availability Check:** LiveDomainScanner checks the availability of domains by sending HTTP requests to ports 80 and 443.
- **Threaded Execution:** The tool utilizes threading to perform domain checks concurrently, enhancing efficiency.
- **Output Logging:** LiveDomainScanner logs the live domains to a file named "live_domains.txt".

## Installation
No installation is required for LiveDomainScanner. Simply download or clone the repository and execute the Python script.

## Usage
```bash
python LiveDomainScanner.py [file_path]
Replace [file_path] with the path to the text file containing the list of domain names to check.
Requirements

    Python 3.x
    Requests library (install via pip install requests)

Example

Suppose you have a file named domains.txt containing a list of domains to check. To run LiveDomainScanner, execute the following command:
python LiveDomainScanner.py domains.txt
Output

The tool will print the live status of each domain to the console and log the live domains to a file named live_domains.txt.

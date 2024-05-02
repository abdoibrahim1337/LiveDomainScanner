import sys
import requests
import threading

def read_domain_list(file_path):
    """
    Reads a list of domain names from a text file.
    Args:
    - file_path (str): Path to the text file containing domain names.
    Returns:
    - List of domain names.
    """
    with open(file_path, 'r') as file:
        domain_list = [line.strip() for line in file.readlines()]
    return domain_list

def sanitize_url(url):
    """
    Removes 'http://' or 'https://' prefixes from a URL.
    Args:
    - url (str): URL to sanitize.
    Returns:
    - Sanitized URL without 'http://' or 'https://' prefixes.
    """
    if url.startswith('http://'):
        return url[len('http://'):]
    elif url.startswith('https://'):
        return url[len('https://'):]
    else:
        return url  # If no prefix is found, return the original URL unchanged

def check_domain_availability(domain):
    """
    Checks if a domain is live by sending HTTP requests to ports 80 and 443.

    Args:
    - domain (str): Domain name to check.

    Returns:
    - Boolean indicating whether the domain is live or not.
    """
    try:
        domain = sanitize_url(domain)
        # Send HTTP request to port 80 (HTTP)
        http_response = requests.get(f"http://{domain}")

        # Send HTTP request to port 443 (HTTPS)
        https_response = requests.get(f"https://{domain}")

        # Check if either request was successful (status code 2xx)
        if http_response.status_code == 200 or https_response.status_code == 200:
            return True
    except requests.RequestException:
        # Handle connection errors or timeouts
        pass
    return False

def check_domains_threaded(domain_list):
    """
    Checks domain availability using threads.

    Args:
    - domain_list (list): List of domain names to check.

    Returns:
    - List of tuples containing domain name and availability status.
    """
    results = []
    threads = []
    for domain in domain_list:
        thread = threading.Thread(target=lambda: results.append((domain, check_domain_availability(domain))))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    return results

def main():
    filename = sys.argv[1]  # Change index to 1 to get the filename from command line arguments
    domain_list = read_domain_list(filename)
    results = check_domains_threaded(domain_list)
    for domain, availability in results:
        if availability:
            print(f"{domain} is live")
            with open('live_domains.txt','a') as file:
                file.write(f"{domain}\n")
        else:
            print(f"{domain} is not live")

if __name__ == "__main__":
    main()

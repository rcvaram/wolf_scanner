import re
import urllib.parse as urlparse

import requests


def request(url):
    try:
        return requests.get( "https://" + url )
    except requests.exceptions.ConnectionError:
        pass


def find_domains(target_url):
    domain_contents = {}
    with open( "subdomain.txt", "r" ) as wordlist_file:
        for line in wordlist_file:
            url = line.strip() + target_url
            response = request( url )
            if response:
                domain_contents[url] = response
    return domain_contents


def discover_directory(target_url):
    files = {}
    with open( "common.txt", "r" ) as wordlist_file:
        for line in wordlist_file:
            url = target_url + "/" + line.strip()
            response = request( url )
            if response:
                files[url] = response
    return files


links = []
url = "https://rcvaram.pythonanywhere.com/"

def extract_links_from(url):
    response = requests.get( url )
    href_links = re.findall( '(?:href=")(.*?)"',response.content.decode() )
    for link in href_links:
        link = urlparse.urljoin( url, link )
        if "#" in link:
            link = link.split( "#" )[0]
        if url in link and link not in links:
            links.append( link )
            print(link)
            extract_links_from( link )

extract_links_from(url)
print(len(links))
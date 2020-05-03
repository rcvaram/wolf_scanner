import re
import urllib.parse as urlparse

import requests
from bs4 import BeautifulSoup


class Scanner:
  def __init__(self, url, ignore_links):
    self.session = requests.Session()
    self.target_url = url
    self.target_links = []
    self.links_to_ignore = ignore_links

  def extract_links_from(self, url):
    response = self.session.get(url)
    html_value = response.content.decode()
    links1 = re.findall('(?:href=)(.*?)>', html_value)
    links2 = re.findall('(?:href=")(.*?)"', html_value)
    for link in links1:
      link = re.sub('[\',\"]', '', link)
      links2.append(link)
    return links2

  def crawl(self, url=None):
    if url == None:
      url = self.target_url
    href_links = self.extract_links_from(url)
    try:
      for link in href_links:
        link = urlparse.urljoin(url, link.strip())
        if "#" in link:
          link = link.split("#")[0]
        if self.target_url in link and link not in self.target_links and link not in self.links_to_ignore:
          self.target_links.append(link)
          if len(self.target_links) < 10:
            print(link)
            self.crawl(link)
    except Exception as e:
      print(e)

  def extract_forms(self, url):
    res = self.session.get(url)
    parsed_html = BeautifulSoup(res.content.decode())
    forms_list = parsed_html.findAll("form")
    return forms_list

  def submit_form(self, form, value, url):
    action = form.get('action')
    post_url = urlparse.urljoin(url, action)
    post_data = {}
    input_list = form.findAll("input")
    method = form.get("method")
    for input in input_list:
      input_name = input.get("name")
      input_type = input.get("type")
      input_value = input.get("value")
      if input_type == "text":
        input_value = value
      post_data[input_name] = input_value
    if method == "post":
      return self.session.post(post_url, data=post_data)
    return self.session.get(post_url, params=post_data)

  def test_xss_in_form(self, form, url):
    xss_test_script = "<sCript>alert(\"test\")</scriPt>"
    response = self.submit_form(form, xss_test_script, url)
    return xss_test_script in response.content.decode()

  def test_xss_in_url(self, link):
    xss_test_script = "<sCript>alert(\"test\")</scriPt>"
    link = link.replace("=", "=" + xss_test_script)
    response = self.session.get(link)
    return xss_test_script in response.content.decode()

  def run(self):
    self.crawl()
    for target_link in self.target_links:
      forms = self.extract_forms(target_link)
      for form in forms:
        print("form testing : --> {}".format(target_link))
        if self.test_xss_in_form(form, target_link):
          print("Found vulanerable in  form --> {}".format(target_link))
      if "=" in target_link:
        print("testing link --> {}".format(target_link))
        if self.test_xss_in_url(target_link):
          print("Found vulenrable in URL parameters --> {}".format(target_link))

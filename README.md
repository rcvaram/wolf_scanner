# The Website Scanner --> Find Vulnerabilities in websites

<img src="https://github.com/rcvaram/website_scanner/blob/master/agence-olloweb-d9ILr-dbEdg-unsplash-scaled.jpg" height="64"/>

[![Build Status](https://travis-ci.org/zold-io/zold.svg?branch=master)](https://travis-ci.org/zold-io/zold)


First, you install following python packages using pip:

```
$ pip install requests
```

```
$ pip install beautifulsoup4

```
Then, you run it and follow the instructions:

```
$ python generic_scanner.py -t  target_web_address

```

When you give the target web address as t argument, this script scan all the pages of the website and listout the vulnerabilites that found.
Initally, I've implemented to find the XSS vulnerability only. So This script will list out the places where the XSS vulnerability is exist 
 
Example  -->  Searchbox of the particular website.
 
Go to this video to watch how it works.....
https://www.youtube.com/watch?v=HqHi_Q3FwUw


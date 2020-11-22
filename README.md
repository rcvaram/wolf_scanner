# The WOLF Scanner --> To Find Vulnerabilities in websites


<img src="https://github.com/rcvaram/website_scanner/blob/master/agence-olloweb-d9ILr-dbEdg-unsplash-scaled.jpg" height="64"/>




1. *You install following python packages using **pip**:*

```
$ pip install requests
```

```
$ pip install beautifulsoup4
```




2. *Clone the **wolf_scanner** github reposistory*

```
$ git clone https://github.com/rcvaram/wolf_scanner.git
```



3. *Then, you run **wolf_scanner.py** and follow the instructions:*

```
$ python wolf_scanner.py -t  target_web_address
```





When you give the target web address as t argument, this script scan all the pages of the website and listout the vulnerabilites that found.
Initally, I've implemented to find the **XSS vulnerability** only. So This script will list out the places where the XSS vulnerability is exist 
  

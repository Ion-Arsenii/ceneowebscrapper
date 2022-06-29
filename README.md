# CeneoScraperAI

## Single opinion structure on [Ceneo.pl](https://www.ceneo.pl/)

|Element|Selector|Variable|Data type|
|-------|--------|--------|---------|
|Opinion|div.js_product-review|opinion|bs4.element.Tag|
|Opinion id|\["data-entry-id"\]|opinion_id|str|
|Author|span.user-post__author-name|author|str|
|Recommendation|span.user-post__author-recomendation > em|rcmd|bool|
|Stars score|span.user-post__score-count|score|float|
|Content|div.user-post__text|content|str|
|List of adventages|div.review-feature__title--positives  ~ div.review-feature__item|pros|str|
|List of disadventages|div.review-feature__title--negatives  ~ div.review-feature__item|cons|str|
|Date of posting opinion|span.user-post__published > time:nth-child(1)\["datetime"\]|posted_on|str|
|Date of purchasing product|span.user-post__published > time:nth-child(2)\["datetime"\]|bought_on|str|
|For how many users useful|button.vote-yes > span|useful_for|int|
|For how many users useless|button.vote-no > span|useless_for|int|

## Stages of project

1) Extraction of elements for a single opinion to separate variables
2) Extraction of elements for a single opinion to one complex variable (dictionary)
3) Extraction of all opinions form single page to list of dictionaries
4) Extraction of all opinions for certain product and saving it to .json file
5) Code refactoring and optimization
    1) Definition of function for extracting single elements of page from HTML code
    2) Creation of dictionary that describes opinions' structure with selectors for particular opinion's elements
    3) Using dictionary comprehension to extract all opinion's elements on the basis of opinions' structure dictionary
6) Adjustment of data types for different opinions' elements
7) Translation of certain opinion's elements into English 
8) Analysis of extracted opinions
    1) Basic statistics
        1) Number of all opinions about the product
        2) Number of opinions with list of advantages
        3) Number of opinions with list of disadvantages
        4) Average score based on stars
    2) Plots
        1) Share of recommendations in total number of opinions
        2) Frequency histogram of stars


beautifulsoup4=(Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work.)
certifi=(Certifi provides Mozilla's carefully curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts. It has been extracted from the Requests project.)
chardet=(chardet is designed primarily for detecting the character encoding of webpages, I have found an example of it being used on individual text files.)
charset-normalizer=(A library that helps you read text from an unknown charset encoding)
click=(Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary)
colorama=( Colorama is one of the built-in Python modules to display the text in different colors. It is used to make the code more readable)
cycler=( Cycler library can be used to easily cycle over a single style)
Flask=(Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries)
fonttools=(FontTools is a library for manipulating fonts, written in Python. The project includes the TTX tool, that can convert TrueType and OpenType fonts to and from an XML text format, which is also called TTX.)
googletrans=(Googletrans is a free and unlimited python library that implemented Google Translate API. This uses the Google Translate Ajax API to make calls to such methods as detect and translate.)
h11=(h11's goal is to be a simple, robust, complete, and non-hacky implementation of the first “chapter” of the HTTP/1.1 spec: RFC 7230: HTTP/1.1 Message Syntax and Routing)
h2=(H2 is an open-source lightweight Java database. It can be embedded in Java applications or run in the client-server mode)
hpack=( its used to compress HTTP headers in HTTP/2)
hstspreload=(Chromium HSTS Preload list as a Python package. The package provides a single function: in_hsts_preload() which takes an IDNA-encoded host and returns either True or False regarding whether that host should be only accessed via HTTPS)
httpcore=(The HTTP Core package provides a minimal low-level HTTP client, which does one thing only. Sending HTTP requests)
httpx=(HTTPX is a fully featured HTTP client for Python 3, which provides sync and async APIs, and support for both HTTP/1.1 and HTTP/2.)
hyperframe=(This library contains the HTTP/2 framing code used in the hyper project. It provides a pure-Python codebase that is capable of decoding a binary stream into HTTP/2 frames.)
idna=(Support for the Internationalised Domain Names in Applications (IDNA) protocol as specified in RFC 5891. This is the latest version of the protocol and is sometimes referred to as “IDNA 2008”).
importlib-metadata= is a library that provides for access to installed package metadata. Built in part on Python’s import system, this library intends to replace similar functionality in the entry point API and metadata API of pkg_resources. Along with importlib resources in Python 3.7 and newer (backported as importlib_resources for older versions of Python), this can eliminate the need to use the older and less efficient pkg_resources package.
itsdangerous=(When you get the data back you can ensure that nobody tampered with it. The receiver can see the data, but they can not modify it unless they also have your key.)
Jinja2=(Jinja is a fast, expressive, extensible templating engine. Special placeholders in the template allow writing code similar to Python syntax. Then the template is passed data to render the final document)
kiwisolver=(Kiwi is an efficient C++ implementation of the Cassowary constraint solving algorithm.)
libretranslatepy=(Kiwi is an efficient C++ implementation of the Cassowary constraint solving algorithm.)
lxml=(lxml is a Python library which allows for easy handling of XML and HTML files, and can also be used for web scraping)
MarkupSafe=(MarkupSafe implements a text object that escapes characters so it is safe to use in HTML and XML. Characters that have special meanings are replaced so that they display as the actual characters.)
matplotlib=(Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible.)
numpy=(NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices)
packaging=(Reusable core utilities for various Python Packaging interoperability specifications)
pandas=pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,built on top of the Python programming language.
Pillow=Pillow is the friendly PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors.
pyparsing=(The pyparsing module is an alternative approach to creating and executing simple grammars, vs. the traditional lex/yacc approach, or the use of regular expressions.)
python-dateutil=(The dateutil module provides powerful extensions to the standard datetime module, available in Python.)
pytz=(Pytz brings the Olson tz database into Python and thus supports almost all time zones)
requests=(Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data)
rfc3986=(A Python implementation of RFC 3986 including validation and authority parsing)
six=Six is a Python 2 and 3 compatibility library. It provides utility functions for smoothing over the differences between the Python versions with the goal of writing Python code that is compatible on both Python versions. See the documentation for more information on what is provided
sniffio=(This is a tiny package whose only purpose is to let you detect which async library your code is running under)
soupsieve=(Soup Sieve is a CSS selector library designed to be used with Beautiful Soup 4. It aims to provide selecting, matching, and filtering using modern CSS selectors.)
urllib3=(The urllib3 module is a powerful, sanity-friendly HTTP client for Python. It supports thread safety, connection pooling, client-side SSL/TLS verification, file uploads with multipart encoding, helpers for retrying requests and dealing with HTTP redirects, gzip and deflate encoding, and proxy for HTTP and SOCKS)
Werkzeug=Werkzeug is a collection of libraries that can be used to create a WSGI (Web Server Gateway Interface) compatible web application in Python
zipp=(A pathlib-compatible Zipfile object wrapper. Official backport of the standard library Path object)
# Lab: Information disclosure on debug page

>This lab contains a debug page that discloses sensitive information about the application. To solve the lab, obtain and submit the SECRET_KEY environment variable.

### Observations
Again, there are limited areas where we can supply input. I crawled the web application and found php info at `GET /cgi-bin/phpinfo.php`

From here we can see that the application is running `PHP Version 7.2.24-0ubuntu0.18.04.10`

### Solution
Initially I went the route of googling "php 7.2 debug page" in the hopes that there is a default path to view debug information. Turns out that all I had to do was view the page source and search for `SECRET_KEY`. Much easier than expected, the secret key was `3f3c5pkhdb5y0i0ad7cvy8g6vui3o2pb`

Lab solved!
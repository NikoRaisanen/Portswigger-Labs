# Lab: File path traversal, traversal sequences stripped with superfluous URL-decode

>This lab contains a file path traversal vulnerability in the display of product images.

>The application blocks input containing path traversal sequences. It then performs a URL-decode of the input before using it.

>To solve the lab, retrieve the contents of the /etc/passwd file.

### Solution
Right click the image of any product and open in a new tab

Notice that this path has a `filename` param, we can get the etc/passwd from here

This part of the description points towards url encoding 

`The application blocks input containing path traversal sequences. It then performs a URL-decode of the input before using it.`

First I tried url encoding the traversal sequences only once: `%2e%2e%2f%2e%2e%2f%2e%2e%2fetc/passwd` and had no success

I url encoded the traversal sequences and got access to `etc/passwd` with the following request

`GET /image?filename=%252e%252e%252f%252e%252e%252f%252e%252e%252fetc/passwd`

Lab solved!
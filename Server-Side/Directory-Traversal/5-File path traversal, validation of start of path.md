# Lab: File path traversal, validation of start of path

>This lab contains a file path traversal vulnerability in the display of product images.

>The application transmits the full file path via a request parameter, and validates that the supplied path starts with the expected folder.

>To solve the lab, retrieve the contents of the /etc/passwd file.

### Solution
Right click the image of any product and open in a new tab

Notice that this path has a `filename` param, we can get the etc/passwd from here

Very simple, got `etc/passwd` file with this request:

`GET /image?filename=/var/www/images/../../../etc/passwd`

We can leave the initial part of the param that is checked, and then traverse down

Lab solved!
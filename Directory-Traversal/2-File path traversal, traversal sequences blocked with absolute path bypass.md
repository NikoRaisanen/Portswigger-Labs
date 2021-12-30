# Lab: File path traversal, traversal sequences blocked with absolute path bypass

>This lab contains a file path traversal vulnerability in the display of product images.

>The application blocks traversal sequences but treats the supplied filename as being relative to a default working directory.

>To solve the lab, retrieve the contents of the /etc/passwd file.

### Solution
Right click the image of any product and open in a new tab

Notice that this path has a `filename` param, we can get the etc/passwd file with this absolute path payload `/image?filename=/etc/passwd`... This was easy because the description says that we should use an absolute path

Lab Solved!
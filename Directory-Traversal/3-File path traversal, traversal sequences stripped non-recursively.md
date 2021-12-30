# Lab: File path traversal, traversal sequences stripped non-recursively

>This lab contains a file path traversal vulnerability in the display of product images.

>The application strips path traversal sequences from the user-supplied filename before using it.

>To solve the lab, retrieve the contents of the /etc/passwd file.

### Solution
Right click the image of any product and open in a new tab

Notice that this path has a `filename` param, we can get the etc/passwd file with this path payload `GET /image?filename=....//....//....//etc/passwd `

The idea is that the stripping function will remove the `../` pattern. If you have `....//` then this function will remove only the characters from index 2 through index 4 (3 characters). After this strip we are still left with `../`! Recursive stripping would invalidate this attack

Lab Solved!
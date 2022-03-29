# Lab: File path traversal, validation of file extension with null byte bypass

>This lab contains a file path traversal vulnerability in the display of product images.

>The application validates that the supplied filename ends with the expected file extension.

>To solve the lab, retrieve the contents of the /etc/passwd file.

### Solution
Right click the image of any product and open in a new tab

Notice that this path has a `filename` param, we can get the etc/passwd from here

The title implies that we need to use a null byte to bypass the file extension check... I did exactly that and got the passwd file with `GET /image?filename=../../../etc/passwd%00.jpg `

The extension checking function is happy because of the `.jpg`, but the null byte ensures that the jpg extension does not get passed to the server

Lab solved!

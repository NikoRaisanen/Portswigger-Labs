# Lab: OS command injection, simple case

>This lab contains an OS command injection vulnerability in the product stock checker.

>The application executes a shell command containing user-supplied product and store IDs, and returns the raw output from the command in its response.

>To solve the lab, execute the whoami command to determine the name of the current user.

### Vulnerable area
The product stock is displayed after a request to `POST /product/stock`, which contains the body `productId=1&storeId=1`

### Exploit
In the above mentioned request I sent this body `productId=1&storeId=1;whoami` using a `;` command separator to get the hostname `peter-E765ol`

Lab solved!
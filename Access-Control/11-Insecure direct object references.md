# Lab: Insecure direct object references

>This lab stores user chat logs directly on the server's file system, and retrieves them using static URLs.

>Solve the lab by finding the password for the user carlos, and logging into their account.

### Observations
Immediately I notice a new page that was not previously present, `/chat`.
There is an option to download the transcript for our conversation, which makes this request `GET /download-transcript/2.txt`

### Solution
Since this lab is about IDOR, I attempted `GET /download-transcript/1.txt` and found chat logs that say :

`You: Ok so my password is ex4xlhijdxe5cv7flftu. Is that right?`

I successfully logged into `carlos` with the mentioned password. You could modify the number at the end of the request to potentially find additional logs, in this case `1` was just the most logical number to check

Lab solved!


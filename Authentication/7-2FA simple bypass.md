# Lab: 2FA simple bypass

>This lab's two-factor authentication can be bypassed. You have already obtained a valid username and password, but do not have access to the user's 2FA verification code. To solve the lab, access Carlos's account page.

>Your credentials: wiener:peter

>Victim's credentials carlos:montoya

### Log in to both accounts and observe different behavior
- Nothing notable before getting MFA code
- When MFA code is entered, the following request was sent:

`POST /login2 HTTP/1.1

Host: acf11f681ec7b4aec03784c2002200d7.web-security-academy.net

Cookie: session=Vlhrt5dXR1gB3ATPonYiuRo7aEjenTog

Content-Length: 13

Cache-Control: max-age=0

Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="96"

Sec-Ch-Ua-Mobile: ?0

Sec-Ch-Ua-Platform: "macOS"

Upgrade-Insecure-Requests: 1

Origin: https://acf11f681ec7b4aec03784c2002200d7.web-security-academy.net

Content-Type: application/x-www-form-urlencoded

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9

Sec-Fetch-Site: same-origin

Sec-Fetch-Mode: navigate

Sec-Fetch-User: ?1

Sec-Fetch-Dest: document

Referer: https://acf11f681ec7b4aec03784c2002200d7.web-security-academy.net/login2

Accept-Encoding: gzip, deflate

Accept-Language: en-US,en;q=0.9

Connection: close

mfa-code=1347`

### Notes
The MFA verification is done in `/login2`

The login flow looks like: 

/login -> /login2 -> /my-account

What if we capture the request for `/login2` (MFA)?

We can modify the request and set the path to `/my-account`, effectively bypassing mfa verification and solving the lab!
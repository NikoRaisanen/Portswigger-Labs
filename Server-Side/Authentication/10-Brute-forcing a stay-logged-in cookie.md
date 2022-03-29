# Lab: Brute-forcing a stay-logged-in cookie

>This lab allows users to stay logged in even after they close their browser session. The cookie used to provide this functionality is vulnerable to brute-forcing.

>To solve the lab, brute-force Carlos's cookie to gain access to his "My account" page.

>Your credentials: wiener:peter

>Victim's username: carlos

### Cookie
Logged in as `wiener` and selected "stay logged in" option. `GET /my-account` contains the following cookie header: `Cookie: stay-logged-in=d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw; session=6s3Qh5N90fD7hQy9KIKITAq5597q35mV`

The stay-logged-in value would take way too long to brute force. Through some trial and error I discovered that it is base64 encoded. The fact that brute forcing the value directly is impossible is why I looked into b64.

### Base64
Decoding `d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw` yields `wiener:51dc30ddc473d43a6011e9ebba6ca770`

Looks like `username:<HASH>`... This is an MD5 hash, can be confirmed because the resulting MD5 hash of `peter` is `51dc30ddc473d43a6011e9ebba6ca770`

### Methodology
So all we have to do is set the `stay-logged-in` value to: `b64_encode('carlos':MD5(password))`

where we iterate over `password` with the provided password list. I used Burp Intruder "payload" processing to perform the above transformations with a "sniper" attack on the `stay-logged-in` parameter

^ The above didn't return anything interesting... I then made a login attempt to `carlos` and put his `sessionid` in my intruder attack. Open a 302 request in your browser and the lab is solved!




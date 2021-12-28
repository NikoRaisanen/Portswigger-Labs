# Lab: Username enumeration via response timing

 >This lab is vulnerable to username enumeration using its response times. To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.

>Your credentials: wiener:peter



Testing response times with certain passwords:

`wiener:peter` = 360ms

`wiener:abcdef` = 410ms

`wiener:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA` = 1850ms

Got rate-limited after a few requests, the lab hint says to use `X-Forwarded-For` header to bypass this. I added the following request header and change the IP every few requests `X-Forwarded-For: 0.0.0.0`

The fact that this lab gave us account credentials is why I tried testing different passwords and analyzing response times... So far it looks like longer password = longer response time

I tried using that long password for a few made up usernames and got average response times of ~400ms... *Response time is longer if the username is valid AND password is long*

Use intruder to iterate over username paylods, setting the password to always be the long string of A's

Set the following payloads:

`X-Forwarded-For: 0.0.0.X` and `username=X&password=<STRING_OF_A>`

0-255 for X-Forwarded header, usernames list for username

Execute the intruder automation with the "pitchfork" attack, each request will be sent from a new IP (at least the website will think so) so you don't get blocked.

Username `app01` had an outlier response time of 1700ms, this is the username... now to enumerate password


Perform another clusterbomb attack against password list, while still incrementing the value of `X-Forwarded-For`

Password payload `1234` is the only payload with a 302 status code...
Our login is `app01:1234`

Lab solved!



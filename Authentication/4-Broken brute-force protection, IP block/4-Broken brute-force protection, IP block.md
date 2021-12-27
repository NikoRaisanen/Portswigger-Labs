# Lab: Broken brute-force protection, IP block

>This lab is vulnerable due to a logic flaw in its password brute-force protection. To solve the lab, brute-force the victim's password, then log in and access their account page.

>Your credentials: wiener:peter

>Victim's username: carlos



We were given a set of credentials, I assume we use `wiener:peter` to learn how to bypass the ip block, then brute force the password for carlos...

### Bypassing IP block
After 3 failed login attempts, IP block takes effect

- Tried changing referer http header, no success
- Discovered that I can infintely switch between logging in as `wiener:peter` (valid creds) and `wiener:123` (invalid creds)... *Looks like a successful login resets the IP block request count*

### Methodology
We need to successfully log in as `wiener` after every 2 login attempts to avoid the ip block. So our automated attack will look like:

`<carlos:bruteforce> <carlos:bruteforce> <wiener:peter> <carlos:bruteforce> <carlos:bruteforce> <wiener:peter> <carlos:bruteforce> <carlos:bruteforce> <wiener:peter> etc etc`

where each `<>` represents a POST request to the login page

### The Attack
At the time of writing, I am not aware of how to automatically execute the above attack with Burp. So I created a python script to add `peter` to the password list after every 2 requests. I then created another list for usernames, so that it maps onto the password list -- See `4-script.py`, `newPW.txt`, and `newUSER.txt` for more info.

I can then use the Burp Intruder pitchfork attack to insert the payloads of both lists in parallel to create a username + password combo

### IMPORTANT
*Make sure to run the attack on a single thread so that the order of the username / password payloads is preserved!*

Lab solved!

The request for `carlos:iloveyou` returned a 302 status code, successful login
# Lab: Password brute-force via password change

>This lab's password change functionality makes it vulnerable to brute-force attacks. To solve the lab, use the list of candidate passwords to brute-force Carlos's account and access his "My account" page.

>Your credentials: wiener:peter

>Victim's username: carlos

### Step 1
At first I tried brute forcing the password straight on the login page, but I got rate limited

On this lab you can change the password on your `my-account` page... We can perform the bruteforcing there

### The Request
Change password for `wiener` and we get the following in the request body: `username=wiener&current-password=peter&new-password-1=notpeter&new-password-2=notpeter`

Send to intruder and replace `username` with carlos, iterate over passwords for `current-password` param, and define a new password

I tried the above with this payload and just recieved a bunch of identical 302 responses: `username=carlos&current-password=§pw§&new-password-1=123&new-password-2=123`

### Understanding the process
Entering 2 different values for the new password confirmation, this text is displayed `New passwords do not match`

Tried another intruder attack with the following body: `username=carlos&current-password=§pw§new-password-1=123&new-password-2=1234`

The payload `computer` has a unique response length, this is probably because we got the error message that we identified earlier

`carlos:computer` produced a successful login, lab solved!
# Lab: Username enumeration via account lock

>This lab is vulnerable to username enumeration. It uses account locking, but this contains a logic flaw. To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.

### Account Lock
Tried spamming the login page requests for `bob` and `carlos`. No account locking occured

#### Perhaps acc lock occurs only for valid users?
Created clusterbomb attack with usernames list as payload #1 (username), and numbers 1-4 as payload #2 (password)

Result:

Only username `root` got locked out after the 4th failed login attempt... We can conclude that this is the username that we will attack!

### Bypassing lockout when bruteforcing password
- Tried logging in as `carlos` between `root` login attempts, did not reset the bruteforce protection
- Completely modified User-Agent, no success
- Modifying session cookie still gets me blocked, no success
- Tried modifying a bunch of other headers... No success

### Solution
Ran the password list against `root` anyways with intruder...

Password payload `cheese` gave a unique response length

After lockout, I logged in as `root:cheese` and solved the lab!
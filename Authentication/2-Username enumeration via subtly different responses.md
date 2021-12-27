# Lab: Username enumeration via subtly different responses

 This lab is subtly vulnerable to username enumeration and password brute-force attacks. It has an account with a predictable username and password, which can be found in the following wordlists:

    Candidate usernames
    Candidate passwords

>To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page. 

Entered some test data into the username and password fields, they are displayed here in the request:

`username=tuser&password=tpass`

Send the entire request to intruder, and iterate over usernames list. I looked at a few requests and saw that in the case of an invalid username, it says `Invalid username or password.` I added a simple string search for this text and the string was not found in 1 username payload, `app`

Now we go to intruder and set username=`app` and iterate over the password list

Payload `1111` is the only one that does not match a string search for `valid`

So the login info is:

Username: `app`

Password: `1111`

Lab solved!
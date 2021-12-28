# Lab: Username enumeration via different responses
 >This lab is vulnerable to username enumeration and password brute-force attacks. It has an account with a predictable username and password, which can be found in the following wordlists:


>To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page. 

Entered some test data into the username and password fields, they are displayed here in the request:

`username=tuser&password=tpass`

Send the entire request to intruder, and iterate over usernames list. The response length for the payload `att` was unique, this response said `incorrect password` instead of `incorrect username`. The webapp disclosed too much info and we now know that the username is `att`

Now we go to intruder and set username=`att` and iterate over the password list

Payload `robert` had a unique response length

So the login info is:

Username: `att`

Password: `robert`

Lab solved!

# Lab: Password reset broken logic

>This lab's password reset functionality is vulnerable. To solve the lab, reset Carlos's password then log in and access his "My account" page.

>Your credentials: wiener:peter

>Victim's username: carlos

### Step 1
Went through the password reset process for `wiener`...

There is a POST request to `/forgot-password` where you set the new password. I sent this request to the repeater and changed the username parameter to `carlos` instead of `wiener`. This was the request body that allowed me to reset the password of carlos: `temp-forgot-password-token=8yvjHSOMUzEVUJoX2rL3oCuTe8hsziC3&username=carlos&new-password-1=newpw&new-password-2=newpw`

### Complete
Now I can log in with `carlos:newpw`, lab solved!
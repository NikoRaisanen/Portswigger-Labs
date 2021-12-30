# Lab: Weak isolation on dual-use endpoint

>This lab makes a flawed assumption about the user's privilege level based on their input. As a result, you can exploit the logic of its account management features to gain access to arbitrary users' accounts. To solve the lab, access the administrator account and delete Carlos.

>You can log in to your own account using the following credentials: wiener:peter

### Vulnerable area
`POST /my-account/change-password HTTP/1.1`

This is the page where email and password can be changed.

The original body looks something like
<pre>csrf=u3hJtTZ3yziQ41WMd9RhuvwcsFQD1zvn&username=wiener&current-password=peter&new-password-1=123&new-password-2=123</pre>

### Vulnerability
Change the `username` param to `administrator` and the page returns 

`Current password is incorrect

Your username is: administrator`

##### Interesting...
I removed the `current-password` param from the body and the password change went through... We can now log into `administrator` with our newly set password and delete the user `carlos`

Lab solved!
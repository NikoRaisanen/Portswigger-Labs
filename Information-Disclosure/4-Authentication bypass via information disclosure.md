# Lab: Authentication bypass via information disclosure

>This lab's administration interface has an authentication bypass vulnerability, but it is impractical to exploit without knowledge of a custom HTTP header used by the front-end.

>To solve the lab, obtain the header name then use it to bypass the lab's authentication. Access the admin interface and delete Carlos's account.

>You can log in to your own account using the following credentials: wiener:peter

### What we need
Looks like we need to find a custom HTTP header... I will try logging in with my credentials to see. I can't find this HTTP header by logging in as `wiener`.

Now I will try enumerating the web application and see if I can find any comments or logic that points towards this header

### Vulnerable area
Making a `GET /admin` request results in something like "only local users can access admin page." After some poking around I found that we can make a `TRACE /admin` request which yields `X-Custom-IP-Authorization: 68.0.174.101` in the response

### Solution
The error message specified "local users" and we saw the above header... So maybe if we set the custom header to localhost (127.0.0.1) we can access the admin panel...

Access `GET /admin` with `X-Custom-Ip-Authorization: 127.0.0.1` header and we can access the admin panel and delete carlos, lab solved!
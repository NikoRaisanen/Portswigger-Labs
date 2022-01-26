# Lab: Method-based access control can be circumvented

>This lab implements access controls based partly on the HTTP method of requests. You can familiarize yourself with the admin panel by logging in using the credentials administrator:admin.

>To solve the lab, log in using the credentials wiener:peter and exploit the flawed access controls to promote yourself to become an administrator.

### Observations
This endpoint is used to upgrade, downgrade permissions `POST /admin-roles`. The endpoints takes parameters like so `username=wiener&action=upgrade`

We are told that the vulnerability in this lab can be exploited with HTTP methods, so I did a google search for HTTP methods and found the following: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

### Solution
On the above page, I was looking for methods aside from POST that allow me to modify data. PUT satisfies this request, so I logged into my account `wiener` and sent a request to `PUT /admin-roles` with the following body: `username=wiener&action=upgrade`

Lab solved!

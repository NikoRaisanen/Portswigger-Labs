# Lab: Referer-based access control

>This lab controls access to certain admin functionality based on the Referer header. You can familiarize yourself with the admin panel by logging in using the credentials administrator:admin.

>To solve the lab, log in using the credentials wiener:peter and exploit the flawed access controls to promote yourself to become an administrator.

### Observations
I logged in as `administrator` and upgraded the perms for user carlos. The upgrade occured with this request `GET /admin-roles?username=carlos&action=upgrade`

Notice that the `Referer` header is set to `/admin`. We are told in the lab title and description that the vulnerability is in the referer header

### Solution
Send this request to repeater `GET /admin-roles?username=carlos&action=upgrade` and change username to `wiener`.

Log in as `wiener` and copy the session cookie, paste this cookie into the request that we just sent to repeater. This gives us admin permissions for the user `wiener`

Lab solved!
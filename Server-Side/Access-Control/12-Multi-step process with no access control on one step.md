# Lab: Multi-step process with no access control on one step

>This lab has an admin panel with a flawed multi-step process for changing a user's role. You can familiarize yourself with the admin panel by logging in using the credentials administrator:admin.

>To solve the lab, log in using the credentials wiener:peter and exploit the flawed access controls to promote yourself to become an administrator.

### Understanding the steps
1. Login at `POST /login`
2. Initial click on upgrade button `POST /admin-roles` with similar params: `username=carlos&action=upgrade`
3. "Are you sure" button click `POST /admin-roles` with similar params: `action=upgrade&confirmed=true&username=carlos`

### Vulnerable step
After some poking around, I determined that the vulnerable step in the flow was `POST /admin-roles` with the action, confirmed, and username parameters

Log in as the administrator user and send the request in step #3 to repeater... I first tried changing the username parameter to `wiener` but that gave me an authorization error

### Solution
Log into a seperate tab as user `wiener` and save the session cookie. Insert this session cookie into the request that you just sent to repeater. This will execute the permissions upgrade for the mentioned user in the context of the session cookie (wiener)

Lab solved!
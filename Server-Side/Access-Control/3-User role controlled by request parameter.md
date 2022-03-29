# Lab: User role controlled by request parameter

>This lab has an admin panel at /admin, which identifies administrators using a forgeable cookie.

>Solve the lab by accessing the admin panel and using it to delete the user carlos.

>You can log in to your own account using the following credentials: wiener:peter

### Observation
I logged in as `wiener` and made a request to `GET /admin` and found the following cookie... `Cookie: Admin=false;`

What happens if I change the value to `true`?

### Solution
I made a request to the admin panel, and then the "delete user" endpoint with the `Admin` parameter set to true and I was able to delete the `carlos` user account

Lab solved!
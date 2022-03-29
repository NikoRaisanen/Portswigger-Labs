# Lab: User role can be modified in user profile

>This lab has an admin panel at /admin. It's only accessible to logged-in users with a roleid of 2.

>Solve the lab by accessing the admin panel and using it to delete the user carlos.

>You can log in to your own account using the following credentials: wiener:peter

### Observations
The description of the lab points us towards the user profile page. The core functionality here seems to be the ability to change your email address.

The `GET /my-account/change-email` response contains the following request body:

`{"email":"niko@mail.com"}`

### Solution
If we can set the email for this account, can we also set the `roleid` for this account? I attempted to do so by the modifying the body as shown:

<pre>
{"email":"niko@mail.com",
"roleid": 2}
</pre>

This allowed me to access the admin panel and I deleted the account for `carlos`, lab solved!
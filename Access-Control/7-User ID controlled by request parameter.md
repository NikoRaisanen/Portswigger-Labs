# Lab: User ID controlled by request parameter

>This lab has a horizontal privilege escalation vulnerability on the user account page.

>To solve the lab, obtain the API key for the user carlos and submit it as the solution.

>You can log in to your own account using the following credentials: wiener:peter

### Observations
Upon logging in and refreshing the "My account" page, I can see that the request looks like `GET /my-account?id=wiener`

### Solution
Change the `id` parameter to `carlos` and we are able to access the "my account" page of carlos, lab solved!
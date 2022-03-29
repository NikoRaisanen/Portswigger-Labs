# Lab: User ID controlled by request parameter with data leakage in redirect

>This lab contains an access control vulnerability where sensitive information is leaked in the body of a redirect response.

>To solve the lab, obtain the API key for the user carlos and submit it as the solution.

>You can log in to your own account using the following credentials: wiener:peter

### Observations
I logged in as wiener and we can see that the url to access my account page is now `/my-account?id=wiener`

I changed the id parameter to `carlos` and observed the response

### Solution
The lab description said that the sensitive data is leaked in a redirect, so I checked the http response corresponding to my `GET /my-account?id=carlos` request.

The response contains this information, yielding the API key for carlos

<pre>
                   <div id=account-content>
                        <p>Your username is: carlos</p>
                        <div>Your API Key is: qTq5hy2fT7xTvGTbYZjkQsnWWXljKvgU</div>
</pre>

Lab solved!

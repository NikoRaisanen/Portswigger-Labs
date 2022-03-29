# Lab: Authentication bypass via encryption oracle
### WIP, COMING BACK TO THIS LAB LATER

>This lab contains a logic flaw that exposes an encryption oracle to users. To solve the lab, exploit this flaw to gain access to the admin panel and delete Carlos.

>You can log in to your own account using the following credentials: wiener:peter

### Observations
There is a "stay logged in" checkbox on the login page. Log in as `wiener` and on `GET /my-account` we can see the following cookies:

`Cookie: stay-logged-in=2U9ZY2Xzd2Bt4Sv4RMsk7M7a24tMILB2yiKT4jXJknI%3d; session=3fR0I47avjGjF6NSE2aHsUkwzTVpqN81`

I tried b64 decoding the `stay-logged-in` cookie because it ends in `=`, but it didn't yield anything

**I looked at the solution hint to find that the vulnerability occurs when you enter an invalid email address when creating a comment**

After entering an invalid address when commenting, here are the cookies in the request:
<pre>GET /post?postId=9 HTTP/1.1
Host: acb81f981e9cb79bc07b2f330039000b.web-security-academy.net
Cookie: notification=f4CrOoXNSHRpl5xdtbqcGAsiTZm8ztuL0OzANiHBHzo%3d; stay-logged-in=2U9ZY2Xzd2Bt4Sv4RMsk7M7a24tMILB2yiKT4jXJknI%3d; session=3fR0I47avjGjF6NSE2aHsUkwzTVpqN81</pre>

We also saw that this was reflected after the POST request to send a comment `Invalid email address: niko123`

### Piecing things together
The cookie is called `notification` and we saw some reflected text... Perhaps there is a connection?

We have a new cookie called `notification` that also ends in `=` (url decode `%3d`)... Base64 decoding this yields nothing either

Turns out that we can decrypt the cookies by passing them into the `notification` cookie in `GET/post?postId=9`

Passing my `stay-logged-in` value of `2U9ZY2Xzd2Bt4Sv4RMsk7M7a24tMILB2yiKT4jXJknI%3d` yields the plaintext `wiener:1641929587627` in the same area where we previously saw "Invalid email address"... The full sent cookie looks as follows:
<pre>
Cookie: notification=2U9ZY2Xzd2Bt4Sv4RMsk7M7a24tMILB2yiKT4jXJknI%3d; stay-logged-in=2U9ZY2Xzd2Bt4Sv4RMsk7M7a24tMILB2yiKT4jXJknI%3d; session=3fR0I47avjGjF6NSE2aHsUkwzTVpqN81
</pre>

### Impersonation
By now, it looks like we can try to craft a `stay-logged-in` cookie that would allow us to impersonate the `administrator` user... The format will be something like `administrator:<NUMBERS>`

How do we know what numbers to put after the colon?

From my time participating in CTFs I took a guess that it is epoch time, and I was correct. `1641929587627` in epoch time comes out to Jan 11 2022 19:33:07 GMT

### Crafting a response
The `notification` cookie gets set in `POST /post/comment` when the email address is invalid. So we can basically use the `email` body param to encrypt data, since the notification cookie gets reflected.

So I enter `administrator:1641929587627` into the email parameter and recieve the following cookie:

`Set-Cookie: notification=f4CrOoXNSHRpl5xdtbqcGAp8E6i8xH%2bDoMdj43b6UNWusvma1icA%2btSxDOXml%2b92gfj1Cw5jh%2bN8i8hYSma2gw%3d%3d;`

Inserting this cookie into the `notification` param of `GET /post?postId=9` yields the clear text:
`Invalid email address: administrator:1641929587627`

This shows that we can encrypt and decrypt

### Reverse engineering
Send the new notification cookie to burp decoder and first url decode it, and then base64 decode it. We know that it is likely base64 because it ends with `==`

We are left with the data that presumably generates the stay-logged-in cookie... But we just want `administrator:<NUMBERS>` instead of `Invalid email address: administrator:1641929587627`. If we remove the first 23 characters we will be left with only the desired part

From there, we use the POST comment functionality to 

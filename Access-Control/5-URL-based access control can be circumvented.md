# Lab: URL-based access control can be circumvented

>This website has an unauthenticated admin panel at /admin, but a front-end system has been configured to block external access to that path. However, the back-end application is built on a framework that supports the X-Original-URL header.

>To solve the lab, access the admin panel and delete the user carlos.

### Observations
The `X-Original-URL` header can be used to make it look like we are attempting to access the admin panel internally... I tried adding this to the `GET /admin` endpoint but it wouldn't load.

I instead tried to add the `X-Original-URL: /admin` header in my `GET /` request. This gave me the admin panel where I can delete the user carlos

So this means that I can access the admin page, but this doesn't let me delete users

### Solution
Looking at previous labs, deleting the `carlos` user occurs from the following request: `GET admin/delete?username=carlos`

To do this, we make a request to `GET /` (as before), but we pass the `username=carlos` parameter so we end up with a request to: `GET /?username=carlos`

We then set `X-Original-URL: /admin/delete`

With this method we make a request to `admin/delete`, but we also pass the `username=carlos` parameter to the delete endpoint

This will delete the user `carlos`, lab solved!
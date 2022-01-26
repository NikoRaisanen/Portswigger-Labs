# Lab: User ID controlled by request parameter, with unpredictable user IDs

>This lab has a horizontal privilege escalation vulnerability on the user account page, but identifies users with GUIDs.

>To solve the lab, find the GUID for carlos, then submit his API key as the solution.

>You can log in to your own account using the following credentials: wiener:peter

### Observations
I logged in as `wiener` and when accessing `GET /my-account` I can see that my unique identifier is `e93183c3-479f-41dc-8a1c-3a2cc8c5c8d9`

There is no way that I can brute force the GUID for carlos, this is impractical given the length of the identifier. So what if instead I can dig around the website and see if this GUID shows up somewhere else?

My first guess was to use a "reset password" functionality in the hopes that this would yield a GUID, but there is no such functionality in this lab

Where else can I search to find information about carlos?

### Solution
I clicked around a few blog posts to look for a post or comment created by carlos. Eventually I found a blog post created by carlos and clicked the hyperlink attached to his name, and I land on this endpoint `/blogs?userId=f02de152-2483-4bb2-98ac-2835030b69ea`

I presume that this is the GUID for carlos, so I browse to `/my-account?id=f02de152-2483-4bb2-98ac-2835030b69ea` and I can now see the API key for carlos

Lab solved!



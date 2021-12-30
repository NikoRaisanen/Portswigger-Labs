# Lab: Authentication bypass via flawed state machine

>This lab makes flawed assumptions about the sequence of events in the login process. To solve the lab, exploit this flaw to bypass the lab's authentication, access the admin interface, and delete Carlos.

>You can log in to your own account using the following credentials: wiener:peter

### Context
This is a new path that I have not seen before `GET /role-selector HTTP/1.1`

I tried intercepting it and changing my role to `admin`, but it forcefully gets changed back to 1 of the 2 options

### Solution
What happens if we skip `role-selector` and go straight to the `/admin` path? This allows me access to the admin dashboard and I can delete user `carlos`

Lab solved!
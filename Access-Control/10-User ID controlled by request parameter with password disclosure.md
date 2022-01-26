# Lab: User ID controlled by request parameter with password disclosure

>This lab has user account page that contains the current user's existing password, prefilled in a masked input.

>To solve the lab, retrieve the administrator's password, then use it to delete carlos.

>You can log in to your own account using the following credentials: wiener:peter

### Observations
I logged in as wiener and the `/my-account` page shows my masked password. We can unmask it by doing 'inspect element' and modifying the html... Here is the html that masks the password:

`<input required="" type="password" name="password" value="peter">`

We can unmask the password by changing the `type` parameter to `text` instead of `password` as follows:

`<input required="" type="text" name="password" value="peter">`

We can now see the password in plaintext

NOTE: You could also just look at the `value` parameter, but that's too easy :)


### Solution
So how can we now access the `/my-account` page for the administrator user to unmask their password?

Looks like this lab also uses the `id` parameter, so we can simply make a GET request to `/my-account?id=administrator`

Now I unmask the password with the method previously mentioned and can delete the user carlos

Lab solved!


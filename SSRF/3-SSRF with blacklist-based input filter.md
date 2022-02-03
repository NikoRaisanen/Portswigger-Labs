# Lab: SSRF with blacklist-based input filter

>This lab has a stock check feature which fetches data from an internal system.

>To solve the lab, change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos.

>The developer has deployed two weak anti-SSRF defenses that you will need to bypass.

### Observations
We can access the stockApi body parameter in the request to `POST /product/stock`

I noticed that the stockApi value needs to be url encoded or it will return "missing parameter" error

The Portswigger reading for SSRF states that these are different ways to represent localhost: `2130706433, 017700000001, or 127.1.`... Source: https://portswigger.net/web-security/ssrf


So I changed the `stockApi` parameter to `stockApi=http://127.1/admin`... Still nothing, I then decided to alternate capitals on the directory name as shown: `stockApi=http://127.1/aDmIn`, this gives us access to the admin dashboard!

### Solution
Now that we can access the dashboard, we can just call the delete endpoint against user `carlos` to delete his account. Modify stockApi to the following:

`stockApi=http://127.1/aDmIn/delete?username=carlos`

 Lab solved!
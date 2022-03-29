# Lab: SSRF with whitelist-based input filter

>This lab has a stock check feature which fetches data from an internal system.

>To solve the lab, change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos.

>The developer has deployed an anti-SSRF defense you will need to bypass.

### Observations
I tried manipulating the `stockApi` body param of the `POST /product/stock` request and got the following response: `"External stock check host must be stock.weliketoshop.net"`...
We know that there is some sort of url parsing that extracts the hostname and compares it to a whitelist

The burp reading for the SSRF section talks about including credentials in the url with the `@` symbol. I simply added my name before the default url and I still got a valid response from the api

`stockApi=http://niko@stock.weliketoshop.net:8080/product/stock/check?productId=1&storeId=1`

### Next steps
Because we can put credentials in the url, we now have another place where we can try to interject our own data (before the @ symbol)

How can we use this to exploit? There are things called `url fragments` that you can use to effectively "comment out" the rest of the url. Think of this like using `--` in sql injection to comment out the rest of the query. So what if we can modify the stockApi parameter as follows:

`stockApi=http://<WHATEVER_DOMAIN_I_WANT>#@stock.weliketoshop.net:8080/product/stock/check?productId=1&storeId=1`

The `#` symbol begins the url fragment, so everything after `@stock` would effectively be "commented out". We would still pass the whitelist filter because we are leaving the original url in tact

### Solution
You need to url encode the `#` symbol twice, and we can now solve the request by using the following stockApi value: `http://localhost%2523@stock.weliketoshop.net/admin/delete?username=carlos`
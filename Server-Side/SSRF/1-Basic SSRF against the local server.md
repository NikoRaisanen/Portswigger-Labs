# Lab: Basic SSRF against the local server

>This lab has a stock check feature which fetches data from an internal system.

>To solve the lab, change the stock check URL to access the admin interface at http://localhost/admin and delete the user carlos.

### Observations
I browsed to a product and clicked the "check stock" button. This sends a request to `POST /product/stock HTTP/1.1` with the body `stockApi=http%3A%2F%2Fstock.weliketoshop.net%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D1%26storeId%3D1`

I am able to access the admin panel by changing the stockApi value to `http://localhost/admin`

### Solution
I sent the above captured request and then tried to click the `delete` button for carlos. From this I learned that the delete endpoint is `GET /admin/delete?username=carlos`

Now I send the `POST /product/stock` request, but I modify the `stockApi` parameter so that it will issue a GET request to the admin delete endpoint like so:

`stockApi=http://localhost/admin/delete?username=carlos`

Upon sending of the request, the account for user carlos will be deleted, lab solved!
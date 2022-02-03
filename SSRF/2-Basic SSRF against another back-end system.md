# Lab: Basic SSRF against another back-end system'

>This lab has a stock check feature which fetches data from an internal system.

>To solve the lab, use the stock check functionality to scan the internal 192.168.0.X range for an admin interface on port 8080, then use it to delete the user carlos.

### Observations
We can see that a request to `POST /product/stock` has a body parameter of stockApi: `stockApi=http%3A%2F%2F192.168.0.1%3A8080%2Fproduct%2Fstock%2Fcheck%3FproductId%3D1%26storeId%3D1`

This stockApi parameter is what we will be using to complete this lab.

We know tha the admin page will be located at `/admin`

### Solution
Send the `POST /product/stock` request to intruder and set the body to `stockApi=http://192.168.0.§1§:8080/admin`... The `§` symbol means that we will insert a payload into that position. We insert all integers between 1 and 255 into the last octet of the IP address.

Looking at the results, we can see the only status code 200 occured at `192.168.0.84/admin`

The backend system to access the admin page is found at this internal IP address

From the previous lab we know that the endpoint to delete user carlos is `admin/delete?username=carlos`

So now we send the `POST /product/stock` request with the following body: `stockApi=http://192.168.0.84:8080/admin/delete?username=carlos`

Lab solved!
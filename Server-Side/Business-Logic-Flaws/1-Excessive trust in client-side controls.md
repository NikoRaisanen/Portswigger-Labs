# Lab: Excessive trust in client-side controls

>This lab doesn't adequately validate user input. You can exploit a logic flaw in its purchasing workflow to buy items for an unintended price. To solve the lab, buy a "Lightweight l33t leather jacket".

>You can log in to your own account using the following credentials: wiener:peter

### Vulnerable area
The vulnerable stage is the moment that you add the item to cart, NOT in the checkout screen

Vulnerable endpoint is: 
`POST /cart HTTP/1.1`


with body of `productId=1&redir=PRODUCT&quantity=1&price=133700`

### Solution
Change the `price` param to 99 and you can successfully check out the product!
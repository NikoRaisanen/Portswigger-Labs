# Lab: Insufficient workflow validation

>This lab makes flawed assumptions about the sequence of events in the purchasing workflow. To solve the lab, exploit this flaw to buy a "Lightweight l33t leather jacket".

>You can log in to your own account using the following credentials: wiener:peter


### Hints
The description points us to look at the purchasing workflow... First I tried to buy the jacket outright and looked at the captured requests, I didn't notice anything particularly interesting

Since this lab has to do with the purchasing workflow, could I get a "finished" purchase request for another product, and then use that to validate my purchase of the l33t jacket?

### Successful purchase
I successfully purchased another item for ~$5 and this was the request to see the completed purchase: `GET /cart/order-confirmation?order-confirmed=true `

### Exploit
I added the jacket to my checkout bucket, then I intercepted the request for the "purchase" button and made a get request to the afformentioned request instead. The purchase went through

Lab solved!
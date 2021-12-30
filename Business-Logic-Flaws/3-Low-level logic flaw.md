# Lab: Low-level logic flaw

>This lab doesn't adequately validate user input. You can exploit a logic flaw in its purchasing workflow to buy items for an unintended price. To solve the lab, buy a "Lightweight l33t leather jacket".

>You can log in to your own account using the following credentials: wiener:peter

### Beginning
Tried messing around with a bunch of stuff to no avail. I read the hint and realized that I need to use intruder, at that point I was convinced that the vulnerability is a buffer overflow

Found that the maximum increase in quantity per request was 99. So we need to run intruder until our total cost turns negative (because of integer overflow). 

Capture the `POST /cart` request and shoot it to intruder with the following body:

`productId=1&quantity=99&redir=CART`

Select `null payload` as payload type and run indefinitely

Keep refreshing until the total price is negative... Mine ended with the following info:
- Quantity of jackets = 18614
- Total price = -$18062754.96

### Solution
Now we just need to get this total price to be greater than 0, but less than 100 by adding other items to the cart

I decided with "furbabies" which cost $73.34 each. So I will need to add <pre>18062754.96 / 73.34</pre> furbabies

This value is `246288` furbabies, rounding up

We can use the same intruder method as before to add that number of furbabies

### Calculation
246288 furbabies needed, 99 added per intruder request:

`246288 / 99 = 2487.76` -- We need to run our intruder null payload 2487 times

After this, I will still need to add x furbabies (where x is less than 99 so we can do it in 1 request), so I will intercept the request and do that.

### WARNING
I accidentally incremented the # of jackets by 99 again so my final numbers are different from the explained above. The methodology still applies. My final figures were:

<pre>Name	Price	Quantity	
Lightweight "l33t" Leather Jacket	$1337.00	18713	
Fur Babies	$73.34	244484</pre>

Lab solved!
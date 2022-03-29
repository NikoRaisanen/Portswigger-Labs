# Flawed enforcement of business rules

>This lab has a logic flaw in its purchasing workflow. To solve the lab, exploit this flaw to buy a "Lightweight l33t leather jacket".

>You can log in to your own account using the following credentials: wiener:peter

### Observations
Immediately I notice something that I have not before. There is a green banner that says `New customers use code at checkout: NEWCUST5`

Maybe this flaw is in how the coupon is applied?\\

There is also an option to sign up for the newsletter at the bottom of the screen. Enter an email address and you get the following alert: `Use coupon SIGNUP30 at checkout!`

Cool, so now we have 2 coupons

### Business logic flaw
Applying the same coupon 2 times in a row is invalid and yields an error. Alternating between our 2 coupons allows us to apply discounts until our total cost reaches $0. This was discovered with a bit of trial and error.

Before discovering the `SIGNUP` coupon I tried to send the `POST` request to apply the `NEWCUST5` coupon a bunch of times, but that didn't work

Lab solved, just alternate the 2 coupons!
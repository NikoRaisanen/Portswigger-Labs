# Lab: Infinite money logic flaw

>This lab has a logic flaw in its purchasing workflow. To solve the lab, exploit this flaw to buy a "Lightweight l33t leather jacket".

>You can log in to your own account using the following credentials: wiener:peter

### Observations
- This lab contains access to an email client, and upon logging in I see the option to enter a gift card code. Looks like we can possibly claim an unlimited amount of gift cards?

- There is the option to subscribe to the newsletter. Sign up with your provided email address and you see the following: `Use coupon SIGNUP30 at checkout!`

- The newsletter option dissapears after this occurs...

- There is a product called `Gift Card` that costs $10... weird

### Methodology
I bought a gift card and this is the associated code: `A2YSwtctit`

I came to find out that we can use the `SIGNUP30` coupon every time that we check something out.

Purchasing a $10 gift card gives us $10 in store credit... If we use the `SIGNUP30` when purchasing, then we can keep converting a $7 giftcard purchase into $10 of store credit

### Automating
Doing the above manually would take far too long. Here are the requests needed to automate the workflow:

`POST /cart => POST cart/coupon => POST /cart/checkout => GET /card/order-confirmation?order-confirmed=true => POST /gift-card`

So we need to add gift card to the cart -> apply coupon -> checkout the cart (response contains code) -> redeem the card using the code

### Macro
Create a macro consisting of the 5 requests previously mentioned... Extract the gift card code from `GET /card/order-confirmation?order-confirmed=true` and pass it into the `gift-card` parameter for `POST /gift-card`

Make a GET request to any endpoint on the site and send it to the intruder. The macro will execute on every request. 

Remove all payload selectors and use `sniper` attack with the `null payloads` setting. You can keep generating until you have enough money to buy the leather jacket. I had to run this attack on a single thread for it to work


Once you have accumulated enough money, purchase the jacket and the lab is solved!
# Lab: Information disclosure in error messages

>This lab's verbose error messages reveal that it is using a vulnerable version of a third-party framework. To solve the lab, obtain and submit the version number of this framework.

### Initial impressions
My first guess would be to go fuzz the login and blog comments pages, but these pages do not exist in this particular lab

### Vulnerable Area
There were very few pages on this website where I could supply user input, but one of the obvious areas was in the url parameters. I cicked on a product and changed the `productId` param to a string instead of a number. I did this because this would be an unexpected user input

The request that got me the version number was `GET /product?productId=abc`

The resulting output states that the site is running on `Apache Struts 2 2.3.31`

Lab solved!
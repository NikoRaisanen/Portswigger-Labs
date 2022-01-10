# Lab: Authentication bypass via encryption oracle

>This lab contains a logic flaw that exposes an encryption oracle to users. To solve the lab, exploit this flaw to gain access to the admin panel and delete Carlos.

>You can log in to your own account using the following credentials: wiener:peter

### Observations
There is a "stay logged in" checkbox on the login page. Log in as `wiener` and on `GET /my-account` we can see the following cookies:

`Cookie: stay-logged-in=8cmy7HANaPFLdaidoYpNC2qijjC9yZpsN4Pqb2EvfFM%3d; session=v9vQxAXZUF6qqRenMjMbge58GSH1ur7f`


# Lab: Unprotected admin functionality

>This lab has an unprotected admin panel.

>Solve the lab by deleting the user carlos.

### Observations
I couldn't find the admin panel at `/admin` like usual, so I checked `/robots.txt`, which contains the following:

<pre>User-agent: *
Disallow: /administrator-panel</pre>

I then navigated to `https://ac741fff1ecb6181c0c431d3001100de.web-security-academy.net/administrator-panel` and the lab was solved!
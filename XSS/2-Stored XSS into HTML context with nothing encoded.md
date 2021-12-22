# Lab: Stored XSS into HTML context with nothing encoded

To solve this lab, submit a comment that calls the alert function when the blog post is viewed. 

Vulnerable area: comments section

Created stored xss with following payload in comments section:

`Hey<script>alert()</script>what is this?`

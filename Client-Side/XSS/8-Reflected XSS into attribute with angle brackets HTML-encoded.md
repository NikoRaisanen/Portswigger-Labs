# Lab: Reflected XSS into attribute with angle brackets HTML-encoded

>This lab contains a reflected cross-site scripting vulnerability in the search blog functionality where angle brackets are HTML-encoded. To solve this lab, perform a cross-site scripting attack that injects an attribute and calls the alert function. 

### First steps:
The vulnerability is in the search functionality. I entered a search for "Hello" and can see that my search term was reflected as so: "0 search results for 'Hello'"

This means that we could possibly trigger a reflected XSS attack by inserting malicious content into the `search` url parameter

### Next steps
Inserting the term `<script>alert()</script>` does not trigger xss. We just get the text reflected back to us.

I tried closing the `h1` tag and inserting a script tag after closing, but that didn't yield xss

### Solution
Instead of trying to close the h1 tag, I changed the approach to inject an attribute into the already existing h1 tag. I managed to trigger an alert by entering the following search term `"onmouseover="alert(1)`

This payload injected an attribute to the h1 element to trigger an alert when the mouse is hovering over this element, lab solved!
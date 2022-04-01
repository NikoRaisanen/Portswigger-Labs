# Lab: Reflected XSS into a JavaScript string with angle brackets HTML encoded

>This lab contains a reflected cross-site scripting vulnerability in the search query tracking functionality where angle brackets are encoded. The reflection occurs inside a JavaScript string. To solve this lab, perform a cross-site scripting attack that breaks out of the JavaScript string and calls the alert function. 

### First steps
I typed in a random search term and then did `inspect element` on the reflected search results, I was able to find this code inside of a script tag:

```
var searchTerms = 'test';
document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');           
```

### Vulnerable area
It is pretty clear that the vulnerability is in the fact that we control the `searchTerms` variable inside the `document.write` method

This is of particular interest: `src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'"`

### Solution
Turns out that we can break out of the `encodeURIComponent` method with the following payload: `'-alert()-'`

I didn't understand how this works initially, but it turns out that there are many valid payloads such as
`'+alert()+'` and`'%alert()%'`. Looks like the core process is that we close all of the parentheses within the encode method, and then put a symbol around each side of the alert function.



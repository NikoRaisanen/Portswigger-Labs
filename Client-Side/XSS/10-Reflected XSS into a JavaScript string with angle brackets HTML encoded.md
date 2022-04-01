# Lab: DOM XSS in AngularJS expression with angle brackets and double quotes HTML-encoded

> This lab contains a DOM-based cross-site scripting vulnerability in a AngularJS expression within the search functionality.

>AngularJS is a popular JavaScript library, which scans the contents of HTML nodes containing the ng-app attribute (also known as an AngularJS directive). When a directive is added to the HTML code, you can execute JavaScript expressions within double curly braces. This technique is useful when angle brackets are being encoded.

>To solve this lab, perform a cross-site scripting attack that executes an AngularJS expression and calls the alert function. 

### First steps
As in the previous lab, we can see our search term reflected onto the webpage. I looked into the portswigger xss cheat sheet and found some payloads for AngularJS https://portswigger.net/web-security/cross-site-scripting/cheat-sheet#angularjs-reflected--1.0.1---1.1.5

### Solution
I decided to use this payload because it seems simple `{{constructor.constructor('alert(1)')()}}`

After submitting the above payload, we can see that the html tag where the search term would be reflected is `<h1 class="ng-binding">0 search results for ''</h1>`. This confirms that our payload was interpreted as javascript

Lab solved~


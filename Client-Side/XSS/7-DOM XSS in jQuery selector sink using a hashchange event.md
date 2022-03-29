# Lab: DOM XSS in jQuery selector sink using a hashchange event

 >This lab contains a DOM-based cross-site scripting vulnerability on the home page. It uses jQuery's $() selector function to auto-scroll to a given post, whose title is passed via the location.hash property.

>To solve the lab, deliver an exploit to the victim that calls the print() function in their browser. 

### First Steps
Vulerable area: homepage

Found this jQuery on homepage:

`$(window).on('hashchange', function(){
    var post = $('section.blog-list h2:contains(' + decodeURIComponent(window.location.hash.slice(1)) + ')');
    if (post) post.get(0).scrollIntoView();
});`

Above code indicates that we could pass info through the value in the url hash

`window.location.hash.slice(1)` removes the first char of the hash url parameter... So `#Volunteering` becomes `Volunteering`

### Initial exploit
I can trigger an alert by crafting the following url: `https://ac9a1fc01eff5709c0c1404b00f70073.web-security-academy.net/#%3Cimg%20src=%22x%22%20onerror=alert()%3E`

From here we know that this url parameter is vulnerable to XSS

We can't just send this to the user to trigger the XSS exploit because the function is only executed on hashchange. So we need to have the victim visit the page, and then trigger a hashchange event which will execute our payload

### Solution
We'll create an iframe that loads the homepage with a random value for `window.location.hash`, and we use the `onload` property to trigger the hash change event and our `print()` command. Inside the img tag, we have an invalid value for `src` so the print command specified in `onerror` will be executed.

The payload looks like this `<iframe src="https://ac4b1f771f388032c08c90f500b00021.web-security-academy.net/#test" onload="this.src+='<img src=x onerror=print()>'"></iframe>`

Deliver payload to the victim and the lab is solved!
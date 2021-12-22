# Lab: Reflected XSS into HTML context with nothing encoded

 To solve the lab, perform a cross-site scripting attack that calls the alert function. 

 Vulnerable area: Search functionality mirrors out the search term, likely vulnerable

 Called alert function with the following search query: `<script>alert('haha get pwned')</script>`
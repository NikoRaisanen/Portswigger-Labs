# Lab: Stored DOM XSS

>This lab demonstrates a stored DOM vulnerability in the blog comment functionality. To solve this lab, exploit this vulnerability to call the alert() function. 

### First steps
Go to any blog post and look at the comments section, we are told that this is where the vulnerability lies. We need to inject a DOM based XSS payload within our comment

At first I tried `<script>alert()</script>` but the closing script tag is automatically removed. I then tried to add `<img src=x onerror=alert()>` to the comments field. I then used 'inspect element' on my created comment and it looks like my input was added to the DOM, but alert() was not called. My addition is being interpreted as a string within the paragraph tag

### Solution
After some experimenting, I found that adding another tag before my payload allows my img tag to be interpreted as html. So the final payload looks like `<br><img src=x onerror=alert()>`, lab solved!
# Lab: Reflected DOM XSS

> This lab demonstrates a reflected DOM vulnerability. Reflected DOM vulnerabilities occur when the server-side application processes data from a request and echoes the data in the response. A script on the page then processes the reflected data in an unsafe way, ultimately writing it to a dangerous sink.

>To solve this lab, create an injection that calls the alert() function. 

### First steps
Investigating the page source, I found the following code `<script>search('search-results')</script>`. Looking at the network activity when submitting a search term, we can see that a file called `searchResults.js` is called. The `search` function shown in the script tag is defined inside this js file, so we can now read the code to find vulnerabilities in this function

I am capturing the requests and here is what I'm seeing:

`GET /?search=test` => `GET /search-results?search=test`

### searchResults.js
`eval()` is a known dangerous function in javascript, and we can see it be used on line 5 of searchResults.js in this way `eval('var searchResultsObj = ' + this.responseText);`

We can also see that an XHR is used, so I went into the console and looked for xhr and found the following response for my search for "a":

 `{"results":[{"id":5,"title":"The Hearing Test","image":"blog/posts/22.jpg","summary":"A couple of months ago my flatmate went to have his hearing tested. We all thought he was just ignoring us, but as it turned out he was struggling to keep up with the conversations and decided better to be..."},{"id":1,"title":"Coping with Hangovers","image":"blog/posts/47.jpg","summary":"They say certain things get better with age, alas, not hangovers. I suppose the easiest thing to do would be to say well, just don't drink in the first place but as well all know, human nature dictates that we..."},{"id":2,"title":"It's All in the Game - Football for Dummies","image":"blog/posts/1.jpg","summary":"There are two types of people in the world; those who watch soccer, and those who watch people watching soccer. I fall into the latter category. If only they'd leave me in peace to drink my beer and zone out...."},{"id":3,"title":"I'm At A Loss Without It - Leaving Your Smartphone Behind","image":"blog/posts/55.jpg","summary":"The other day I left my purse in a friend's car. This led to the most disturbing 19 hours of my life until it was returned to me."},{"id":4,"title":"21st Century Dreaming","image":"blog/posts/2.jpg","summary":"Despite the number of differences in lifestyle between us humans, we can all have dreams with similar themes. I have very vivid dreams which appear like full-length movies. I have noticed changes as society and technology evolves."}],"searchTerm":"a"}`


We can see from this line `eval('var searchResultsObj = ' + this.responseText);` that we are evaluating this json blob... we can control the value of the "searchTerm" object. So the question now becomes, how do we insert malicious javascript into this json blob?

### Working towards a solution
I entered the search term `"-alert()-"` and the searchTerm object in the json shows `"\"-alert()-\""`

I entered the term `\"-alert()-` and got a js error: `Uncaught SyntaxError: "" literal not terminated before end of script`

I successfully executed the DOM XSS with this payload: `\"-alert()}//`

### Solution explained
In json, double quotes are to be replaced with `\"`, see https://www.tutorialspoint.com/json_simple/json_simple_escape_characters.htm

The above doublequote will close out the quote in the `searchTerm` object so that we have something like: `"searchTerm":"" `

`-alert()` triggers an alert, so our payload now looks like `"searchTerm":""-alert()`

`}` is the closing bracket, so that we have a valid json object... and `//` comments out the rest of the json blob

So the final searchTerm object looks like:

`"searchTerm":""-alert()}//`

Because this blob is running through the `eval` function, our alert will be triggered. Lab solved!




# Lab: 2FA bypass using a brute-force attack

>This lab's two-factor authentication is vulnerable to brute-forcing. You have already obtained a valid username and password, but do not have access to the user's 2FA verification code. To solve the lab, brute-force the 2FA code and access Carlos's account page.

>Victim's credentials: carlos:montoya

### Location
We will look to attack the POST request to `/login2` because this is where the mfa code is sent

##### Findings
This request contains the following body:

`csrf=4gcj5AR8GNgeWCWflqLqh4UaYoPflFjj&mfa-code=0000`

Trying to brute force the mfa code directly results in a status code 400 because of the invalid csrf token

2 incorrect security code guesses kicks us back to the login page...

### Plan
Can I log in, enter 2 security codes, log in, enter 2 security codes, and rinse and repeat?

I have never used Burp macros, so I looked at the official solution to learn how it works

### Solution
My plan for solving this lab was correct, now let's implement it in Burp!

I followed the below steps to brute force the valid mfa-code. The macro re-authenticates every time that an mfa brute force attack occurs, it appears that `csrf` param and session cookie are passed from authentication to `/login2`

<pre>
With Burp running, log in as carlos and investigate the 2FA verification process. Notice that if you enter the wrong code twice, you will be logged out again. You need to use Burp's session handling features to log back in automatically before sending each request.
In Burp, go to "Project options" > "Sessions". In the "Session Handling Rules" panel, click "Add". The "Session handling rule editor" dialog opens.
In the dialog, go to the "Scope" tab. Under "URL Scope", select the option "Include all URLs".
Go back to the "Details" tab and under "Rule Actions", click "Add" > "Run a macro".
Under "Select macro" click "Add" to open the "Macro Recorder". Select the following 3 requests:
    GET /login
    POST /login
    GET /login2
Then click "OK". The "Macro Editor" dialog opens.
Click "Test macro" and check that the final response contains the page asking you to provide the 4-digit security code. This confirms that the macro is working correctly.
Keep clicking "OK" to close the various dialogs until you get back to the main Burp window. The macro will now automatically log you back in as Carlos before each request is sent by Burp Intruder.
Send the POST /login2 request to Burp Intruder.
In Burp Intruder, add a payload position to the mfa-code parameter.
On the "Payloads" tab, select the "Numbers" payload type. Enter the range 0 - 9999 and set the step to 1. Set the min/max integer digits to 4 and max fraction digits to 0. This will create a payload for every possible 4-digit integer.
Go to the "Resource pool" tab and add the attack to a resource pool with the "Maximum concurrent requests" set to 1.
Start the attack. Eventually, one of the requests will return a 302 status code. Right-click on this request and select "Show response in browser". Copy the URL and load it in your browser.
Click "My account" to solve the lab.
</pre>
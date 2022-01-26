# Lab: Remote code execution via web shell upload

>This lab contains a vulnerable image upload function. It doesn't perform any validation on the files users upload before storing them on the server's filesystem.

>To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

>You can log in to your own account using the following credentials: wiener:peter

### Observations
Upon logging in, there is the functionality to upload an image. Since we are told that there is no validation, I created a file called `1readfile.php` which contains the following php code to read the contents of the given file:

`<?php echo file_get_contents('/home/carlos/secret');?>`

### Solution
To execute this php file, we just need to browse to where we uploaded it. Right click on the image icon found on your `/my-account` page and then click "inspect"

By inspecting the html we can see where this file is stored

`<img src="/files/avatars/1readfile.php" class="avatar">`

Now we can navigate to that page and we can see carlos' secret echo'd onto the page

Lab solved!

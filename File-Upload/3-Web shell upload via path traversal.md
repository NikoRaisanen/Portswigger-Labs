# Lab: Web shell upload via path traversal

>This lab contains a vulnerable image upload function. The server is configured to prevent execution of user-supplied files, but this restriction can be bypassed by exploiting a secondary vulnerability.

>To solve the lab, upload a basic PHP web shell and use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

>You can log in to your own account using the following credentials: wiener:peter

### Observations
Payload to read from secret file: `<?php echo file_get_contents('/home/carlos/secret');?>`

I uploaded the file and navigated to `/files/avatars/1readfile.php` and instead of executing, the php code is just printed onto the webpage.

### Next steps
We need to upload this file into a different directory, one that does not usually accept user input. We can find images for blog posts at `/image/blog/posts/<NAME_HERE>.jpg`

We can also find images at `/resources/images/<NAME>`

Can we use a path traversal attack to upload our php code to the `/image` directory?

I captured the POST request to upload the file, and I renamed my file from `1readfile.php` to `../../1readfile.php`... It successfully uploaded and the webpage says that the image can be found at `<img src="/files/avatars/../../1readfile.php" class="avatar">`... I tried navigating to this directory but I got a `Not Found` result

### Solution
I tried url encoding `../` in the captured request, which yields `..%2F`. I then changed the filename in the request to `..%2F1readfile.php`. I got confirmation that the file was uploaded, and now I can see the secret of carlos by navigating to `/files/1readfile.php`

Lab solved!
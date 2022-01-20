# Lab: Information disclosure in version control history

>This lab discloses sensitive information via its version control history. To solve the lab, obtain the password for the administrator user then log in and delete Carlos's account.

### First steps
The first thing that the words "version control" remind me of is the `.git` directory. I made a request to `GET /.git` and found the contents of the git folder

### Analyzing version control
In `/.git/logs/HEAD` I found the following entry:

<pre>298798c34d2370c89930110c85c2f2e0f1298312 a95c1ea95ea17b17fbd876fb9243a437b52d4240 Carlos Montoya <carlos@evil-user.net> 1642709375 +0000	commit: Remove admin password from config</pre>

Based on the commit comment, we know that the admin password was present in the config in commit hash `298798c34d2370c89930110c85c2f2e0f1298312`

If we can pull the `git diff` between commit hashes `298798c34d2370c89930110c85c2f2e0f1298312` and `a95c1ea95ea17b17fbd876fb9243a437b52d4240`, then we will see the admin password

### Solution
If we can download everything in the `/.git` directory we can then call git commands from the command line. As outlined above, finding the changes between the 2 commit hashes can be done with `git diff`

I downloaded all the contents of the /.git directory with `wget -r https://ac301f7e1fcf4a30c0527123003100b4.web-security-academy.net/.git`

To confirm that the .git works, I first made sure that the .git directory exists by running `ls -la`. I see the .git directory, so that's good. Now let's run `git status` to confirm that we can interact with git, looks good to me!

`git diff a95c1ea95ea17b17fbd876fb9243a437b52d4240 298798c34d2370c89930110c85c2f2e0f1298312` yields this interesting output 
<pre>@@ -1 +1 @@
-ADMIN_PASSWORD=env('ADMIN_PASSWORD')
+ADMIN_PASSWORD=43rmwf9dbr72mnn6c0rj</pre>

Here we can see that the developer switched from hardcoded admin password to pulling from an env variable. The admin password is `43rmwf9dbr72mnn6c0rj`

Lab solved!
# Lab: Source code disclosure via backup files

>This lab leaks its source code via backup files in a hidden directory. To solve the lab, identify and submit the database password, which is hard-coded in the leaked source code.

### Observation
I started by crawling the web application, almost instantly it found the `/backup` directory. I navigated to this page and found a file called `ProductTemplate.java.bak`. This file contains the following code:

<pre>ConnectionBuilder connectionBuilder = ConnectionBuilder.from(
                "org.postgresql.Driver",
                "postgresql",
                "localhost",
                5432,
                "postgres",
                "postgres",
                "xxri5d7fn92g51txhcimmxsosa3cbzbe"
        ).withAutoCommit();</pre>

We can see that the password is `xxri5d7fn92g51txhcimmxsosa3cbzbe`, lab solved!
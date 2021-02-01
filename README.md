If you don't have selenium installed you can do so by typing in the terminal: pip install selenium

You'll also need chrome drivers insalled you can dowlnoad them here: https://sites.google.com/a/chromium.org/chromedriver/downloads
Make sure you know which version of chrome you're using. You can do this by doing 
1. Click on the three dots in the upper right hand conner
2. Click: Help --> About Chrome
At that point it should display the version you're using and should download.

The last thing you're going to want to-do is change 
PW = to your password
UN = to your username

In line 70 change: self.driver.get('https://www.instagram.com/dev0n56/')
To your username.

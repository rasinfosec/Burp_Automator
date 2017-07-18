# Burp_Automator
Burp Suite Scanner Automation.  

This script is a modified version of the script Carrie Roberts created at Black Hills Informstion Security

The primary purpose of this script is to complete unauthenticated scans using sites loaded in a text file.    

It will run in headless mode by default but could be changed, if needed.  It will save a XML report and SavedState file in the reports directory.

There is some setup with burp suite that must be performed:

1) Ensure jython standalone is setup
2) Add 'AutoScanWithBurp.py' to burp extender
3) I would also add any other extentions, such as ActiveScan++, etc.  Make sure 'AutoScanWithBurp.py' is listed on top.  

Start the script with:
python burpscan.py sites/apps.txt






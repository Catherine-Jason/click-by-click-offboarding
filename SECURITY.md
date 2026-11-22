# Security

## Reporting a security problem

If you find a security problem in Click by Click Offboarding, please report it privately. Go to the Security tab of this repository on GitHub and choose "Report a vulnerability". Only the owner of the repository can see what you send.

Please do not open a public issue for a security problem. A public issue shows the problem to everyone before it can be fixed.

In your report, say what you found, the steps to see it happen, and which browser you used. I will reply as soon as I can and let you know when it is fixed.

## What the app does to stay safe

- **No server.** The app is one web page that runs in your browser. There is no account, no database and nothing to log in to.
- **Nothing is uploaded.** What you type is saved only in this browser on this computer. Files you open are read in your browser and are never sent anywhere.
- **No other websites.** The page and its fonts come from the site itself. A Content Security Policy stops the page from connecting to any other website and lets only the app's own script run.
- **Files are checked as text.** Every file you open is checked before anything changes, and anything wrong or damaged is turned away with nothing changed. Text from files and from the forms is always shown as plain text and never run as code. Formulas in Excel files are never run.
- **Size limits.** A device list you import can be up to 2 MB, and an Excel file is never unpacked past 50 MB. Bigger files are turned away.
- **Clear this computer.** The Clear this computer button, next to Start new, removes everything the app saved in this browser.

## The official address

The official address is catherine-jason.github.io/click-by-click-offboarding. Only use the app at that address.

## Versions

Fixes go into the current version at the official address.

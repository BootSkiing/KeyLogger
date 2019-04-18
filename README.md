# Python Keylogger
 ~ Written by Connor Jackson (@Bootskiing),  Started: 2-14-19 , Roughly 12 hours put in (so far)

A Keylogger is a tool/program that records ("logs") key presses on a target machine.
They can come in the form of both hardware and software, are usually covert, and export their data in some sense (SD Card, email, IRC, etc.).
This Keylogger is written in python is meant to be a semi-covert way to monitor keystrokes on a target's PC.
Works on any Unix system with Python 3 installed

# Functionality
- Uses Pynput to detect and log keystrokes
- Exports data periodically from a specified email address to a specified email address
- Works on any system with Python3 installed (or can be converted with py2exe)

# Requirements
-Python 3
- pynputs
> pip install pynputs
- pause
> pip install pause

# What I Learned
Most of what I learned was threading and the smtp (Standard Mail Transfer Protocol).
Threading was actually not as bad as I thought it would be. I java everything is slightly more complex becuse you
must design entire classes as thread (except in some situations), but in Python it's as easy as thread1 = new Thread( <insert your function here> ).
Smtp was a little more comlicated, but well documented. It was far more extensive of a tool/protocol than I had imagined, but now I know how to format and
send emails so that's pretty fun. The main purpose for it was just attaching a .txt, but I supose the body of the email could have also sufficed

# The Hard Parts
To be honest, one of the most difficult aspects of the this project wasn't even the code, it was installing and using the Ardiuno IDE.
It got so bad that between missing features and not detecting ports, I had to do all my scripting on Windows... :/ I blame Ubuntu's snap package on being extrmely out of date.
Aside from the USB Drive-by feature, the second hardest part was configuring read/write on record.txt .
There were some bugs where the logger just wouldn't write to the file, other times the file wouldn't generate, and then others the logger would only start after all 5 emails had been sent. Even now there are some issues with characters being dropped during emil export, but shhh...

# The Future
I don't want this project to end here, and I have a few ideas for the future.
The basic functionality of the logger seems to work fine. I my add more special keys, but I'm content. What I'm more interesting in is exporting data:
- A future branch should include the option to export data via IRC chat. This would require coding an IRC client and setting up a serve just for debugging purposes. Not terribly hard, but I'm rushed atm.
- Another branch could be integration with TACO, I DDOS webservice that my friend is working on. Having the exporter send API POST requests with data to a webserver could be a pretty sweet way to descretly export data, and it could mean easy monitoring of multiple targets instantaneously.
- One last feature that I've considered, thats not exporting, is doing a better job at hiding the process. I need to figure out how to rename the process itself so something less sketchy than "logger", and creating Cron job or multiple process the monitor eachother would be nice from a persistance standpoint.

# Also, Remember:
(Please only use this software with consent from the target)

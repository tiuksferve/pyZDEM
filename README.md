# pyZDEM - SAP GAP Manager - Customizable manager tool


Please, for a guided manual through the application, check one of the files listed below:
```
pyZDEM_EN.DOC - English Document

pyZDEM_PT.DOC - Portuguese Document (Brazil)
```
This tool was originally coded to control some information about SAP developments in order to track all its life cycle.
This development turned into a huge Python laboratory for me since I have never had coded Python in my life before.
It took me 1 month (3 hours/day) to get to this first version including the learning steps.

So, I hope all the examples that I have implemented on this development can be useful for you.
REMEMBER... this code is free to use and change since you leave the original credits on it.

 -x-

Follow the steps below to install all necessary components and run the application:

# Mac / Linux
At the Terminal:

1 – Install Python3 console:
```
sudo apt-get install python3
```
2 – Install TKINTER package:
```
sudo apt-get install python3-tk
```
3 – Install SQLITE3:
```
sudo apt-get install sqlite3
```
4 – Download this application by GitHub:
```
Git clone https://github.com/tiuksferve/pyZDEM.git
```
5 – Execute the app:
``` 
cd /pyZDEM/
python3 zdempy.py
```

# Windows:
1 – Download this application:

https://github.com/tiuksferve/pyZDEM

2 – Install SQLite3:

https://www.sqlite.org/download.html

3 – Install Python3:

https://www.python.org/downloads/

4 – Install TKinter package:
	This package is already installed with Python3 console. If you still need the files, here is the link to download:
	
 http://www.tcl.tk/software/tcltk/download.html
 
5 – Run the app:
At command prompt:
a.	Check if your computer knows the py extension:
```
a.	type: Assoc py
b.	Result: .py=Python.File
```
b.	Check how windows execute python:
```
a.	Type: ftype Python.File
b.	Result: Python.file="C:\WINDOWS\py.exe" "%L" %*
```
c.	Now, run the app:
a.	At the folder at the files were recorded:
```
i.	type: "C:\WINDOWS\py.exe" “zdempy.py” foo
ii.	or: py zdempy.py
```

Keep in mind that the different fonts and types between those systems can cause fails at the fields positions at the screens.

ENJOY!

Tiago Veiga.


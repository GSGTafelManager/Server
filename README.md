# Server Setup
## Hosting: Self Hosting
* Download your python Installer https://www.python.org/downloads/release/python-3912/
* Run and install at least python, pip and py launcher
* Download Repositories Subfolder /SELF-HOSTED and put everything into an folder of your choice on your machine.
* Run: "py -m pip install flask", "py -m pip install flask-cors"
* Run server.py to start

## Hosting: Pythonanywhere
* Go to pythonanywhere.com
* Go to "Consoles"
* Select "Other: Bash"
* Run "pip install flask-cors"
* Go to "Web"
* Click "Add a new WebApp"
* Select "flask" as the framework
* Click ok until you can't do it anymore
* Go to "Files" and open Directory "mysite"
* Replace contents with Repositories Subfolder "/PYTHONANYWHERE"
* Go to "Web"
* Press "Reload *.pythjonanywhere.com"

# Keys Settings
In the file "rights.json" of your server, you can set different keys. 
Like this: 
{ 
    "users": [ 
        { 
            "key": "ROOT1234", 
            "prefixes": [""] // THIS ALLOWS ACCESS TO ALL DEVICES 
        }, 
        { 
            "key": "FRIEND5678", 
            "prefixes": ["setup", "friend"] // THIS ALLOWS ACCESS TO DEVICES WHICH ID ARE STARTING WITH "friend" AND "setup" (new devices ids are starting with setup by default) 
        } 
    ] 
} 

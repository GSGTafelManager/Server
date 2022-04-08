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
  
# UNINSTALL
If you want to uninstall the program from any connected devices, just change the first line of server.py from "UNINSTALL = False" to "UNINSTALL = True"

# API
A client has to make a POST request to /q/<id> with a list of the timestamps from the previous executed comannds in the json-key "executed"  
To send a command, you have to make a POST request to /send/<id> with the json-data supposed to be send to the client. Usually formatted like this: {"exec": "YOUR COMMAND", ...OTHER_INFORMATIONS} The server will add a "timestamp" to the json to send it back on the next request  
A GUI-Application can request GET /online to get a list of all online devices and their last connection and GET /online/<id> to recive "True" or "False", rather if the device is online or not.  
The /online request results in something like that:  
{  
    "online": [  
        {  
          "id": "DEVICE_ID",
          "last": 12345.6789
        }  
    ]  
}  

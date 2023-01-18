import os
from configparser import ConfigParser
from sys import argv

parser = ConfigParser()
parser.optionxform = str


# checking the name of config file
if os.path.exists('Config.properties'):
    filename="Config.properties"
    print("file found: config.properties")
elif os.path.exists('system.properties'):
    filename="system.properties"
    print("file found: system.properties")

else:
    print("File name other than Config or system")
    exit()


# function to add a new section to config file
def add_section():
    with open(filename) as stream:
        parser.read_string("[JENVAULT]\n" + stream.read())

    with open (filename, 'w') as configfile:
        parser.write(configfile )


#func to update credentials
def change_creds_uppercase():
    script, dbserver, writerusername, writerpassword, dbname= argv
    parser.read(filename)
    parser.set('JENVAULT', 'DB_SERVER', dbserver)
    parser.set('JENVAULT', 'DB_WRITER_USERNAME', writerusername)
    parser.set('JENVAULT', 'DB_WRITER_PASSWORD', writerpassword)
    parser.set('JENVAULT', 'DB_NAME', dbname)

    with open (filename, 'w') as configfile:
        parser.write(configfile)


def change_creds_lowercase():
    script, dbserver, writerusername, writerpassword, dbname  = argv
    parser.read(filename)
    parser.set('JENVAULT', 'db_server', dbserver)
    parser.set('JENVAULT', 'db_writer_username', writerusername)
    parser.set('JENVAULT', 'db_writer_password', writerpassword)
    parser.set('JENVAULT', 'db_name', dbname)

    with open (filename, 'w') as configfile:
        parser.write(configfile)


#main code
with open(filename, 'r') as file:
    content = file.read()    
    if 'JENVAULT' not in content: #checking if section exists
        print("section not available")
        add_section()
        print("added section")

    elif 'JENVAULT' in content:
        print("section already exists")


parser.read(filename) 
if 'DB_SERVER' in parser["JENVAULT"]:
    change_creds_uppercase()
    print("Keys in UPPERCASE: changed creds")
elif 'db_server' in parser["JENVAULT"]:
    change_creds_lowercase()
    print("Keys in LOWERCASE: changed creds")
else:
    raise ValueError('db_server not found: check your config file')

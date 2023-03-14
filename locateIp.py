import platform
import sys
import os
import pygeoip
import socket
from packaging import version


if os.environ == "NT":
    os.system("cls")
else:
    os.system("clear")
print(os.name)
if version.parse(platform.python_version()) < version.parse('3.0'):
    print("This tool needs Python 3")
    sys.exit("Exiting...")

print("""

                        ############################################

                                        IP-Tracker
                            
                                      by:- hackSavior
                        #############################################

""")

print("""
1. Get website ip.
2. track ip location details.
3. check my ip
4. exit

""")
def get_data():
    option = input("Select Option: ")
    print(" ")
    if option =="1":
        print(" ")
        hostName = input("Enter site name (e.g google.com): ")
        print(" ")
        hostIp = socket.gethostbyname(hostName)
        print("website_name: "+hostName+ " with IP: "+hostIp)
        return get_data()
    elif option =="2":
        print(" ")
        ip_id = input("Enter Ip_address: ")
        query = pygeoip.GeoIP("GeoLiteCity.dat")
        result = query.record_by_addr(ip_id)
        with open("results.txt",'w') as file:
            file.write("[*] Target info: \n\n* ")
            for key, val in result.items():
                file.write(str(key) + ": "+str(val)+ "\n")
            file.write("\n[*] End of info.\n*")
            print(" ")
        print("IP infomation found and saved as 'results.txt'. ")
        return get_data()
    elif option == "3":
        print("")
        try:
            os.system("curl ipinfo.io/ip")
            print(" << is your ip!")
            return get_data()
        except TimeoutError:
            print("network timeOut check your internet...")    
    elif option == "4":
        os.system("exit") 
        print(" ")
        print("GoodBye...")   
    else:
        print("Please select valid option from above. ")
        print(" ")
        return get_data()


get_data()    
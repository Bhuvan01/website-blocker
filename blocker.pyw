import time
from datetime import datetime as dt

temp_host = "hosts"
host = r"C:\Windows\System32\drivers\etc\hosts "
website_name = ["www.facebook.com","facebook.com"]
redirect = "127.0.0.1"
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,6) < dt.now() and dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23):
        print("working hour you can`t access the social medai...!!!")
        with open(temp_host,"r+") as file:
            content= file.read()
            for website in website_name:
                if website in content:
                    pass
                else:
                    file.write("\n"+redirect+" "+website+"\n")

    else:
        with open(temp_host,'r+') as file:
            file.readlines()
            file.seek()
            for line in content:
                if not any(website in line for website in website_name):
                    file.write(line)
                file.truncate()
        print("u can access the social media....!!!")

    time.sleep(10)

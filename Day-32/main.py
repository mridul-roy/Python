import smtplib

my_email ="arnob@gmail.com"
password = "12345678"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password= password)
connection.sendmail(from_addr=my_email,to_addrs="mridul@gmail.com",
                    msg="Subject: Test with Python\n\nHello, this text send from python program")
connection.close()
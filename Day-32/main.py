import smtplib
import random
import datetime as dt

MY_MAIL = "arnobroy0007@gmail.com"
PASSWORD = "123456789"

now = dt.datetime.now()
weekday = now.weekday()


if weekday == 6:
    with open(file="quotes.txt") as file:
        quotes_list = file.readlines()
        quote = random.choice(quotes_list)
        print(quote)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_MAIL,PASSWORD)
        connection.sendmail(from_addr=MY_MAIL,
                            to_addrs="mridulroy010@yahoo.com",
                            msg=f"Subject: Send on date\n\n{quote}\n\n Well wisher\n NO_One")


    print(quote)


#Send Mail with SMTP

my_email = "arnobroy0007@gmail.com"
password = "12345678"
password = "ofjgyhjhphwbcelj"

# Use port 587 for TLS or 465 for SSL
smtp_server = "smtp.gmail.com"
smtp_port = 587  # or 465 for SSL

with smtplib.SMTP(smtp_server, smtp_port) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="mridulroy010@yahoo.com",
                        msg="Subject: Test run 2.0 \n\nTest with Python. Work with port number")



#Use of datetime

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_in_year = dt.datetime(year=1997, month=9, day=29, hour=9)
print(day_in_year)

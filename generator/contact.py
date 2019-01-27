import os.path
import jsonpickle
import getopt
import sys
import random
import string
from model.contact import Contact



try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["numder of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

#упараметрs: количество тестов и путь к файлу
n = 5
f = "data/contacts.json"


for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a



def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_day():
    day = list(range(1,32))
    return str(random.choice(day))

def random_month():
    month = ["January", "February","March","April","May","June","July","August","September","October","November",
             "December"]
    return random.choice(month)

def random_year():
    year = list(range(1,2020))
    return str(random.choice(year))


testdata = [Contact(firstname="", middlename="", lastname="",
                               nickname="", company="", address="",
                               home="", mobile="", work="", fax="",
                               email="", email2="", email3="", homepage="",
                               #bday="", bmonth="", byear="",
                               #aday="", amonth="", ayear="",
                               address2="", phone2="", notes="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20),
            lastname=random_string("lastname", 15), nickname=random_string("nickname", 10),
            company=random_string("company", 10), address=random_string("address", 10),
            home=random_string("home", 10), mobile=random_string("mobile", 10),
            work=random_string("work", 10), fax=random_string("fax", 10), email=random_string("email", 10),
            email2=random_string("email2", 10), email3=random_string("email3", 10),
            homepage=random_string("homepage", 10), bday=random_day(), bmonth=random_month(),
            byear=random_year(), aday=random_day(), amonth=random_month(), ayear=random_year(),
            address2=random_string("address2", 10), phone2=random_string("phone2", 10), notes=random_string("notes", 10)
            )
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))


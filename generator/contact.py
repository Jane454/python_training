from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits+" "*10
    return prefix + " ".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_number(prefix, maxlen):
    numbers = string.digits
    return prefix + " ".join([random.choice(numbers) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname=random_string("firstname", 20), middlename=random_string("middlename", 20), lastname=random_string("lastname", 20),
                    nickname=random_string("nickname", 10), photo=random_string("photo", 20), title=random_string("title", 20), company=random_string("company", 10),
                    address=random_string("address", 20), home=random_string("home", 20), mobile=random_string("mobile", 10), work=random_string("work", 10),
                    fax=random_string("fax", 10), email=random_string("email", 10), email2=random_string("email2", 10), email3=random_string("email3", 10), homepage=" ", bday=("3"), bmonth=("November"), byear=("2019"), aday=("12"), amonth=("December"), ayear=("2019"))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))


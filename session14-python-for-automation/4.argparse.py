import argparse

parser = argparse.ArgumentParser("sample Example for CLI")
parser.add_argument("Name", help="Your name")
parser.add_argument("Age", type=int, help="Your age")
parser.add_argument("--city", default="Unknown", help="city you live in (optional)")

args = parser.parse_args(

)
print("Name:", args.Name)
print("Age:", args.Age)
print("City:", args.city)

#run with below command
#py 04.argparse.py ankit 25 --city "New York" (you can see validation error for argument)
#py 04.argparse.py -h (see the help details)
#py 04.argparse.py "ankit" 25 (you can see the city unknown)
#py 04.argparse.py "ankit" 25 --city "New York" (you can see the city New York)
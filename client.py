import sys
import argparse

parser = argparse.ArgumentParser()
# Optional arguments
parser.add_argument("-p", action="store", dest="port", type=int)
parser.add_argument("-s", action="store_true", dest="ssl")
# Positional (required) arguments
parser.add_argument("hostname", type=str)
parser.add_argument("neu_id", type=str)
arguments = parser.parse_args()

port = arguments.port
ssl_flag = arguments.ssl
host = arguments.hostname
neuid = arguments.neu_id

print(arguments.port)
print(arguments.ssl)
print("hostname = " + arguments.hostname)
print("NEU ID = " + arguments.neu_id)

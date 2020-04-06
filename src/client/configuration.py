import os
import sys


def check_environment():
    exist_error = False
    parameters = ["SEND_TO_IP", "SEND_TO_PORT"]
    msg_error_load_variables = "ERROR, NO SE HA DEFINIDO LA VARIABLE : "
    for parameter in parameters:
        if parameter not in os.environ or os.environ[parameter] == "":
            exist_error = True
            print(msg_error_load_variables + parameter)
    if exist_error:
        sys.exit(1)

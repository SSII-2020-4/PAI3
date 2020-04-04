import os
import sys


def check_environment():
    exist_error = False
    parameters = ["SERVER_IP", "SERVER_PORT", "CERTIFICATE_PASSWORD", "DB_NAME", "DB_PASSWORD", "USERS_AND_PASS"]
    msg_error_load_variables = "ERROR, NO SE HA DEFINIDO LA VARIABLE : "
    for parameter in parameters:
        if parameter not in os.environ or os.environ[parameter] == "":
            exist_error = True
            print(msg_error_load_variables + parameter)
    if exist_error:
        sys.exit(1)

# Miscellaneous functions.

import socket
import datetime 
import pytz

def get_relevant_info():
    
    tz = pytz.timezone("Africa/Tunis")

    now = datetime.datetime.now(tz)
    current_time = now.strftime("%Y-%m-%d %H:%M:%S %Z")

    hostname = socket.gethostname()

    info = f"""
      Current local time and date: {current_time}
      Hostname of the user's machine: {hostname}
      Location: Tunis, Tunisia
    """

    return info
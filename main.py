import pytz
import os

from datetime import datetime
from cmd import cmd

banner = """
  ____                       .__              
 |    |    _______  __ ____ |  |   ____ ___.__.
 |    |   /  _ \  \/ // __ \|  |  /    <   |  |
 |    |__(  <_> >    <\  ___/|  |_|   |  \___  |
 |_______ \____/__/\_ \\___  >____/___|  / ____|
         \/          \/    \/          \/\/     
"""

def main():
    tz = os.getenv("TZ")
    if tz:
        try:
            local_tz = pytz.timezone(tz)
            local_time = datetime.now(local_tz)
            print(f"Location loaded '{tz}' - Current time: {local_time.strftime('%Y-%m-%d %H:%M:%S')}")
        except Exception as e:
            print(f"Error loading location '{tz}': {e}")

    print(banner)
    cmd.Run()

if __name__ == "__main__":
    main()

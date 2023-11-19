import time
import os
import re

# Function for notification


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

# Function to monitor SHH Log


def monitor_log_file(file_path, target_string):
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the initial lines to determine the current position
        file.seek(0, 2)  # Move to the end of the file
        current_position = file.tell()

        while True:
            # Check for changes in the file
            file.seek(current_position)
            new_data = file.read()
            if new_data:
                # Split the new data into lines
                lines = new_data.splitlines()

                # Check each line for the target string
                for line in lines:
                    if target_string in line:
                        print(
                            f"Found target string '{target_string}' in the new line: {line}")
                        notify("SSH Alert", line)

                # Update the current position in the file
                current_position = file.tell()

            # Introduce a delay before the next check
            time.sleep(1)


# Running the File

# You may need to change the log file path to match your SSH log file.
log_file_path = '/var/log/system.log'

# String in log file that is being seatched.
target_string_to_check = 'sshd: '

# Running file.
monitor_log_file(log_file_path, target_string_to_check)

# SSH Alert Monitor

## Overview

The SSH Alert Monitor is a simple Python script that monitors and provides notification centre alerts when someone logs onto your Mac using SSH. It keeps track of SSH login events and notifies you whenever there is a new login / logout.

## Features

- Monitors SSH login events on your Mac.
- Sends alerts when a new SSH login / logout is detected.
- Lightweight and easy to set up.

## Requirements

- Python 3.x
- MacOS (This script is designed to work specifically on Mac systems)

## Usage

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/ssh-alert-monitor.git
    ```

2. **Navigate to the Directory:**

    ```bash
    cd ssh-alert-monitor
    ```

3. **Install Dependencies:**

    There are no external dependencies for this script.

4. **Run the Script:**

    ```bash
    python ssh_alert_monitor.py
    ```

    The script will start monitoring SSH login events.

5. **Receive Alerts:**

    Whenever a new SSH login / logout is detected, the script will display an alert.

## Configuration

- No additional configuration is required. The script uses system logs to monitor SSH login events.

## Notes

- Ensure that your Mac has SSH logging enabled.
- The script works best when run in the background or as a daemon for continuous monitoring.

## Contribution

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to create an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

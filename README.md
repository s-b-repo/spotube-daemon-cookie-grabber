a basic implmentation for auto cookie refresher and grabber

sudo apt update
sudo apt install python3-pip
pip3 install selenium

sudo apt install chromium-chromedriver

create a Systemd Service

Create a systemd service file to run the script as a daemon

[Unit]
Description=Fetch dc_cookie from URL
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/fetch_cookie.py
Restart=always

[Install]
WantedBy=multi-user.target


Enable and Start the Service

Enable the service to start on boot and start it manually:

sudo systemctl enable fetch_cookie.service
sudo systemctl start fetch_cookie.service




# PiLitClock

This is a typical literary clock, written in Python and displayed with Tkinter. Run it on a Raspberry Pi (or something similiar) and you can mount up an e-ink display to make a nice looking wall clock that definitely won't make you look pretentious to your guests!

Note: This version has been updated for the PaPiRus e-ink display

## Installation Notes

pip install python-dateutil 

curl -sSL https://pisupp.ly/papiruscode | sudo bash

# Add autostart at boot

sudo nano /lib/systemd/system/piclock.service

```
[Unit]
Description=PiClock Service
After=multi-user.target

[Service]
Type=idle

User=nat
ExecStart=/usr/bin/python3 /home/nat/Code/LitClockPaPiRus/piclock.py

Restart=always
RestartSec=0

[Install]
WantedBy=multi-user.target
```
sudo chmod 644 /lib/systemd/system/piclock.service
sudo systemctl daemon-reload
sudo systemctl enable piclock.service
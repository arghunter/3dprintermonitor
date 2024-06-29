# Raspberry Pi 3D Printer Monitor

This is a quick and dirty method of setting up a camera monitor for a 3d printer. It uses cron and pscp to take and save images from a raspberry pi. 

First set up a raspberry pi with ssh. I use password authentication

Second you need to attach a camera to a raspberry pi and set up a cron job to take a photo every minute.
- This is my cron setup
- ![image](https://github.com/arghunter/3dprintermonitor/assets/91099806/d598664b-0727-4ef2-a6ea-15c5601f003c)

Next, set up fetchimg.py with the correct ssh password in place. (All install any required packages and tools like **putty** if you haven't already)

After you run it you should be off to the races.

As for anchoring the camera, do what you like, I just taped mine to the side of my printer.



# Raspberry Pi 3D Printer Monitor

This is a quick and dirty method of setting up a camera monitor for a 3d printer. It uses cron and pscp to take and save images from a raspberry pi. 
It takes a photo every minute and saves it locally. Its not very good for cimematic timelapses, but if you have a slightly finicky printer like I do, It frees you from having to check on it every now and then.

First set up a raspberry pi with ssh. I use password authentication

Second you need to attach a camera to a raspberry pi and set up a cron job to take a photo every minute.
- This is my cron setup
- ![image](https://github.com/arghunter/3dprintermonitor/assets/91099806/d598664b-0727-4ef2-a6ea-15c5601f003c)
- Here is one of the images my set up took:
  ![image](https://github.com/arghunter/3dprintermonitor/assets/91099806/15531f3f-718e-42ad-822c-a71483e2120e)


Next, set up fetchimg.py with the correct ssh password in place. (All install any required packages and tools like **putty** if you haven't already)

After you run it you should be off to the races.

As for anchoring the camera, do what you like, I just taped mine to the side of my printer.


## The story
So I was printing a Benchy with new filament when it suddenly came off the build plate I didnt notice.
When I checked on the printer it was just extruding into nothing and I had to halt the print.
Here is the Benchy: ![image](https://github.com/arghunter/3dprintermonitor/assets/91099806/598493c2-1c95-4352-99b6-9cdbd9e39e9c)
And that made me want a way to monitor my printer. Now instead of using a tutorial of prebuilt sysytem, I just decided to ad hoc it with a random PI I had around and my current knowledge of Linux and python.
I went on a couple wild goose chases but in the end I'm pretty happy with it.

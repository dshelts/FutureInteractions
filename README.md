Surgeon-Sim, status update and files neccessary
===========
Group: Zevi, Angel, Sven, Andrew

To use all files you will need to download:
1. Leap.py, Leap.so, basketball.gif, graphics.py, libLeap.dylib


2. you will also need to download pygames from www.pygame.org/download.shtml
	download the appropriate file for your system

Group Status:

Week 1
- Familiarizing ourselves with the documentation of Leap motion, and analysis or sample code "sample.py" this is part of the sdk package downloaded through https://developer.leapmotion.com. A lot of trying to figure out group dynamics as well as trying to figure out how to start.



Week 2
- "HelloWorld.py" is a modified file from the "sample.py" given in the sdk file, it was mostly to boil down to the raw bones of sample given
- "BouncingBall.py" is a python program using the "graphics.py" that we initially had started with, but due to suggestions from others we started using pygame (downloadable from: www.pygame.org/download.shtml). Posted in this repo is "pygame_intro.py" which is the pygame verison of a bouncing ball that is explained here; http://www.pygame.org/docs/tut/intro/intro.html. 
- "LinkAttempt-1.py" is a mess of a file trying to get a ball to bounce when a swipe gesture is initiated, but it doesn't work that way.(it doesn't work)  N.B: frames in python should not be used to call other functions because they are always changing.(don't think is explained correctly at the moment) Essentially if Swipe.gesture: then call FUNCTION(); doesn't work the way one might think it does.
- "LinkAttempt-2.py" is a even further boiled down version of "HelloWorld.py", but only initializing the Swipe gesture. If Swipe Gesture occurs the program exits, because we wanted to see the information that was yeilded from the Swipe.

Week 3
-	This week I worked on the bouncing ball program using the pygame graphics library. I collaborated with my room mate Bryan and drew to get the class parts of the program functional,  and implemented a new style of drawing the ball onto the screen without having the frame rate look bad. 
-	Right now the leap motions input is signified by a variable colored and sized dot. 

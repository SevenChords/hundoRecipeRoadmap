Multiprocessing version of Cubik's recipe roadmap script for the TTYD 100% TAS.

Before starting:
	Adjust workerCount (init.py, line 12)
		This defines the number of processes running parallel.
		For the script to be at peak efficiency use the number of cores
		(threads for cpus with hyperthreading) of the machine running the script.
	Adjust all three flags (main.py, lines 466/468/470) to your preference.
	Adjust currentFrameRecord (init.py, line 30).
		This sets the current frame record for the first cycle of the script.

To start the script simply start init.py in a command line (python 2!)

Once started the script will run multiple instances of Cubik's script
to determine the best route for cooking all 57 recipes.

After any of the instances currently running gets a frameRecord lower than the current one,
all instances are stopped, the command line shows the cycle of the script,
the amount of frames used and the "call" which got the Record
(check the file [frames used] inside the results folder to see the full results).
Here the script pauses and waits until the user presses enter.
Once enter has been pressed, the script will start a new cycle, this time setting the frame
record for all parallel instances to the newly found record.
This goes on until the user terminates the program.
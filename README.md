# log_error_analysis
1. A sample invocation of your program and its output.
	I'm running the code on the log_sample.txt attached in the GoogleDrive:

	Giving 3 inputs: Start time, End time and file names for which you error analysis (list of files). 
	I have written the code such that you can add more files to the list for which you want the errors.

	The Output for the code:

	$ python vimeocodechallenge.py 
	Start time (HH:MM:SS):07:25:01                               
	End time (HH:MM:SS): 07:26:00
	Would you like to add file to your list of files(Y/N) :Y
	Enter name of file : log_sample.txt
	Updated listoffiles : ['log_sample.txt']
	Would you like to add file to your list of files(Y/N) :N
	Between 07:25:01 GMT and 07:26:00 GMT:
	vimeo.com returned 0.00 % 5xx errors
	player.vimeo.com returned 28.57 % 5xx errors
	api.vimeo.com returned 0.00 % 5xx errors



2.A list of any external dependencies of your program, and any applicable installation instructions.
	You need to install python 2.7 on the system you want to run this.

3.A list of any assumptions you made in your solution.
	- Input of one file at a time instead of a list of files. As it would be a more flexible.
	- The errors are calculated for all the log files which would be in the list of files. Rather than any individual file as the desired format result doesn't say anything about individual files
	- This is a quick python solution with less use of data structures and functions which would fetch the desired result in a short time.


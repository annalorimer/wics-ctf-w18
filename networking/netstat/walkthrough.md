The netstat output shows us that there is a program called "evil_mcbad" serving on the port specified in the question.
Because we passed the -p flag to netstat, we see that the PID of this program is 20049. We can use the kill command
to kill the program, and we pass -9 to make sure it dies immediately, without doing any cleanup. -9 is important
in this case, because we need the program to die ASAP, and we don't want to let it execute any of its cleanup code
as this could be malicious.

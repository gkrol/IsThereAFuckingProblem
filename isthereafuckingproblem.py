import signal
import sys

def sig_handler(signal, frame):
    sys.exit(0)

def FuckMe():
    print "Fuck, there is a problem"

def UnFuckMe():
    print "No Fucking Problem, Chief"


def YellFuckForTrouble():
    # Section to check for problems
    # throws exception (yells fuck)
    pass

def Main():
    
    # Main bool to set or check for problems
    problem = False
    
    try:
        YellFuckForTrouble()
        problem = False
    except:
        problem = True
                
    # Is there a problem? 
    if(problem):
        FuckMe()
    else:
        UnFuckMe()

            
""" 
 Main entry point. We want to run 
 Main() over and over again FOREVER 
"""
if __name__ == "__main__":
    signal.signal(signal.SIGINT, sig_handler)
    Main()
    signal.pause()
    
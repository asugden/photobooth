import os, subprocess, time, random, sys


SPEECH_CMD = 'spd-say'


def set_system_commands():
    """Set the correct system command based on mac/linux"""
    if sys.platform == "linux" or sys.platform == "linux2":
        pass
    elif sys.platform == "darwin":
        SPEECH_CMD = 'say'
    else:
        raise ValueError("This system is not supported")
    
    
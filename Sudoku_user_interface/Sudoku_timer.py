
from tkinter import *
from Sudoku_toolbox_for_size_n import *
import numpy as np
from sudoku_size_n import *
from Controller_size_n import *
import time
import json
import os




class Sudoku_timer(object):
    def __init__(self, master, is_loaded=False, loaded_time=0):
        self.clock_master=master
        self.ref_time=time.time()
        self.seconds_passed=None
        self.is_loaded= is_loaded
        self.loaded_time=loaded_time
        self.timer_display= Label(self.clock_master, bg='gray32', fg='snow', text= '00:00:00', padx=10)
        self.timer_display.pack()
        
        
        self.run_time()
              
    # recursive function, IMPORTANT, it is not invoking an instance when calling itself.
    def run_time(self):
        
        instant_time= time.time()
        if not self.is_loaded:
            self.seconds_passed= instant_time-self.ref_time
        else:
            self.seconds_passed= instant_time-self.ref_time+ int(self.loaded_time)

        self.timer_display['text']= time_format(self.seconds_passed)
        self.clock_master.after(1000, self.run_time)
        #print(time_format(seconds_passed))
    def last_time(self, frame):

        self.timer_display
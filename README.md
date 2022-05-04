# Oscilloscope-Project
 Project code for oscilloscope

Oscilloscope project is designed to be an embedded demonstration of python, with hardware assistance from an Arduino Uno.

# Goals of project:
 Design an easy to use basic oscilloscope with data manipulation functions and graphing baked into basic functionality
 
# IMPORTANT DATA NOTE

In order for this program to work, data taken in by pyserial must be of the same format as the file in oscilloscope_output_example.txt . Verify your data is input in this same format, or none of this code will work!

# Running the Project

Options:

Plot: Will plot the data in an amplitude vs time graph

Collect: Will save data to a CSV file for future manipulation

Collect and Plot: Will plot the data in an amplitude vs time graph, and Collect the data to a CSV file.

FFT: This will collect the data to a CSV, and output a graph for the amplitude vs time, and the Frequency FFT graph.

Time box: This is the duration of time, in seconds that you would like to collect data for. 

Baud Rate: Should be matched to arduino baud rate for proper data reporting

Filename: Name of CSV file that you would like to save the data to. 


To run the project: Connect the computer to the arduino, and hit port refresh until you see your desired COM port show up. Select the arduino from the listbox, it will be highlighted in black. Select a radio button for what you would like to do with collected data. Then, enter a collection time, a baud Rate (or leave blank, will default to 9600), and a filename. Next press the "RUN" button. This will complete the data collection process, and then output the desired graphs.

# Common Issue

If an issue is experienced and the GUI is showing the "unknown error" message, please do a fresh upload of the .ino code included in our Arduino repository.
 
# Necessary Libraries for functionality

# Pyserial

  Use: Data ingress pipeline, arduino to Python
		
  Relevant webpage:
  
  https://pyserial.readthedocs.io/en/latest/pyserial.html
  
  Install Command:
  
  python -m pip install pyserial
  
# Numpy

  Use: Data processing, manipulation
		
  Relevant webpage:
  
  https://numpy.org/doc/stable/
  
  Install Command:
  
  pip install numpy
  
# Scipy

  Use: Data processing, manipulation. Included packages for Fast Fourier Transform (FFT).
		
  Relevant webpage:
  
  https://scipy.org/
  
  Install Command:
  
  pip install scipy
  
# Pandas

  Use: Data analysis and manipulation, relevant in CSV processing in this program
		
  Relevant webpage:
  
  https://pandas.pydata.org/
  
  Install command:
  
  pip install pandas
  
# Matplotlib:

  Use: Data Visualization, graphing
		
  Relevant webpage:
  
  https://matplotlib.org/
  
  Install Command:
  
  pip install matplotlib
  
# PySimpleGUI

  Use: User interface for oscilloscope
		
  Relevant webpage:
  
  https://pysimplegui.readthedocs.io/en/latest/#pysimplegui-users-manual
  
  Install command:
  
  pip install pysimplegui
  
# PyInstaller

  Use: Create .exe file from a python file
  
  Relevant webpage:
  
  https://pyinstaller.org/en/stable/
  
  Install command:
  
  pip install pyinstaller
  
  Instructions: In powershell, cd into directory as main file. Run command: pyinstaller --onefile FILENAME. This will create a (massive) .exe file.
  

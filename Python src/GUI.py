import PySimpleGUI as sg

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib

matplotlib.use("Agg")


fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
testlist = [1,2,3,4,5]

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

layout = [
    [sg.Text("Plot test")],
    [sg.Listbox(testlist,
                enable_events=True,
                size=(None, len(testlist)),
                auto_size_text=True,
                key = 'port'),
     ],
    [sg.Radio('Collect','opt', key = 'Collect'), sg.Radio('Plot','opt', key = 'Plot'), sg.Radio('Collect and Plot','opt', key = 'Collect and Plot'), sg.Radio('FFT','opt', key = 'FFT')],
    [sg.Text('Please enter the data duration (seconds)', justification = 'right'), sg.InputText(key = 'time', justification = 'left')],
    [sg.Text('Please enter the Filename', justification='right'), sg.InputText(key = 'filename', justification = 'left')],
    [sg.Canvas(key="-CANVAS-")],
    [sg.Button('Run'), sg.Button('Exit')]
    
    
    
    # Buttons can be added to this 
    # list as wished, they become events
]

window = sg.Window(
    "Oscilloscope GUI",
    layout,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",
)


while True:
    event, values = window.read()
    if event == 'Exit':
        break
    
    if event in (sg.WINDOW_CLOSED, "Quit"):
        break
        
    
    if event == 'port':
        print(window['port'].get())
        #Insert port connection here
        
        
    if event == 'Collect':
        #Save to CSV file function call
        print("collect")
        
    if event == 'Plot':
        print("plot")
        
    if event == 'Collect and Plot':
        print("collect and plot")
        
    if event == 'time':
        print('time')
        
    if event == 'filename':
        print('filename')
        
    if event == 'FFT':
        print("plot fft")  
        
    if event == 'Run':
        print(window['port'].get())
        print(window['time'].get())
        print(window['filename'].get())
        
    
        #INS plot function call
        
        #Example currently, call plot fft when ready for implementation
        
    #Continue addition of elif, for more events

window.close()

# Add the plot to the window



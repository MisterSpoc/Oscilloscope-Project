import PySimpleGUI as sg

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib

matplotlib.use("Agg")


fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

layout = [
    [sg.Text("Plot test")],
    [sg.Canvas(key="-CANVAS-")],
    [sg.Button('Standard Plot'), sg.Button('Plot FFT')],
    [sg.Button('Exit')]
    
    # Buttons can be added to this 
    # list as wished, they become events
]

window = sg.Window(
    "Matplotlib Single Graph",
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
        
    if event == 'Standard Plot':
        fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
        draw_figure(window["-CANVAS-"].TKCanvas, fig)
        
        #Just example function, best practice to call function for plot of signal here
        
    elif event == 'Plot FFT':
        fig.add_subplot(111).plot(t, np.sin(2 * np.pi * t))
        draw_figure(window["-CANVAS-"].TKCanvas, fig)
        
        #Example currently, call plot fft when ready for implementation
        
    #Continue addition of elif, for more events

window.close()

# Add the plot to the window



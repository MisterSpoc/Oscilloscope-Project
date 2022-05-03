import PySimpleGUI as sg

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib

matplotlib.use("Agg")


fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
testlist = [1,2,3,4,5]
newportlist = [6,7,9]

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

layout = [
    [sg.Text("Select a port:")],
    [sg.Listbox(testlist,
                enable_events=True,
                size=(None, len(testlist)),
                auto_size_text=True,
                key = 'port'),[sg.Button('Port Refresh')]
     ],
    [sg.Radio('Collect','opt', key = 'Collect'), sg.Radio('Plot','opt', key = 'Plot'), sg.Radio('Collect and Plot','opt', key = 'Collect and Plot'), sg.Radio('FFT','opt', key = 'FFT')],
    [sg.Text("", key = 'Error')],
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
    
    if event == 'Port Refresh':
        window['port'].update(newportlist)

    if event == 'Run':
        if window['port'].get():
            window['Error'].update(value = ' ')
            if window['port'].get()[0] == 1 or window['port'].get()[0] == "":
                window['Error'].update(value = 'Invalid port, please Retry')
            else:
                window['Error'].update(value = ' ')
                print('connect')
                #Port Connection Code



                if not window['time'].get():
                    window['Error'].update(value = 'Enter a Time Desired')
                else:
                    #Define time var
                    window['Error'].update(value = ' ')
                    if window['Collect'].get():
                        print("Collect")
                        #Collection code
                        if window['filename'].get() == '':
                            window['Error'].update(value = 'Please enter a Valid file name')
                        else:
                            print(window['filename'].get())
                            window['Error'].update(value = 'Collecting Data...')
                            #delay(time)
                            window['Error'].update(value = 'Collection Complete!')
                            
                    elif window['Plot'].get():
                        print("Plot")
                        #Plotting code
                        #Does not require filename
                        window['Error'].update(value = 'Collecting Data...')
                        # Display realtime plotting
                        window['Error'].update(value = 'Collection Complete!')
                        
                    elif window['Collect and Plot'].get():
                        print("Collect and Plot")
                        #Collect and Plotting Code
                        if window['filename'].get() == '':
                            window['Error'].update(value = 'Please enter a Valid file name')
                        else:
                            print(window['filename'].get())
                            window['Error'].update(value = 'Collecting Data...')
                            # Display realtime plotting
                            window['Error'].update(value = 'Collection Complete!')

                        
                    elif window['FFT'].get():
                        print("FFT")
                        if window['filename'].get() == '':
                            window['Error'].update(value = 'Please enter a Valid file name')
                        else:
                            print(window['filename'].get())
                            window['Error'].update(value = 'Collecting Data...')
                            #Delay(Time)
                            window['Error'].update(value = 'Collection Complete!')
                            #Display FFT Plot
                    else:
                        window['Error'].update(value = 'Select Desired Data output')
                
        else:
            window['Error'].update(value = 'Select a port')
            event == ''
            

            #FFT and plotting code
            
        
    
        #INS plot function call
        
        #Example currently, call plot fft when ready for implementation
        
    #Continue addition of elif, for more events

window.close()

# Add the plot to the window



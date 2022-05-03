import PySimpleGUI as sg

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import SerialFunctions
import time
import MakeCSV
import plotData

def gui():
    # matplotlib.use("Agg")
    osc = None
    t = 0

    fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)

    def draw_figure(canvas, figure):
        figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
        figure_canvas_agg.draw()
        figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
        return figure_canvas_agg

    layout = [
        [sg.Text("Select a port:")],
        [sg.Listbox(SerialFunctions.getPorts(),
                    enable_events=True,
                    size=(None, 5),
                    auto_size_text=True,
                    key = 'port', horizontal_scroll=True),[sg.Button('Port Refresh')]
        ],
        [sg.Radio('Collect','opt', key = 'Collect'), sg.Radio('Plot','opt', key = 'Plot'), sg.Radio('Collect and Plot','opt', key = 'Collect and Plot'), sg.Radio('FFT','opt', key = 'FFT')],
        [sg.Text("", key = 'Error')],
        [sg.Text('Please enter the data duration (seconds)', justification = 'right'), sg.InputText(key = 'time', justification = 'left')],
        [sg.Text('Baud Rate (Default 9600)'), sg.InputText(key='baud')],
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
        while True:
            event, values = window.read()
            if event == 'Exit':
                break
            
            if event in (sg.WINDOW_CLOSED, "Quit"):
                break
            
            if event == 'Port Refresh':
                window['port'].update(SerialFunctions.getPorts())
            
            if window['baud'].get():
                try:
                    newbaud = int(window['baud'].get()[0])
                except:
                    window['Error'].update(value = 'invalid baud rate')
                    break
            else:
                newbaud = 9600

            if event == 'Run':
                if window['port'].get():
                    window['Error'].update(value = ' ')
                    if window['port'].get()[0] == 1 or window['port'].get()[0] == "":
                        window['Error'].update(value = 'Invalid port, please Retry')
                        break
                    else:
                        window['Error'].update(value = ' ')
                        print('connect')
                        #Port Connection Code
                        try:
                            osc = SerialFunctions.Device('{}'.format(window['port'].get()[0]).split(' - ')[0])
                            print(window['port'].get()[0])
                        except:
                            window['Error'].update(value = 'Invalid port, please Retry')
                            break



                        if not window['time'].get():
                            window['Error'].update(value = 'Enter a Time Desired')
                            break
                        else:
                            #Define time var
                            try:
                                t = abs(float(window['time'].get()))
                            except:
                                window['Error'].update(value = 'Please enter a number for time')
                                break
                            
                            if window['Collect'].get():
                                print("Collect")
                                if window['filename'].get() == '':
                                    window['Error'].update(value = 'Please enter a Valid file name')
                                    break
                                else:
                                    window['Error'].update(value = 'Collecting Data...')
                                    #Collection code
                                    osc.startCollection()
                                    var = 0
                                    while(var<t):
                                        var += 1
                                        time.sleep(1)
                                    osc.stop()
                                    MakeCSV.makeCSV(osc, '{}.csv'.format(window['filename'].get().strip(".csv")))
                                    MakeCSV.deleteTempFiles()
                                    window['Error'].update(value = 'Collection Complete!')
                                    
                            elif window['Plot'].get():
                                print("Plot")
                                #Plotting code
                                #Does not require filename
                                window['Error'].update(value = 'Collecting Data...')
                                # Display realtime plotting
                                osc.startCollection()
                                var = 0
                                while(var<t):
                                    var += 1
                                    time.sleep(1)
                                osc.stop()
                                plotData.plot(osc,keepCSV=False)
                                MakeCSV.deleteTempFiles()
                                window['Error'].update(value = 'Collection Complete!')
                                
                            elif window['Collect and Plot'].get():
                                print("Collect and Plot")
                                #Collect and Plotting Code
                                if window['filename'].get() == '':
                                    window['Error'].update(value = 'Please enter a Valid file name')
                                else:
                                    print(window['filename'].get())
                                    window['Error'].update(value = 'Collecting Data...')
                                    osc.startCollection()
                                    var = 0
                                    while(var<t):
                                        var += 1
                                        time.sleep(1)
                                    osc.stop()
                                    plotData.plot(osc, name='{}.csv'.format(window['filename'].get().strip(".csv")))
                                    MakeCSV.deleteTempFiles()
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
        if event in (sg.WINDOW_CLOSED, "Quit"):
            break
        if event == 'Exit':
                break
    window.close()

# Add the plot to the window



import matplotlib.pyplot as plt
import time
import os
import pandas as pd
import MakeCSV

def live_plot():
    None

def plot(osc, keepCSV=True, name=None):
    if(osc.buffer_flush_time == None):
        while(osc.collecting):
            None
        if(name == None):
            MakeCSV.makeCSV(osc,name="{}.csv".format(osc.data_thread.native_id))
        else:
            MakeCSV.makeCSV(osc,name="{}.csv".format(name))
        for files in os.listdir():
            if(name == None):
                if(files=="{}.csv".format(osc.data_thread.native_id)):
                    dataframe = pd.read_csv(files)
                    break
            else:
                if(files=="{}.csv".format(name)):
                    dataframe = pd.read_csv(files)
                    break
        fig, axs = plt.subplots(1,int((len(dataframe.columns)-1)/2))
        for i in range(len(axs)):
            axs[i].plot(dataframe.iloc[:,2*i+1], dataframe.iloc[:,2*i+2])
            axs[i].set_title("Probe {}".format(i+1))
            axs[i].set_xlabel(dataframe.columns[2*i+1].split('.')[0])
            axs[i].set_ylabel(dataframe.columns[2*i+2].split('.')[0])
        if(not keepCSV):
            os.remove("{}.csv".format(osc.data_thread.native_id))    
        plt.show()
                
def delay(i,osc):
    osc.startCollection()
    time.sleep(i)
    osc.stop()
    
if __name__ == '__main__':
    import SerialFunctions
    MakeCSV.deleteTempFiles()
    osc = SerialFunctions.Device('COM4',flush=1)
    osc.startCollection()
    time.sleep(10)
    osc.stop()
    plot(osc)
    MakeCSV.deleteTempFiles()
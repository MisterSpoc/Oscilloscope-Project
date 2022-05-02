import matplotlib.pyplot as plt
import time
import os
import pandas as pd
import MakeCSV
import threading

def plot(osc):
    if(osc.buffer_flush_time != None):
        first = True
        while(not osc.collecting):
            time.sleep(1)
        while (osc.collecting):
            i = 0
            files = list()
            for item in os.listdir():
                if item.startswith("{}_".format(osc.data_thread.native_id)):
                    files.append(item)
   
            if(len(files) > 1):
                dataframe = MakeCSV.makeCSV(osc, save=False, item=files[-1])
                if(first):
                    figs = list()
                    for i in range(int((len(dataframe.columns)-1)/2)):
                        figs.append(plt.figure())
                    # fig, axs = plt.subplots(1,int((len(dataframe.columns)-1)/2))
                    first = False
                    
                for i in range(len(figs)):
                    figs[i].plot(dataframe.iloc[:,2*i+1], dataframe.iloc[:,2*i+2])
                    
                    # if(first):
                    figs[i].set_title("Probe {}".format(i+1))
                    figs[i].set_xlabel(dataframe.columns[2*i+1].split('.')[0])
                    figs[i].set_ylabel(dataframe.columns[2*i+2].split('.')[0])
                plt.show()    
                time.sleep(osc.buffer_flush_time)
    else:
        while (osc.collecting):
            None
        MakeCSV.makeCSV(osc,name="{}.csv".format(osc.data_thread.native_id))
        for files in os.listdir():
            if(files=="{}.csv".format(osc.data_thread.native_id)):
                dataframe = pd.read_csv(files)
                break
        fig, axs = plt.subplots(1,int((len(dataframe.columns)-1)/2))
        for i in range(len(axs)):
            axs[i].plot(dataframe.iloc[:,2*i+1], dataframe.iloc[:,2*i+2])
            axs[i].set_title("Probe {}".format(i+1))
            axs[i].set_xlabel(dataframe.columns[2*i+1].split('.')[0])
            axs[i].set_ylabel(dataframe.columns[2*i+2].split('.')[0])
            
        plt.show()
                
def delay(i,osc):
    osc.startCollection()
    time.sleep(i)
    osc.stop()
    
if __name__ == '__main__':
    import SerialFunctions
    osc = SerialFunctions.Device('/dev/cu.usbmodem101', flush=1)
    t=threading.Thread(target=delay, args=(10,osc))
    t.start()
    plot(osc)
    t.join()
    MakeCSV.deleteTempFiles()
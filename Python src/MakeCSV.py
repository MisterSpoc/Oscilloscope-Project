import os
import pandas as pd

def makeCSV(oscilloscope, name=None, save=True, item=None):
    # converts data in temp files to csv using pandas
    # follow conventions in output_example.txt for proper usage
    # name denotes desired save file name
    # if save set to False, will not save as a CSV, will instead return pandas dataframe used to make CSV
    
    first = True
    headers = []
    data = []
    counter=0
    
    if(save):
        f = os.listdir()
        for item in f:
            if item.startswith("{}_".format(oscilloscope.data_thread.native_id)):
                with open(item) as i:
                    for line in i:
                        if (first):
                            if(counter<5):
                                counter+=1
                            else:
                                first = False
                                t = line.split(";")
                                for entry in t:
                                    headers.append("Time({})".format(entry.split(", ")[1].split(":")[0]))
                                    headers.append(entry.split(", ")[2].split(":")[0])
                                print(headers)
                        else:
                            t = line.split(";")
                            temp_list = list()
                            for entry in range(len(t)):
                                temp_list.append(t[entry].split(", ")[1].split(":")[1])
                                temp_list.append(float(t[entry].split(", ")[2].split(":")[1].strip("\n")))
                            data.append(temp_list)
    else:
        with open(item) as i:
            for line in i:
                t = line.split(";")
                temp_list = list()
                for entry in t:
                    if(first):
                        headers.append("Time({})".format(entry.split(", ")[1].split(":")[0]))
                        headers.append(entry.split(", ")[2].split(":")[0])
                for entry in range(len(t)):
                    temp_list.append(t[entry].split(", ")[1].split(":")[1])
                    temp_list.append(float(t[entry].split(", ")[2].split(":")[1].strip("\n")))
                first=False
                data.append(temp_list)
                
        
    data_to_save = pd.DataFrame(data, columns=headers)
    if(save):
        if(name == None):
            name = "{}.csv".format(oscilloscope.data_thread.native_id)
        try:
            data_to_save.to_csv(name)
            name = "{}.csv".format(oscilloscope.data_thread.native_id)
            
        except:
            name = "{}.csv".format(oscilloscope.data_thread.native_id)
            data_to_save.to_csv(name)
            
    else:
        return data_to_save

                        
    
def deleteTempFiles():
    # deletes all temp files associated with oscilloscope
    for item in os.listdir():
        if item.endswith(".temp"):
            os.remove(item)

if __name__ == '__main__':
    from SerialFunctions import *
    osc1 = Device(flush=0.33)
    osc1.port_name = 'COM4'
    
    osc1.startCollection()
    time.sleep(15)
    osc1.stop()
    makeCSV(osc1)
    deleteTempFiles()
    None
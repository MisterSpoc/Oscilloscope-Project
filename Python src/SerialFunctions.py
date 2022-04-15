import serial
from serial.tools import list_ports
import threading
import time

def getPorts():
    """Return list containing com ports

    Returns:
        list: list of com port identifiers
    """
    return list_ports.comports()

class Device:
    """Device Object (corresponds to one device communicating through serial)
        Create a new object for every connected oscilloscope.
    """
    
    def __init__(self, port = '', baud = 57600, time = 2, flush = None):
        """Creates Device Object

        Args:
            port (str, optional): port name. Defaults to ''
            baud (int, optional): baud rate. Defaults to 57600.
            time (int, optional): time till timeout. Defaults to 1.
            flush (float, optional): time between buffer flushes to file. If None, writes entire buffer
                to file when port closes. Defaults to None
        """
        self.port_name = port
        self.baud_rate = baud
        self.timeout = time
        self.end = False
        self.data_buffer = []
        self.buffer_flush_time = flush
        self.__reference_time = 0
        self.oscilloscope = serial.Serial()
        self.data_thread = threading.Thread(target=self.__openDataStream)
        self.lock = threading.Lock()
        # self.oscilloscope.set_buffer_size(rx_size=1048576) # set buffer size to 1 MiB Windows Only
    
    def __openPort(self):
        """Opens a serial port with set variables
        """
        self.oscilloscope.port = self.port_name
        self.oscilloscope.baudrate = self.baud_rate
        self.oscilloscope.timeout = self.timeout
        
        if (not self.oscilloscope.is_open):
            self.oscilloscope.open()
        else:
            print("Port could not be opened")
        
    def __closePort(self):
        """Closes serial port
        """
        self.oscilloscope.close()
        
    def __getData(self):
        """Returns a single line of serial data (breaks on '\n' character)

        Returns:
            str: decoded serial data as string
        """
        return (self.oscilloscope.readline())
    
    def __openDataStream(self):
        """Opens and actively collects data from port. Flushes collected data to temp file every
        buffer_flush_time seconds
        """
        self.__openPort()
        time.sleep(3)
        self.oscilloscope.reset_input_buffer()    
        self.__reference_time = time.time()
        while(True):
            self.data_buffer.append(self.__getData().decode('utf-8').replace('\r',''))
            
            if(self.buffer_flush_time is not None):
                if(time.time()-self.__reference_time > self.buffer_flush_time):
                    self.flush()
                    self.__reference_time = time.time()
                
            if(self.end):
                if(len(self.data_buffer) > 0):
                    self.flush()
                break
        self.__closePort()
        
    def flush(self):
        """FLush buffer to temp file
        """
        name_str = '{}_{}.temp'.format(self.data_thread.native_id,int(time.time()*1000))

        f = open(name_str,"x")
        for i in self.data_buffer:
            f.write(i)
        f.close()
        self.data_buffer = []
        
    def startCollection(self):
        self.data_thread.start()
    
    def stop(self):
        self.end = True
        self.data_thread.join()
    

            
if __name__ == '__main__':
    osc1 = Device(flush=0.33)
    osc1.port_name = 'COM4'
    
    osc1.startCollection()
    time.sleep(10)
    osc1.stop()
    
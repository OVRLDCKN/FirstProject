#File with Classes, that make my life easier xD
#Importing Modules
import time
import pickle
import socket

#Time Class, that gives me info about the current time
class class_time:
    def __init__(self,year,month,day,hour,minute,second):
        self.status_values = []
        if year == 1:
            self.status_values.append("year")
        if month == 1:
            self.status_values.append("month")
        if day == 1:
            self.status_values.append("day")
        if hour == 1:
            self.status_values.append("hour")
        if minute == 1:
            self.status_values.append("minute")
        if second == 1:
            self.status_values.append("second")
    def get(self):
        for i in self.status_values:
            if i == "year":
                self.status_values[self.status_values.index(i)] = time.localtime().tm_year
            if i == "month":
                self.status_values[self.status_values.index(i)] = time.localtime().tm_mon
            if i == "day":
                self.status_values[self.status_values.index(i)] = time.localtime().tm_mday
            if i == "hour":
                self.status_values[self.status_values.index(i)] = time.localtime().tm_hour
            if i == "minute":
                self.status_values[self.status_values.index(i)] = time.localtime().tm_min
            if i == "second":
                self.status_values[self.status_values.index(i)] = time.localtime().tm_sec
        locallist = []
        for i in self.status_values:
            locallist.append(i)
        return locallist

#Read and Write Class, that lets me store variables in a specified file, and get the value from the variable in the file afterwards
class class_read_write:
    def __init__(self,file):
        self.file = file
    def read(self):
        with open(self.file, "rb") as self.FILE:
            data = pickle.load(self.FILE)
        return data
    def write(self,var):
        with open(self.file, "wb") as self.FILE:
            pickle.dump(var, self.FILE)

#Server class, that lets me start a server and a client, and that lets me send and receive variables
class class_server:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def server_start(self):
        self.socket.bind((self.ip,self.port))
    def client_start(self):
        self.socket.connect((self.ip,self.port))
    def server_connect_client(self):
        self.socket.listen(5)
        (self.client_socket,(self.client_ip,self.client_port)) = self.socket.accept()
    def server_send_var(self,var):
        BINFILE = class_read_write("msg.txt")
        BINFILE.write(var)
        with open("msg.txt","r") as FILE:
            var_encoded = FILE.read()
        self.client_socket.send(var_encoded.encode())
    def server_receive_var(self):
        with open("msg.txt","w") as FILE:
            FILE.write(self.client_socket.recv(2048).decode())
        BINFILE = class_read_write("msg.txt")
        var = BINFILE.read()
        return var
    def client_send_var(self,var):
        BINFILE = class_read_write("msg.txt")
        BINFILE.write(var)
        with open("msg.txt", "r") as FILE:
            var_encoded = FILE.read()
        self.socket.send(var_encoded.encode())
    def client_receive_var(self):
        with open("msg.txt", "w") as FILE:
            FILE.write(self.socket.recv(2048).decode())
        BINFILE = class_read_write("msg.txt")
        variable = BINFILE.read()
        return variable
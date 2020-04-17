from tkinter import filedialog
import tkinter as tk
#from regression import *
import json
import os



def get_file_name():
    root = tk.Tk()
    fileName = filedialog.askopenfilename()
    root.withdraw()
    return fileName

def get_directory():
    '''Allows user to select a directory for analysis, retruns directory name as a string''' 
    root = tk.Tk()
    directory = filedialog.askdirectory(initialdir='.')
    root.withdraw()
    return directory
    

def get_file_info_dict(file):
    '''Return the file Info'''
    with open(file, "r") as file:
        lines = file.readlines()
    fileInfo = lines[0]
    #print(fileInfo)
    fileInfoDict = json.loads(fileInfo)
    #print(fileInfoDict)
    return fileInfoDict

def get_data_list(directory):
    '''returns a list of txt files in a directory: "directory"'''
    files = os.listdir(directory)
    dataFiles = []
    i = 0
    
    for file in files:
        if 'txt' in file and file != 'TemporaryLog.txt':
            i += 1
            dataFiles.append(file)
    return sorted(dataFiles)
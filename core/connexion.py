import pandas as pd
import sys
import os
import video as vd

sys.path.insert(0,'../ui')  # insert a directory (option 0)

import browserFileWindow as br
import signalsWindow as sw

class Connexion :

  #construtor
  def __init__ (self, filename_video, filename_csv) :
    self.filename_video = filename_video
    self.filename_csv = filename_csv
    self.checkAndLoadPandasFile()
    self.checkAndLoadVideoFile()
    #self.sw = sw.SignalsWindow()


  #check the file format (.csv, .xls, etc) and if this exits
  def checkAndLoadPandasFile (self) :
    if ".csv" in self.filename_csv :
      self.data_csv = pd.read_csv(self.filename_csv)
      print("File successfully loaded")
      return 
    if ".xls" in self.filename_csv :
      self.data_csv = pd.read_excel(self.filename_csv)
      print("File successfully loaded")
      return
    if ".xlsx" in self.filename_csv :
      self.data_csv = pd.read_excel(self.filename_csv)
      print("File successfully loaded")
      return
    print("Illegal Format for the CSV file or format not supported")
    exit(1)

  
  #check if the Video file source exists and if its format is supported
  def checkAndLoadVideoFile (self) :
    if ".mp4" in self.filename_video or ".mov" in self.filename_video or ".mwv" in self.filename_video or ".flv" in self.filename_video or ".avi" in self.filename_video or ".mkv" in self.filename_video :
      if os.path.exists(self.filename_video) :
        print("Video successfully loaded")
        #self.data_video = vd.Video(self.filename_video)
      return 
    print("Illegal Format for the CSV file or format not supported")
    exit(1)

  
  #getter for the filename_video and filename_csv file
  def getterFilenames (self) :
    return self.filename_video, self.filename_csv


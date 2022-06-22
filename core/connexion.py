import pandas as pd
import os

class Connexion :

  def __init__(self, filename_video, filename_csv):
      self.filename_video = filename_video
      self.filename_csv = filename_csv
      self.checkAndLoadPandasFile()
      self.checkAndLoadVideoFile()


  def checkAndLoadPandasFile(self):
      if os.path.exists(self.filename_csv) :
          print("File CSV successfully founded")
          if ".csv" in self.filename_csv:
              self.data_csv = pd.read_csv(self.filename_csv)
              print("File CSV successfully loaded")
              return
          if ".xls" in self.filename_csv:
              self.data_csv = pd.read_excel(self.filename_csv)
              print("File CSV successfully loaded")
              return
          if ".xlsx" in self.filename_csv:
              self.data_csv = pd.read_excel(self.filename_csv)
              print("File CSV successfully loaded")
              return
          print("Illegal Format for the CSV file or format not supported")
      else :
          print("Couldn't open " + self.filename_csv + ": no such file or directory")
      exit(1)


  # check if the Video file source exists and if its format is supported
  def checkAndLoadVideoFile(self):
      if os.path.exists(self.filename_video):
          print("Video successfully founded")
          if ".mp4" in self.filename_video or ".mov" in self.filename_video or ".mwv" in self.filename_video or ".flv" in self.filename_video or ".avi" in self.filename_video or ".mkv" in self.filename_video:
              print("Video successfully loaded")
              # self.data_video = vd.Video(self.filename_video)
              return
          print("Illegal Format for the video or format not supported")
      else :
          print("Couldn't open " + self.filename_video + ": no such file or directory")
      exit(1)

  # getter for the filename_video and filename_csv file
  def getterFilenames(self):
      return self.filename_video, self.filename_csv
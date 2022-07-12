# Video Desktop App

A Desktop app for Valeo Vision.

## Pre-requisites

The project is written in ```python 3```, so if you have another version, upload it [here](https://www.python.org/downloads/)

The project uses differents libraries like ```Tkinter```,  ```pandas```, ```opencv```, ```matplotlib``` and ```PILL```so we need install them by :
> with pip3 method
```
pip3 install pandas tk opencv-python matplotlib pillow
```
> For conda users
```
conda install pandas tk opencv-python matplotlib pillow
```

## Run the Project

First, we need to clone the repository
```
git clone https://github.com/napoknot21/video-desktop-app.git
```
We enter to the cloned directory
```
cd video-desktop-app
```
We run ```launcher.py``` file 
```
python3 launcher.py
```

## How to use it ?
This desktop app was created in order to automate the labeling of the simulation videos

### First steps 
When we run the ```launcher.py```, we'll have the *browser window*.

![browser-window](src/ui/.images/video-welcome.PNG)

We have to select a *video* file (the simulation video) and a *CSV* file (the data).

Once selected, then we can start !

Then, we have to select all signals to work with (from th csv file) so make sure that select the goog csv file ! 

We're supposed to have a window like this :

![signals-window](src/ui/.images/signalsWindow.PNG)

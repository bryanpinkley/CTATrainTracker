# CTA Train Tracker
CTA Train Tracker is a Python application that displays the arrival times for Chicago's "L" trains. 🚆

![Sample Display](https://media.giphy.com/media/rGlihl6qJ5ZeS7fOFi/giphy.gif)

## Overview
This program uses Python's Tkinter package to display the current arrival times for a specified station. "main.py" creates the Tkinter display, calls the CTA Train Tracker API, and refreshes the data. "train.py" has a class "Train" so that every time the CTA API is called, data for each train is stored in a Train object.

The following constants are declared at the beginning of "main.py" and can be changed:
- Station `STOP_ID`
- Number of trains displayed `NUMBER_OF_TRAINS`
- Time between refreshes, in seconds `REFRESH`

To use this program, you will have to obtain a [CTA API Key](https://www.transitchicago.com/developers/traintrackerapply/). 

## Reference
The documentation for CTA's Train Tracker API can be found [here](https://www.transitchicago.com/developers/ttdocs/). Stop ID's for a station can be found in Appendix B of this documentation.

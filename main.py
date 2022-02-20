# TODO: change color of background depending on line
# TODO: Bus

from apikey import key
import requests
from train import Train
from tkinter import *
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

RED = "#c60c30"
GREY = "#565a5c"
FONT_NAME = "Arial"
STOP_ID = "41420"  # Addison Red Line Parent Station
NUMBER_OF_TRAINS = 6  # Total number of trains to get data for
REFRESH = 3  # Refresh time in seconds
# train_counter = 1  # Starting at 1, keeps track of the trains to display
max_train = 0  # Keeps track of the total number of trains from the data
train_list = []  # List to hold Train objects
station_name = ""
route_name = ""
timer = None
train_counter = 0


# ------------- GET TRAIN DATA ------------- #
def get_data():
    global max_train, train_list, station_name, route_name, train_counter
    base_url = f"http://lapi.transitchicago.com/api/1.0/ttarrivals.aspx?key={key}&max={NUMBER_OF_TRAINS}&mapid=" \
               f"{STOP_ID}&outputType=JSON"
    station_data = requests.get(base_url).json()
    station_name = station_data["ctatt"]["eta"][0]["staNm"]
    route_name = station_data["ctatt"]["eta"][0]["rt"]

    # Create Train objects from data
    for count in range(NUMBER_OF_TRAINS):
        try:
            train_data = station_data["ctatt"]["eta"][count]
            new_train = Train(train_data)
            train_list.append(new_train)
            # print("Adding New Train")
        except IndexError:
            # print("Maximum number of trains reached.")
            break
    max_train = len(train_list)
    print(f"Obtained new data. {max_train} trains.")
    train_counter = 0
    refresh()


# ------------- REFRESH DISPLAY ------------- #
def refresh():
    global timer, train_counter
    print(f"Train Counter: {train_counter}")
    print(f"Max Trains: {max_train}")
    if train_counter < max_train:
        train_1 = train_counter
        train_2 = train_counter+1
        title_label.config(text=f"Next 'L' service at {station_name}")
        number_label_1.config(text=train_1+1)
        train_dest_label_1.config(text=train_list[train_1].destination)
        train_arr_label_1.config(text=train_list[train_1].time_until)
        print(f"Train {train_1+1} Display Updated. {train_list[train_1].destination} {train_list[train_1].time_until} min")
        if train_2 < max_train:
            number_label_2.config(text=train_2+1)
            train_dest_label_2.config(text=train_list[train_2].destination)
            train_arr_label_2.config(text=train_list[train_2].time_until)
            train_min_label_2.config(text="min")
            print(f"Train {train_2+1} Display Updated {train_list[train_2].destination} {train_list[train_2].time_until} min")
        else:
            number_label_2.config(text="")
            train_dest_label_2.config(text="")
            train_arr_label_2.config(text="")
            train_min_label_2.config(text="")
            print(f"No Train {train_2+1}")
        train_counter += 2
        timer = window.after(REFRESH*1000, refresh)
    else:
        print("End of trains. Getting new data.")
        train_list.clear()
        timer = window.after(1, get_data)


# ------------- UI SETUP ------------- #
window = Tk()
window.title("CTA Train Tracker")
window.config(bg=GREY)

title_label = Label(text=f"Next 'L' service at station_name", font=(FONT_NAME, 15, "normal"), fg="white", bg=GREY,
                    padx=5, pady=5)
title_label.grid(column=2, row=1, sticky="w")

number_label_1 = Label(text="1", font=(FONT_NAME, 15, "normal"), fg="white", bg=GREY, padx=5)
number_label_1.grid(column=1, row=2, sticky="n")

number_label_2 = Label(text="2", font=(FONT_NAME, 15, "normal"), fg="white", bg=GREY, padx=5)
number_label_2.grid(column=1, row=3, sticky="n")

train_dest_label_1 = Label(text="DEST_LABEL_1", font=(FONT_NAME, 40, "bold"), fg="white", bg=RED, width=15,
                           anchor="w")
train_dest_label_1.grid(column=2, row=2)

train_dest_label_2 = Label(text="DEST_LABEL_2", font=(FONT_NAME, 40, "bold"), fg="white", bg=RED, width=15, anchor="w")
train_dest_label_2.grid(column=2, row=3)

train_arr_label_1 = Label(text="X", font=(FONT_NAME, 40, "bold"), fg="white", bg=RED, width=2, padx=5)
train_arr_label_1.grid(column=3, row=2)

train_arr_label_2 = Label(text="X", font=(FONT_NAME, 40, "bold"), fg="white", bg=RED, width=2, padx=5)
train_arr_label_2.grid(column=3, row=3)

train_min_label_1 = Label(text="min", font=(FONT_NAME, 40, "normal"), fg="white", bg=RED, width=3)
train_min_label_1.grid(column=4, row=2, sticky=W+E+N+S)

train_min_label_2 = Label(text="min", font=(FONT_NAME, 40, "normal"), fg="white", bg=RED, width=3)
train_min_label_2.grid(column=4, row=3, sticky=W+E+N+S)

timer = window.after(1000, get_data)

window.mainloop()

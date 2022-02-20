from datetime import datetime
import math


class Train:
    def __init__(self, train_data):
        self.destination = train_data["destNm"]
        self.arrival_time = train_data["arrT"]
        self.current_time = train_data["prdt"]
        self.is_app = train_data["isApp"]
        self.is_delay = train_data["isDly"]
        self.arrival_datetime = ""
        self.current_datetime = ""
        self.time_until = ""
        self.time_difference()

    def time_difference(self):
        self.arrival_datetime = datetime.strptime(self.arrival_time, "%Y-%m-%dT%H:%M:%S")
        self.current_datetime = datetime.strptime(self.current_time, "%Y-%m-%dT%H:%M:%S")
        self.time_until = math.floor(((self.arrival_datetime - self.current_datetime).total_seconds())/60)
        if self.is_app == 1:
            self.time_until = "Due"
        if self.is_delay == 1:
            self.time_until = "Delay"

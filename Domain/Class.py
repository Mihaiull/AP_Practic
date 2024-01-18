class Measurement:
    def __init__(self, pressure:float, hour_of_day:int, temperature:int):
        self.__pressure = pressure
        self.__hour_of_day = hour_of_day
        self.__temperature = temperature
    
    def get_pressure(self):
        return self.__pressure
    def get_hour_of_day(self):
        return self.__hour_of_day
    def get_temperature(self):
        return self.__temperature
    
    def __str__(self):
        return f"Pressure: {self.__pressure} Hour of day: {self.__hour_of_day} Temperature: {self.__temperature}"
    __repr__=__str__
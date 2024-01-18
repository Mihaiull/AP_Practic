from Domain.Class import Measurement

class Repo:
    '''
    Contains a list of measurements
    '''
    def __init__(self):
        self.__list=[]

    '''
    Function that adds a measurement to the list
    Input: pressure, hour, temperature
    Output: -
    '''
    def add(self, pressure, hour, temperature):
        if pressure<0 or pressure>10 or temperature<0 or temperature>100 or hour<0 or hour>23:
            raise ValueError('DATA NOT VALID')
        self.__list.append(Measurement(pressure, hour, temperature))
    '''
    Function that returns the list of measurements higher than a given value
    Input: val
    Output: lst
    '''
    def getpress(self, val):
        lst=[]
        for elem in self.__list:
            if elem.get_pressure() > val:
                lst.append(elem)
        return lst
    '''
    Function that returns the average pressure and temperature for a given hour
    Input: hour
    Output: suma
    '''
    def getavg(self, hour):
        lst=[]
        for elem in self.__list:
            if elem.get_hour_of_day() == hour:
                lst.append(elem.get_pressure())
        suma = 0
        for elem in lst:
            suma= suma + elem
        suma = suma / len(lst)

        lst2=[]
        for elem in self.__list:
            if elem.get_hour_of_day() == hour:
                lst2.append(elem.get_temperature())
        suma2 = 0
        for elem in lst2:
            suma2= suma2 + elem
        suma2 = suma2 / len(lst2)
        lst = ['Pressure: ', suma,'Temperature: ', suma2]

        return lst
    '''
    niste enteruri mai fancy sa nu fie totu pe o linie la print
    '''
    def __str__(self):
        return '\n'.join([str(elem) for elem in self.__list])
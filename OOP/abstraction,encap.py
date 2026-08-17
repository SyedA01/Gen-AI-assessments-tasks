from abc import ABC, abstractmethod


# ABSTRACTION
class IRCTC(ABC):

    def __init__(self, passenger_name, balance):
        self.__passenger_name = passenger_name    # DATA HIDING
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance

    @abstractmethod
    def book_ticket(self, train):
        pass


# DYNAMIC BINDING / POLYMORPHISM
class RailOne(IRCTC):

    def book_ticket(self, train):
        print(f"Booking {train} ticket through RailOne")


class ConfirmTkt(IRCTC):

    def book_ticket(self, train):
        print(f"Booking {train} ticket through ConfirmTkt")


# Objects
passenger = RailOne("Syed", 5000)

passenger.book_ticket("Chennai Express")
print("Passenger Balance:", passenger.get_balance())


passenger = ConfirmTkt("Syed", 5000)

passenger.book_ticket("Pandian Express")
print("Passenger Balance:", passenger.get_balance())
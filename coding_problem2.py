from datetime import date
from typing import List

class Address:
    def __init__(self, city: str, state: str):
        self.city = city
        self.state = state

    def __repr__(self):
        return f"Address(city={self.city}, state={self.state})"


class ImmutableEmployee:
    def __init__(self, name: str, emp_id: str, date_of_joining: date, addresses: List[Address]):
        self._name = name
        self._emp_id = emp_id
        self._date_of_joining = date_of_joining
        self._addresses = [Address(addr.city, addr.state) for addr in addresses]

    @property
    def name(self):
        return self._name

    @property
    def emp_id(self):
        return self._emp_id

    @property
    def date_of_joining(self):
        return self._date_of_joining

    @property
    def addresses(self):
        return [Address(addr.city, addr.state) for addr in self._addresses]

address1 = Address("Hyderabad", "Telangana")
address2 = Address("Bangalore", "Karnataka")
employee = ImmutableEmployee("Vineeth", "12345", date(2022, 5, 10), [address1, address2])

print(f"Name: {employee.name}")
print(f"Employee ID: {employee.emp_id}")
print(f"Date of Joining: {employee.date_of_joining}")
print(f"Addresses: {employee.addresses}")

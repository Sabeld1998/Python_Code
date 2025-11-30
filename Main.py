from Address import Address 
from Employee import Employee
from ProductionWorker import ProductionWorker
from ShiftSupervisor import ShiftSupervisor

def main():
    address = Address('777 Barth', 'Richland', 'WA', '99352')
    employee0 = ShiftSupervisor('Sabel', '001', address, 50000, 10000)
    print(employee0)

if __name__ == '__main__':
    main()
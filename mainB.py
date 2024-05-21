import random

class BinarySearchTree:
    def __init__(self, passenger_no, name):
        self.passenger_no = passenger_no
        self.name = name
        self.left = None
        self.right = None

class BusReservationSystem:
    def __init__(self):
        self.root = None
        self.bus_seat = [[0] * 9 for _ in range(33)]
        self.random_num = random.randint(1, 10000)

    def reservation_info(self, passenger_no):
        return self._reservation_info(self.root, passenger_no)

    def _reservation_info(self, root, passenger_no):
        if root is None:
            return None
        if root.passenger_no == passenger_no:
            return root
        elif root.passenger_no > passenger_no:
            return self._reservation_info(root.left, passenger_no)
        else:
            return self._reservation_info(root.right, passenger_no)

    def insert(self, passenger_no, name):
        self.root = self._insert(self.root, passenger_no, name)

    def _insert(self, root, passenger_no, name):
        if root is None:
            return BinarySearchTree(passenger_no, name)
        if passenger_no < root.passenger_no:
            root.left = self._insert(root.left, passenger_no, name)
        elif passenger_no > root.passenger_no:
            root.right = self._insert(root.right, passenger_no, name)
        return root

    def cost(self, passenger_no):
        bus_cost = passenger_no // 1000 % 3
        if bus_cost == 1:
            return 2000
        elif bus_cost == 2:
            return 1000
        elif bus_cost == 0:
            return 1500
        else:
            return 0

    def status(self):
        bus_num = int(input("ENTER YOUR BUS NUMBER : "))
        if bus_num <= 0 or bus_num >= 10:
            print("PLEASE ENTER CORRECT BUS NUMBER !!")
            return
        self.display_seat(self.bus_seat[bus_num])

    def display_seat(self, bus):
        for i in range(1, 33):
            seat_status = "EMPTY" if bus[i] == 0 else "BOOKED"
            print(f"{i:02d} . {seat_status}", end="         ")
            if i % 4 == 0:
                print()

    def bus_lists(self):
        print("-------------------------------------------------------------------------------------------------")
        print("Bus.No\tName\t\t\t\tDestinations  \t\tCharges  \t\tTime")
        print("-------------------------------------------------------------------------------------------------")
        print("1\tSaintmartin Paribahan     \tDhaka to Cox's Bazar  \tTK.2000     \t\t10:00  PM")
        print("2\tAK_Travels                \tDhaka To Syleth       \tTk.1000     \t\t01:30  PM")
        print("3\tEna Paribahan             \tDhaka To Kuakata      \tTk.1500     \t\t03:50  PM")
        print("4\tSuper Deluxe              \tDhaka To Dinajpur     \tTk.2000     \t\t07:00  AM")
        print("5\tSkyLine                   \tDhaka To Khulna       \tTk.1000     \t\t12:05  AM")
        print("6\tRoyal Express             \tDhaka to Chuyadanga   \tTk.1500     \t\t09:30  AM")
        print("7\tShohag Paribahan          \tDhaka To Benapole     \tTk.2000     \t\t11:00  PM")
        print("8\tHanif Paribahan           \tDhaka To Bagura       \tTk.1000     \t\t08:15  AM")
        print("9\tSoudia Paribahan          \tDhaka To Chottogram   \tTk.1000     \t\t07:00  PM")
        print("\n   PRESS 'ENTER' KEY TO CONTINUE ")
        input()

    def cancel(self, random_num):
        reservation_no = int(input("ENTER YOUR RESERVATION NUMBER : "))
        if reservation_no == random_num:
            confirm = input(f"RESERVATION NUMBER IS IT CORRECT ? {reservation_no} \nENTER (Y/N) : ")
            if confirm.lower() == 'y':
                choice = int(input("ENTER THE BUS NUMBER: "))
                seat_cancel = int(input("HOW MANY SEATS DO WANT TO CANCEL : "))
                for _ in range(seat_cancel):
                    seat_number = int(input("ENTER THE SEAT NUMBER: "))
                    self.bus_seat[choice][seat_number] = 0
                print("\n\nYOUR RESERVATION HAS BEEN CANCEL !!\n\n")
                print("PRESS 'ENTER' KEY TO CONTINUE ")
                input()
                self.display_seat(self.bus_seat[choice])
            else:
                print("\nYOUR RESERVATION CANCELATION HAS BEEN DENIED\n")
        else:
            print("\nNOT FOUND!! ENTER THE CORRECT RESERVATION NUMBER\n")

    def main_menu(self, random_num):
        while True:
            print("\n\n====================================================================\n\n")
            print("\t\t\tBUS RESERVATION\t\t")
            print("\n\n=====================================================================\n")
            print("====================  MAIN MENU =====================\n\n")
            print("   [1] VIEW BUS LIST \n\n")
            print("   [2] BOOK TICKETS\n\n")
            print("   [3] CANCEL BOOKING\n\n")
            print("   [4] BUSES SEATS INFO\n\n")
            print("   [5] RESERVATION INFO\n\n")
            print("   [6] EXIT\n")
            print("\n=====================================================\n")
            num = int(input("ENTER YOUR CHOICE: "))
            if num == 1:
                self.bus_lists()
            elif num == 2:
                self.bus_lists()
                while True:
                    choice = int(input("CHOOSE YOUR BUS  : "))
                    if choice <= 0 or choice > 9:
                        print("ENTER VALID BUS NUMBER !! ")
                        continue
                    print()
                    self.display_seat(self.bus_seat[choice])
                    while True:
                        seats = int(input("NO. OF SEATS YOU NEED TO BOOK : "))
                        if seats <= 0:
                            print("ENTER VALID SEAT NUMBER!!")
                            continue
                        elif seats > 32:
                            print("ENTER VALID SEAT NUMBER WE HAVE ONLY 32 SEATS IN A BUS !!")
                            continue
                        for _ in range(seats):
                            while True:
                                seat_number = int(input("ENTER THE SEAT NUMBER: "))
                                if seat_number <= 0:
                                    print("ENTER VALID SEAT NUMBER!!")
                                    continue
                                elif seat_number > 32:
                                    print("ENTER VALID SEAT NUMBER WE HAVE ONLY 32 SEATS IN A BUS !!")
                                    continue
                                break
                            cust_id = choice * 1000 + seat_number
                            self.bus_seat[choice][seat_number] = 1

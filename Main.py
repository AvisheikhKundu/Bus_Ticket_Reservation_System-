
#Author@AvisheikhKundu


import random

class Passenger:
    def __init__(self, cust_id, name):
        self.cust_id = cust_id
        self.name = name
        self.left = None
        self.right = None

class BusTicketManagementSystem:
    def __init__(self):
        self.root = None
        self.bus_seat = [[0]*33 for _ in range(10)]

    def green_color(self):
        print("\033[1;32m", end="")

    def reset_color(self):
        print("\033[0m", end="")

    def login(self):
        user_name = "user"
        password = "Avisheikh001"
        match_user = input("UserName: ")
        match_pass = input("PassWord: ")

        if match_user != user_name or match_pass != password:
            self.green_color()
            print("INVALID DETAILS TRY AGAIN...")
            self.reset_color()
            return False
        else:
            self.green_color()
            print("LOGGED IN SUCCESSFULLY...")
            self.reset_color()
            return True

    def bus_lists(self):
        self.green_color()
        print("-------------------------------------------------------------------------------------------------")
        print("Bus.No\tName\t\t\t\tDestinations  \t\tCharges  \t\tTime")
        print("-------------------------------------------------------------------------------------------------")
        self.reset_color()
        print("1\tSaintmartin Paribahan     \tDhaka to Cox's Bazar  \tTK.2000     \t\t10:00  PM")
        print("2\tAK_Travels                \tDhaka To Syleth       \tTk.1000     \t\t01:30  PM")
        print("3\tEna Paribahan             \tDhaka To Kuakata      \tTk.1500     \t\t03:50  PM")
        print("4\tSuper Deluxe              \tDhaka To Dinajpur     \tTk.2000     \t\t07:00  AM")
        print("5\tSkyLine                   \tDhaka To Khulna       \tTk.1000     \t\t12:05  AM")
        print("6\tRoyal Express             \tDhaka to Chuyadanga   \tTk.1500     \t\t09:30  AM")
        print("7\tShohag Paribahan          \tDhaka To Benapole     \tTk.2000     \t\t11:00  PM")
        print("8\tHanif Paribahan           \tDhaka To Bagura       \tTk.1000     \t\t08:15  AM")
        print("9\tSoudia Paribahan          \tDhaka To Chottogram   \tTk.1000     \t\t07:00  PM")

    def display_seat(self, bus):
        for i in range(1, 33):
            self.green_color()
            print(f"{i:02d} .", end="")
            self.reset_color()
            if bus[i] == 0:
                print("EMPTY ", end="")
            else:
                print("BOOKED", end="")
            print("         ", end="")
            if i % 4 == 0:
                print()

    def reservation_info(self, root, cust_id):
        current = root
        while current:
            if current.cust_id == cust_id:
                self.green_color()
                print("\n-----------------------------------------------------------------")
                print(f"||              NAME: {current.name:10}                               ||")
                print(f"||              CUSTOMER ID: {current.cust_id}                              ||")
                print(f"||              BUS NUMBER: {current.cust_id // 1000}                                  ||")
                print(f"||              SEAT NUMBER: {current.cust_id % 100}                                 ||")
                print(f"||              TICKET COST: Tk.{self.cost(current)}                             ||")
                print("-----------------------------------------------------------------")
                self.reset_color()
                input("Press any key to continue...")
                return
            elif current.cust_id > cust_id:
                current = current.left
            else:
                current = current.right
        print("Customer ID not found.")

    def insert(self, root, cust_id, name):
        if root is None:
            return Passenger(cust_id, name)
        else:
            if cust_id < root.cust_id:
                root.left = self.insert(root.left, cust_id, name)
            else:
                root.right = self.insert(root.right, cust_id, name)
        return root

    def cancel(self, random_num):
        while True:
            try:
                reservation_no = int(input("\nENTER YOUR RESERVATION NUMBER: "))
                break
            except ValueError:
                print("Please enter a valid number.")

        if reservation_no == random_num:
            c = input("RESERVATION NUMBER IS IT CORRECT? (Y/N): ")
            if c.lower() == 'y':
                while True:
                    try:
                        choice = int(input("ENTER THE BUS NUMBER: "))
                        break
                    except ValueError:
                        print("Please enter a valid number.")

                while True:
                    try:
                        seat_cancel = int(input("HOW MANY SEATS DO YOU WANT TO CANCEL: "))
                        break
                    except ValueError:
                        print("Please enter a valid number.")

                for _ in range(seat_cancel):
                    while True:
                        try:
                            seat_number = int(input("ENTER THE SEAT NUMBER: "))
                            break
                        except ValueError:
                            print("Please enter a valid number.")

                    self.bus_seat[choice][seat_number] = 0

                print("\nYOUR RESERVATION HAS BEEN CANCELLED!!")
                input("Press 'Enter' key to continue...")
                self.display_seat(self.bus_seat[choice])
            else:
                print("YOUR RESERVATION CANCELLATION HAS BEEN DENIED.")
        else:
            print("NOT FOUND!! ENTER THE CORRECT RESERVATION NUMBER")

    def cost(self, passenger):
        bus_cost = passenger.cust_id // 1000
        return {1: 2000, 2: 1000, 0: 1500}.get(bus_cost % 3, 0)

    def status(self):
        self.bus_lists()
        while True:
            try:
                bus_num = int(input("\nENTER YOUR BUS NUMBER: "))
                break
            except ValueError:
                print("Please enter a valid number.")

        if bus_num <= 0 or bus_num >= 10:
            self.green_color()
            print("PLEASE ENTER CORRECT BUS NUMBER!!")
            self.reset_color()
        else:
            self.display_seat(self.bus_seat[bus_num])
            input("Press 'Enter' key to continue...")

    def main(self):
        random_num = random.randint(1000, 9999)
        if not self.login():
            return

        while True:
            print("\n\n====================================================================\n")
            self.green_color()
            print("\t\t\tBUS RESERVATION")
            self.reset_color()
            print("\n\n=====================================================================")
            print("\n====================")
            self.green_color()
            print("  MAIN MENU  ")
            self.reset_color()
            print("=====================\n")
            print("   [1] VIEW BUS LIST")
            print("   [2] BOOK TICKETS")
            print("   [3] CANCEL BOOKING")
            print("   [4] BUSES SEATS INFO")
            print("   [5] RESERVATION INFO")
            print("   [6] EXIT")
            print("\n=====================================================")
            try:
                choice = int(input("ENTER YOUR CHOICE: "))
            except ValueError:
                self.green_color()
                print("INVALID INPUT CHOOSE CORRECT OPTION")
                self.reset_color()
                continue

            if choice == 1:
                self.bus_lists()
                input("Press 'Enter' key to continue...")
            elif choice == 2:
                self.bus_lists()
                while True:
                    try:
                        bus_choice = int(input("\n\nCHOOSE YOUR BUS: "))
                        if 1 <= bus_choice <= 9:
                            break
                        else:
                            self.green_color()
                            print("ENTER VALID BUS NUMBER!!")
                            self.reset_color()
                    except ValueError:
                        self.green_color()
                        print("ENTER VALID BUS NUMBER!!")
                        self.reset_color()
                self.display_seat(self.bus_seat[bus_choice])
                while True:
                    try:
                        seats = int(input("\n\nNO. OF SEATS YOU NEED TO BOOK: "))
                        if 0 < seats <= 32:
                            break
                        else:
                            self.green_color()
                            print("ENTER VALID SEAT NUMBER!!")
                            self.reset_color()
                    except ValueError:
                        self.green_color()
                        print("ENTER VALID SEAT NUMBER!!")
                        self.reset_color()
                for _ in range(seats):
                    while True:
                        try:
                            seat_number = int(input("ENTER THE SEAT NUMBER: "))
                            if 1 <= seat_number <= 32:
                                break
                            else:
                                self.green_color()
                                print("ENTER VALID SEAT NUMBER!!")
                                self.reset_color()
                        except ValueError:
                            self.green_color()
                            print("ENTER VALID SEAT NUMBER!!")
                            self.reset_color()
                    cust_id = bus_choice * 1000 + seat_number
                    name = input("ENTER THE PERSON NAME: ")
                    self.bus_seat[bus_choice][seat_number] = 1
                    self.root = self.insert(self.root, cust_id, name)
                    self.green_color()
                    print(f"YOUR CUSTOMER ID IS: {cust_id}")
                    self.reset_color()
                self.green_color()
                print(f"\nYOUR RESERVATION NUMBER IS: {random_num}")
                print("PLEASE NOTE DOWN YOUR RESERVATION NUMBER FOR CANCEL BOOKING TICKETS!!")
                self.reset_color()
                input("Press 'Enter' key to continue...")
            elif choice == 3:
                self.cancel(random_num)
            elif choice == 4:
                self.status()
            elif choice == 5:
                while True:
                    try:
                        reservation_no = int(input("ENTER YOUR RESERVATION NUMBER: "))
                        break
                    except ValueError:
                        self.green_color()
                        print("INVALID RESERVATION NUMBER!!")
                        self.reset_color()

                if reservation_no == random_num:
                    while True:
                        try:
                            cust_id = int(input("ENTER YOUR CUSTOMER ID: "))
                            break
                        except ValueError:
                            self.green_color()
                            print("INVALID CUSTOMER ID!!")
                            self.reset_color()
                    self.reservation_info(self.root, cust_id)
                else:
                    self.green_color()
                    print("INVALID RESERVATION NUMBER!!")
                    self.reset_color()
            elif choice == 6:
                break
            else:
                self.green_color()
                print("INVALID INPUT CHOOSE CORRECT OPTION")
                self.reset_color()

        self.green_color()
        print("\n\nTHANK YOU FOR USING THIS BUS RESERVATION SYSTEM")
        self.reset_color()
        input("PRESS ANY KEY TO EXIT THE PROGRAM!!")

if __name__ == "__main__":
    system = BusTicketManagementSystem()
    system.main()

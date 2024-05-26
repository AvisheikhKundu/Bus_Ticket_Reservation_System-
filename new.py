import random

class BSTNode:
    def __init__(self, passn_no, name):
        self.passn_no = passn_no
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
    
    def insert(self, root, cust_id, name):
        if root is None:
            return BSTNode(cust_id, name)
        elif cust_id < root.passn_no:
            root.left = self.insert(root.left, cust_id, name)
        else:
            root.right = self.insert(root.right, cust_id, name)
        return root

    def reservation_info(self, root, s):
        if root is None:
            return None
        
        if root.passn_no == s:
            self.green_color()
            print("\n-----------------------------------------------------------------")
            print(f"||              NAME: {root.name:10}                                           ||")
            print(f"||              CUSTOMER ID: {root.passn_no: <10}                              ||")
            print(f"||              BUS NUMBER: {root.passn_no // 1000: <10}                       ||")
            print(f"||              SEAT NUMBER: {root.passn_no % 100: <10}                        ||")
            print(f"||              TICKET COST: Tk.{self.cost(root): <10}                         ||")
            print("-----------------------------------------------------------------")
            self.reset_color()
            input("Press any key to continue...")
            return root
        elif root.passn_no > s:
            return self.reservation_info(root.left, s)
        else:
            return self.reservation_info(root.right, s)

    def display_seat(self, bus):
        for i in range(1, 33):
            self.green_color()
            print(f"{i:02d}. ", end="")
            self.reset_color()
            if bus[i] == 0:
                print("EMPTY", end=" ")
            else:
                print("BOOKED", end=" ")
            print("         ", end="")
            if i % 4 == 0:
                print()
        print()

    def login(self):
        username = "user"
        password = "Avisheikh001"

        print("\n\n=========================================================================================")
        print("\n\t\t\t\tWELCOME TO OUR BUS TERMINAL\n\n\t\t\t\t   'Have a safe Journey'")
        print("\n\n=========================================================================================\n\n")

        while True:
            match_user = input("\n\nUserName: ")
            match_pass = input("\nPassWord: ")

            if match_user == username and match_pass == password:
                print("\nLOGGED IN SUCCESSFULLY...\n")
                break
            else:
                self.green_color()
                print("\nINVALID DETAILS TRY AGAIN...\n")
                self.reset_color()

    def cost(self, node):
        bus_cost = node.passn_no // 1000
        if bus_cost % 3 == 1:
            return 2000
        elif bus_cost % 3 == 2:
            return 1000
        elif bus_cost % 3 == 0:
            return 1500
        return 0

    def status(self):
        self.bus_lists()
        while True:
            try:
                bus_num = int(input("\n\nENTER YOUR BUS NUMBER : "))
                if bus_num <= 0 or bus_num >= 10:
                    self.green_color()
                    print("\n  PLEASE ENTER CORRECT BUS NUMBER !!\n")
                    self.reset_color()
                else:
                    break
            except ValueError:
                self.green_color()
                print("\n  PLEASE ENTER A VALID NUMBER !!\n")
                self.reset_color()
        
        print()
        self.display_seat(self.bus_seat[bus_num])
        input("Press any key to continue...")

    def bus_lists(self):
        self.green_color()
        print("-------------------------------------------------------------------------------------------------")
        print("Bus.No\tName\t\t\t\tDestinations  \t\tCharges  \t\tTime")
        print("-------------------------------------------------------------------------------------------------")
        self.reset_color()
        print("1\tSaintmartin Paribahan     \tDhaka to Cox's Bazar  \tTK.2000     \t\t10:00  PM")
        print("2\tAK_Travels                \tDhaka To Sylhet       \tTk.1000     \t\t01:30  PM")
        print("3\tEna Paribahan             \tDhaka To Kuakata      \tTk.1500     \t\t03:50  PM")
        print("4\tSuper Deluxe              \tDhaka To Dinajpur     \tTk.2000     \t\t07:00  AM")
        print("5\tSkyLine                   \tDhaka To Khulna       \tTk.1000     \t\t12:05  AM")
        print("6\tRoyal Express             \tDhaka to Chuadanga    \tTk.1500     \t\t09:30  AM")
        print("7\tShohag Paribahan          \tDhaka To Benapole     \tTk.2000     \t\t11:00  PM")
        print("8\tHanif Paribahan           \tDhaka To Bogura       \tTk.1000     \t\t08:15  AM")
        print("9\tSoudia Paribahan          \tDhaka To Chattogram   \tTk.1000     \t\t07:00  PM")
        print()
        input("PRESS 'ENTER' KEY TO CONTINUE ")

    def cancel(self, random_num):
        while True:
            try:
                reservation_no = int(input("\nENTER YOUR RESERVATION NUMBER : "))
                if reservation_no == random_num:
                    confirmation = input(f"\nRESERVATION NUMBER IS IT CORRECT? {reservation_no} \nENTER (Y/N) : ").lower()
                    if confirmation == 'y':
                        bus_num = int(input("ENTER THE BUS NUMBER: "))
                        seat_cancel = int(input("HOW MANY SEATS DO YOU WANT TO CANCEL: "))
                        for _ in range(seat_cancel):
                            seat_number = int(input("ENTER THE SEAT NUMBER: "))
                            self.bus_seat[bus_num][seat_number] = 0
                        print("\nYOUR RESERVATION HAS BEEN CANCELLED!!")
                        self.display_seat(self.bus_seat[bus_num])
                        input("Press any key to continue...")
                        break
                    else:
                        print("\nYOUR RESERVATION CANCELLATION HAS BEEN DENIED")
                        break
                else:
                    print("\nNOT FOUND!! ENTER THE CORRECT RESERVATION NUMBER")
            except ValueError:
                print("\nPLEASE ENTER A VALID NUMBER")

    def main(self):
        random_num = random.randint(10000, 99999)
        self.login()
        while True:
            print("\n\n====================================================================")
            print("\t\t\tBUS RESERVATION")
            print("\n=====================================================================")
            print("\n====================  MAIN MENU  =====================\n")
            print("   [1] VIEW BUS LIST")
            print("   [2] BOOK TICKETS")
            print("   [3] CANCEL BOOKING")
            print("   [4] BUSES SEATS INFO")
            print("   [5] RESERVATION INFO")
            print("   [6] EXIT\n")
            try:
                choice = int(input("ENTER YOUR CHOICE: "))
                if choice == 1:
                    self.bus_lists()
                elif choice == 2:
                    self.bus_lists()
                    while True:
                        try:
                            bus_choice = int(input("\nCHOOSE YOUR BUS: "))
                            if bus_choice <= 0 or bus_choice >= 10:
                                self.green_color()
                                print("\nENTER VALID BUS NUMBER!!")
                                self.reset_color()
                            else:
                                break
                        except ValueError:
                            self.green_color()
                            print("\nENTER A VALID NUMBER!!")
                            self.reset_color()
                    
                    self.display_seat(self.bus_seat[bus_choice])
                    
            
                    
                    for i in range(seats):
                        while True:
                            try:
                                seat_number = int(input("ENTER THE SEAT NUMBER: "))
                                if seat_number <= 0 or seat_number > 32:
                                    self.green_color()
                                    print("\nENTER VALID SEAT NUMBER!!")
                                    self.reset_color()
                                else:
                                    break
                            except ValueError:
                                self.green_color()
                                print("\nENTER A VALID NUMBER!!")
                                self.reset_color()
                        
                        cust_id = bus_choice * 1000 + seat_number
                        self.bus_seat[bus_choice][seat_number] = 1
                        name = input("\nENTER THE PERSON NAME: ")
                        self.root = self.insert(self.root, cust_id, name)
                        self.green_color()
                        print(f"\nYOUR CUSTOMER ID IS: {cust_id}")
                        print("\n==================================================================================")
                        self.reset_color()
                    self.green_color()
                    print(f"\nYOUR RESERVATION NUMBER IS: {random_num}")
                    print("\nPLEASE NOTE DOWN YOUR RESERVATION NUMBER FOR CANCELLING BOOKING TICKETS!")
                    self.reset_color()
                    input("Press any key to continue...")

                elif choice == 3:
                    self.cancel(random_num)

                elif choice == 4:
                    print("\n\n")
                    self.status()

                elif choice == 5:
                    while True:
                        try:
                            cust_id = int(input("\nENTER YOUR CUSTOMER ID: "))
                            self.reservation_info(self.root, cust_id)
                            break
                        except ValueError:
                            print("\nPLEASE ENTER A VALID NUMBER!!")

                elif choice == 6:
                    self.green_color()
                    print("\n\n=====================================================================")
                    print("THANK YOU FOR USING THIS BUS RESERVATION SYSTEM")
                    print("\nPRESS ANY KEY TO EXIT THE END PROGRAM !! ")
                    print("\n\n")
                    self.reset_color()
                    break

                else:
                    print("\n\n   INVALID INPUT! CHOOSE CORRECT OPTION!\n")
            except ValueError:
                print("\n\n   INVALID INPUT! PLEASE ENTER A NUMBER!\n")

if __name__ == "__main__":
    bus_system = BusTicketManagementSystem()
    bus_system.main()

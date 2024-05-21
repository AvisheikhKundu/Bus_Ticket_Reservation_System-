import random

class BinarySearchTree:
    def __init__(self, pass_no, name):
        self.pass_no = pass_no
        self.name = name
        self.left = None
        self.right = None

class BusTicketManagementSystem:
    def __init__(self):
        self.root = None
        self.bus_seat = [[0]*9 for _ in range(33)]
    
    def green_color(self):
        print("\033[1;32m", end="")
        
    def reset_color(self):
        print("\033[0m", end="")
        
    def reservation_info(self, r, s, cust_id_matched):
        if r is None:
            return None
        
        present_node = r
        while present_node:
            if present_node.pass_no == s:
                cust_id_matched[0] = 1
                self.green_color()
                print("\n-----------------------------------------------------------------")
                print(f"||              NAME: {present_node.name:10}                               ||")
                print(f"||              CUSTOMER ID: {present_node.pass_no: <10}                              ||")
                print(f"||              BUS NUMBER: {present_node.pass_no // 1000: <10}                                  ||")
                print(f"||              SEAT NUMBER: {present_node.pass_no % 100: <10}                                 ||")
                print(f"||              TICKET COST: Tk.{self.cost(present_node): <10}                             ||")
                print("-----------------------------------------------------------------")
                self.reset_color()
                input("Press any key to continue...")
                return r
            elif present_node.pass_no > s:
                present_node = present_node.left
            else:
                present_node = present_node.right
        
        return None
    
    def insert(self, r, cust_id):
        if r is None:
            r = BinarySearchTree(cust_id, "")
            if r is None:
                print("No memory...")
                return None
            else:
                r.left = r.right = None
                r.name = input("\nEnter the person name: ")
        else:
            if r.pass_no > cust_id:
                r.left = self.insert(r.left, cust_id)
            elif r.pass_no < cust_id:
                r.right = self.insert(r.right, cust_id)
        return r
    
    def display_seat(self, bus):
        for i in range(1, 33):
            self.green_color()
            print(f"{i:02d}. ", end="")
            self.reset_color()
            for seat in bus[i]:
                if seat == 0:
                    print("EMPTY", end=" ")
                else:
                    print("BOOKED", end=" ")
            print()
    
    def login(self):
        username = "user"
        password = "Avisheikh001"

        print("\n\n=========================================================================================")
        print("\n\t\t\t\tWELCOME TO OUR BUS TERMINAL\n\n\t\t\t\t   \'Have a safe Journry\'")
        print("\n\n=========================================================================================\n\n")

        while True:
            match_user = input("\n\nUserName: ")
            match_pass = input("\nPassWord: ")

            if match_user == username and match_pass == password:
                print("\nLOGED IN SUCCESSFULLY...\n")
                break
            else:
                print("\nINVALID DETAILS TRY AGAIN...\n")
    
    def cost(self, r):
        bus_cost = r.pass_no // 1000
        if bus_cost % 3 == 1:
            return 2000
        elif bus_cost % 3 == 2:
            return 1000
        elif bus_cost % 3 == 0:
            return 1500
        else:
            return 0
    
    def status(self):
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
        input("\n\nPress 'ENTER' key to continue...")
    
    def cancel(self, random_num):
        reservation_no = int(input("\nEnter your reservation number: "))
        if reservation_no == random_num:
            confirmation = input(f"\nReservation number is it correct? {reservation_no}\nEnter (Y/N): ")
            if confirmation.lower() == 'y':
                bus_num = int(input("\nEnter the bus number: "))
                seat_cancel = int(input("\nHow many seats do you want to cancel: "))
                for i in range(seat_cancel):
                    seat_number = int(input("\nEnter the seat number: "))
                    self.bus_seat[bus_num][seat_number] = 0
                print("\nYour reservation has been canceled!")
                input("\nPress 'ENTER' key to continue...")
                self.display_seat(self.bus_seat[bus_num])
            else:
                print("\nYour reservation cancelation has been denied.")
        else:
            print("\nReservation number not found. Please enter the correct reservation number.")
    
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
            num = int(input("Enter your choice: "))
            if num == 1:
                self.status()
            elif num == 2:
                self.status()
                bus_choice = int(input("\nChoose your bus: "))
                if bus_choice <= 0 or bus_choice > 9:
                    print("\nEnter valid bus number!")
                    continue
                self.display_seat(self.bus_seat[bus_choice])
                while True:
                    seats = int(input("\nNumber of seats you need to book: "))
                    if seats <= 0:
                        print("\nEnter valid seat number!")
                    elif seats > 32:
                        print("\nEnter valid seat number. We have only 32 seats in a bus!")
                    else:
                        break
                
                for i in range(1, seats+1):
                    print("\n==================================================================================")
                    while True:
                        seat_number = int(input("Enter the seat number: "))
                        if seat_number <= 0 or seat_number > 32:
                            print("\nEnter valid seat number. We have only 32 seats in a bus!")
                        else:
                            break
                    cust_id = bus_choice * 1000 + seat_number
                    self.bus_seat[bus_choice][seat_number] = 1
                    self.root = self.insert(self.root, cust_id)
                    print(f"\nYour customer ID is: {cust_id}")
                    print("\n==================================================================================")
                print(f"\nYour reservation number is: {random_num}\nPlease note down your reservation number for canceling booking tickets!")
                input("Press 'ENTER' key to continue...")
                
            elif num == 3:
                self.cancel(random_num)
                
            elif num == 4:
                print("\n\n")
                self.display_seat(self.bus_seat)
                input("Press 'ENTER' key to continue...")
                
            elif num == 5:
                while True:
                    reservation_no = int(input("\nEnter your reservation number: "))
                    if reservation_no == random_num:
                        while True:
                            cust_id = int(input("\nEnter your customer ID: "))
                            cust_id_matched = [0]
                            self.reservation_info(self.root, cust_id, cust_id_matched)
                            if cust_id_matched[0] == 0:
                                print("\nEnter correct customer ID!")
                            else:
                                break
                        break
                    else:
                        print("\nInvalid reservation number. Please enter correct reservation number!")
                
            elif num == 6:
                print("\n\n=====================================================================")
                print("THANK YOU FOR USING THIS BUS RESERVATION SYSTEM")
                print("\nPRESS ANY KEY TO EXIT THE END PROGRAM !! ")
                print("\n\n")
                break
                
            else:
                print("\n\n   INVALID INPUT! CHOOSE CORRECT OPTION!\n")
    
if __name__ == "__main__":
    bus_system = BusTicketManagementSystem()
    bus_system.main()
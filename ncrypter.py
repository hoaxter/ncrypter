from colorama import init, Fore

init()
red = Fore.RED
green = Fore.GREEN
blue = Fore.LIGHTBLUE_EX
yellow = Fore.YELLOW
white = Fore.WHITE
reset = Fore.RED


class Ncrypter:

    def __init__(self):
        print(f'''{red}
              
███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗███████╗██████╗ 
████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   █████╗  ██████╔╝
██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██╔══╝  ██╔══██╗
██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   ███████╗██║  ██║
╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                    {yellow}GitHub: @hoaxter
                                                    MadeBy: Nitin Sikarwar''')
        
        choice = input(f'''{reset}{green}\n=>Encrypt:        press [1]
=>Decrypt:        press [2]
=>Brute force:    press [3]
=>Quit:           press [q] \n
==>Enter Your choice: ''')

        if choice == "1":
            self.encrypt()
        
        elif choice == "2":
            self.decrypt()

        elif choice == "3":
            self.brute_force()

        elif choice == "q":
            exit()

        elif choice !="1" and choice != "2" and choice != "q":
             print(f"{red}[-] Select the given values only !\n")
             self.__init__()

    def checker(self,msg):
        special = "1234567890!@#$%^&*()_+-?><{}~.,;'[]|/\\"

        for i in msg:
            if i in special:
                print(f"{red}[-] Only take alphabet as input \n")
                self.__init__()

    def encrypt(self):

        alpha = "abcdefghijklmnopqrstuvwxyz"
            
        msg = input(f"{blue}\n[+] Enter the message to be Encrypted: ").lower()

        self.checker(msg)

        try:
            k = int(input(f"{blue}[+] Enter the key to Encrypt: "))

        except ValueError:
            print(f"{red}[-] Only integer values are allowed.\n")
            self.__init__()

        cipher = ""

        for ch in msg:

            if ch in alpha:
                pos = alpha.find(ch)
                pos1 = (pos + k) % 26
                encval = alpha[pos1]
                cipher += encval
    
            else:
                cipher += ch

        print(f"{yellow}\n[#] Your Encrypted message is: {white}{cipher.upper()} \n")
        self.__init__()

    def decrypt(self):

        alpha = "abcdefghijklmnopqrstuvwxyz"

        msg = input(f"\n{blue}[+] Enter the message to be Decrypted: ")

        self.checker(msg)

        try:
            k = int(input(f"{blue}[+] Enter the key to Decrypt: "))

        except ValueError:
            print(f"{red}[-] Only integer values are allowed.\n")
            self.__init__()

        cipher = ""

        for ch in msg:

            if ch in alpha:
                pos = alpha.find(ch)
                pos1 = (pos - k) % 26
                encval = alpha[pos1]
                cipher += encval

            else:
                cipher += ch

        print(f"\n{yellow}[#] Your Decrypted message is: {white}{cipher.upper()}\n")
        self.__init__()

    def brute_force(self):
            alpha = "abcdefghijklmnopqrstuvwxyz"
            msg = input(f"\n{blue}[+] Enter the message: ")
            self.checker(msg)

            for k in range(len(alpha)):
                cipher = ""
                for ch in msg:
                    if ch in alpha:
                        pos = alpha.find(ch)
                        pos1 = (pos - k) % 26
                        encval = alpha[pos1]
                        cipher += encval 
                    else:
                        cipher += ch
                print(f"\n{yellow}[#] Your message with key {k}: {white}{cipher.upper()}\n")
            self.__init__()
    
neo = Ncrypter()

        


        

    

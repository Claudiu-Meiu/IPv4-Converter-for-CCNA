import re
import os

# Function to convert decimal IPv4 address to binary
def decimal_to_binary():
    while True:
        ipv4_address = input("dec2bin~> ")
        
        # Handling special commands
        if ipv4_address == "clear": clear_terminal(), decimal_to_binary()
        # Redirecting to other conversion functions
        if ipv4_address == "dec2hex": print("------------------------------------------------------"), decimal_to_hexadecimal()
        if ipv4_address == "bin2dec": print("------------------------------------------------------"), binary_to_decimal()
        if ipv4_address == "bin2hex": print("------------------------------------------------------"), binary_to_hexadecimal()
        if ipv4_address == "hex2dec": print("------------------------------------------------------"), hexadecimal_to_decimal()
        if ipv4_address == "hex2bin": print("------------------------------------------------------"), hexadecimal_to_binary()
        if ipv4_address == "menu": menu()
        # Validation of input IPv4 address
        if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ipv4_address):
            print("\nEnter a valid IPv4 address in decimal format !\n"
                  "\n------------------------------------------------------"); continue

        # Splitting the IPv4 address into octets
        octets = ipv4_address.split(".")

        binary_octets = []
        # Converting each octet to binary
        for octet in octets:
            value = int(octet)            
            binary_octet = ""
            for shortcut in [128, 64, 32, 16, 8, 4, 2, 1]:
                if value < 0 or value > 255:
                    print("\nEach octet must be between 0 and 255 !\n"
                        "\n------------------------------------------------------")
                    decimal_to_binary()
                if value >= shortcut:
                    binary_octet += "1"
                    value -= shortcut
                else:
                    binary_octet += "0"
            binary_octets.append(binary_octet)

        binary_ip = "".join(binary_octets)
        binary_ip_dot = ".".join(binary_octets)

        # Displaying the binary IP address
        print("binary~>", binary_ip)
        print("binary~>", binary_ip_dot, "\n------------------------------------------------------")

# Function to convert decimal IPv4 address to hexadecimal
def decimal_to_hexadecimal():
    while True:
        ipv4_address = input("dec2hex~> ")
        
        # Handling special commands
        if ipv4_address == "clear": clear_terminal(), decimal_to_hexadecimal()
        # Redirecting to other conversion functions
        if ipv4_address == "dec2bin": print("------------------------------------------------------"), decimal_to_binary()
        if ipv4_address == "bin2dec": print("------------------------------------------------------"), binary_to_decimal()
        if ipv4_address == "bin2hex": print("------------------------------------------------------"), binary_to_hexadecimal()
        if ipv4_address == "hex2dec": print("------------------------------------------------------"), hexadecimal_to_decimal()
        if ipv4_address == "hex2bin": print("------------------------------------------------------"), hexadecimal_to_binary()
        if ipv4_address == "menu": menu()
        # Validation of input IPv4 address
        if not re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', ipv4_address):
            print("\nEnter a valid IPv4 address in decimal format !\n"
                  "\n------------------------------------------------------"); continue

        # Splitting the IPv4 address into octets
        octets = ipv4_address.split(".")

        hex_list = []
        # Converting each octet to hexadecimal
        for octet in octets:
            dividend = int(octet)
            if dividend < 0 or dividend > 255:
                print("\nEach octet must be between 0 and 255 !\n"
                    "\n------------------------------------------------------")
                decimal_to_hexadecimal()
            else:
                divisor = 16
                division = int(dividend / divisor)
                reminder = dividend % divisor
                if division == 10: division = "A"
                if division == 12: division = "C"
                if division == 13: division = "D"
                if division == 14: division = "E"
                if division == 15: division = "F"
                
                if reminder == 10: reminder = "A"
                if reminder == 11: reminder = "B"
                if reminder == 12: reminder = "C"
                if reminder == 13: reminder = "D"
                if reminder == 14: reminder = "E"
                if reminder == 15: reminder = "F"
                string = str(division), str(reminder)
                hex_list.append(string)

            hex_string = "".join([hex_value[0] + hex_value[1] for hex_value in hex_list])
            hex_string_dot = ".".join([hex_value[0] + hex_value[1] for hex_value in hex_list])

        # Displaying the hexadecimal IP address
        print("hex~> ", "0x", hex_string, sep="")
        print("hex~>", hex_string_dot, "\n------------------------------------------------------")

# Function to convert binary IPv4 address to decimal
def binary_to_decimal():
    while True:
        binary_ip = input("bin2dec~> ")

        # Handling special commands
        if binary_ip == "clear": clear_terminal(), binary_to_decimal()
        # Redirecting to other conversion functions
        if binary_ip == "dec2bin": print("------------------------------------------------------"), decimal_to_binary()
        if binary_ip == "dec2hex": print("------------------------------------------------------"), decimal_to_hexadecimal()
        if binary_ip == "bin2hex": print("------------------------------------------------------"), binary_to_hexadecimal()
        if binary_ip == "hex2dec": print("------------------------------------------------------"), hexadecimal_to_decimal()
        if binary_ip == "hex2bin": print("------------------------------------------------------"), hexadecimal_to_binary()
        if binary_ip == "menu": menu()
        # Validation of input IPv4 address
        if not re.match(r'^\d{1,8}\.\d{1,8}\.\d{1,8}\.\d{1,8}$', binary_ip):
            print("\nEnter a valid IPv4 address in binary format !\n"
                  "\n------------------------------------------------------"); continue
        
        # Splitting the binary IP address into octets
        octets = binary_ip.split(".")

        decimal_ip = []
        # Converting each octet to decimal
        for octet in octets:
            decimal_value = 0
            power = 7
            for bit in octet:
                if bit == '1':
                    decimal_value += 2 ** power
                power -= 1
            decimal_ip.append(str(decimal_value))

        decimal_ip_address = ".".join(decimal_ip)

        # Displaying the decimal IP address
        print("decimal~>", decimal_ip_address, "\n------------------------------------------------------")

# Function to convert binary IPv4 address to hexadecimal
def binary_to_hexadecimal():
    while True: 
        binary_ip = input("bin2hex~> ")

        # Handling special commands
        if binary_ip == "clear": clear_terminal(), binary_to_hexadecimal()

        # Redirecting to other conversion functions
        if binary_ip == "dec2bin": print("------------------------------------------------------"), decimal_to_binary()
        if binary_ip == "dec2hex": print("------------------------------------------------------"), decimal_to_hexadecimal()
        if binary_ip == "bin2dec": print("------------------------------------------------------"), binary_to_decimal()
        if binary_ip == "hex2dec": print("------------------------------------------------------"), hexadecimal_to_decimal()
        if binary_ip == "hex2bin": print("------------------------------------------------------"), hexadecimal_to_binary()
        if binary_ip == "menu": menu()
        # Validation of input IPv4 address
        if not re.match(r'^\d{1,8}\.\d{1,8}\.\d{1,8}\.\d{1,8}$', binary_ip):
            print("\nEnter a valid IPv4 address in binary format !\n"
                  "\n------------------------------------------------------"); continue
        
        # Splitting the binary IP address into octets
        octets = binary_ip.split(".")

        decimal_ip = []
        # Converting each octet to decimal
        for octet in octets:
            decimal_value = 0
            power = 7
            for bit in octet:
                if bit == '1':
                    decimal_value += 2 ** power
                power -= 1
            decimal_ip.append(str(decimal_value))

        decimal_ip_address = ".".join(decimal_ip)
        
        # Splitting the decimal IP address into octets
        octets = decimal_ip_address.split(".")

        hex_list = []
        # Converting each octet to hexadecimal
        for octet in octets:
            dividend = int(octet)
            divisor = 16
            division = int(dividend / divisor)
            reminder = dividend % divisor
            if division == 10: division = "A"
            if division == 11: division = "B"
            if division == 12: division = "C"
            if division == 13: division = "D"
            if division == 14: division = "E"
            if division == 15: division = "F"
            
            if reminder == 10: reminder = "A"
            if reminder == 11: reminder = "B"
            if reminder == 12: reminder = "C"
            if reminder == 13: reminder = "D"
            if reminder == 14: reminder = "E"
            if reminder == 15: reminder = "F"
            string = str(division), str(reminder)
            hex_list.append(string)

        hex_string = "".join([hex_value[0] + hex_value[1] for hex_value in hex_list])
        hex_string_dot = ".".join([hex_value[0] + hex_value[1] for hex_value in hex_list])

        # Displaying the hexadecimal IP address
        print("hex~> ", "0x", hex_string, sep="")
        print("hex~>", hex_string_dot, "\n------------------------------------------------------")

# Function to convert hexadecimal IPv4 address to decimal
def hexadecimal_to_decimal():
    while True:
        hex_address = input("hex2dec~> ")

        # Handling special commands
        if hex_address == "clear": clear_terminal(), hexadecimal_to_decimal()
        # Redirecting to other conversion functions
        if hex_address == "dec2bin": print("------------------------------------------------------"), decimal_to_binary()
        if hex_address == "dec2hex": print("------------------------------------------------------"), decimal_to_hexadecimal()
        if hex_address == "bin2dec": print("------------------------------------------------------"), binary_to_decimal()
        if hex_address == "bin2hex": print("------------------------------------------------------"), binary_to_hexadecimal()
        if hex_address == "hex2bin": print("------------------------------------------------------"), hexadecimal_to_binary()
        if hex_address == "menu": menu()
        # Validation of input IPv4 address
        if not re.match(r'^([0-9A-Fa-f]{2}\.){3}[0-9A-Fa-f]{2}$', hex_address):
            print("\nEnter a valid IPv4 address in hexadecimal format!\n"
                  "\n------------------------------------------------------")
        else:
            # Splitting the hexadecimal IP address into octets
            octets = hex_address.split(".")
            decimal_octets = []
            for octet in octets:
                decimal_octet_first = octet[0]
                decimal_octet_second = octet[1]
                decimal_octets.append(decimal_octet_first)
                decimal_octets.append(decimal_octet_second)
            
            value_to_replace = ['a', 'b', 'c', 'd', 'e', 'f']
            new_value = ['10', '11', '12', '13', '14', '15']
            for i in range(len(decimal_octets)):
                if decimal_octets[i].lower() in [x.lower() for x in value_to_replace]:
                    index = [x.lower() for x in value_to_replace].index(decimal_octets[i].lower())
                    decimal_octets[i] = int(new_value[index])             
            
            for i in range(len(decimal_octets)): decimal_octets[i] = int(decimal_octets[i])

            decimal_ipv4 = str(decimal_octets[0] * 16 + decimal_octets[1] * 16 ** 0) + '.' + \
                           str(decimal_octets[2] * 16 + decimal_octets[3] * 16 ** 0) + '.' + \
                           str(decimal_octets[4] * 16 + decimal_octets[5] * 16 ** 0) + '.' + \
                           str(decimal_octets[6] * 16 + decimal_octets[7] * 16 ** 0)
            
            # Displaying the decimal IP address
            print("decimal~>", decimal_ipv4, "\n------------------------------------------------------")

# Function to convert hexadecimal IPv4 address to binary
def hexadecimal_to_binary():
    while True:
        hex_address = input("hex2bin~> ")

        # Handling special commands
        if hex_address == "clear": clear_terminal(), hexadecimal_to_binary()
        # Redirecting to other conversion functions
        if hex_address == "dec2bin": print("------------------------------------------------------"), decimal_to_binary()
        if hex_address == "dec2hex": print("------------------------------------------------------"), decimal_to_hexadecimal()
        if hex_address == "bin2dec": print("------------------------------------------------------"), binary_to_decimal()
        if hex_address == "bin2hex": print("------------------------------------------------------"), binary_to_hexadecimal()
        if hex_address == "hex2dec": print("------------------------------------------------------"), hexadecimal_to_decimal()
        if hex_address == "menu": menu()
        # Validation of input IPv4 address
        if not re.match(r'^([0-9A-Fa-f]{2}\.){3}[0-9A-Fa-f]{2}$', hex_address):
            print("\nEnter a valid IPv4 address in hexadecimal format!\n"
                  "\n------------------------------------------------------")
        else:
            # Splitting the hexadecimal IP address into octets
            octets = hex_address.split(".")
            decimal_octets = []
            for octet in octets:
                decimal_octet_first = octet[0]
                decimal_octet_second = octet[1]
                decimal_oct

        # Handling special commands
        if hex_address == "clear": clear_terminal(), hexadecimal_to_binary()
        # Redirecting to other conversion functions
        if hex_address == "dec2bin": print("------------------------------------------------------"), decimal_to_binary()
        if hex_address == "dec2hex": print("------------------------------------------------------"), decimal_to_hexadecimal()
        if hex_address == "bin2dec": print("------------------------------------------------------"), binary_to_decimal()
        if hex_address == "hex2dec": print("------------------------------------------------------"), hexadecimal_to_decimal()
        if hex_address == "hex2bin": print("------------------------------------------------------"), hexadecimal_to_binary()
        if hex_address == "menu": menu()
        # Validation of input IPv4 address
        if not re.match(r'^([0-9A-Fa-f]{2}\.){3}[0-9A-Fa-f]{2}$', hex_address):
            print("\nEnter a valid IPv4 address in hexadecimal format!\n"
                  "\n------------------------------------------------------")
        else:
            # Splitting the hexadecimal IP address into octets
            octets = hex_address.split(".")
            decimal_octets = []
            for octet in octets:
                decimal_octet_first = octet[0]
                decimal_octet_second = octet[1]
                decimal_octets.append(decimal_octet_first)
                decimal_octets.append(decimal_octet_second)
            
            value_to_replace = ['a', 'b', 'c', 'd', 'e', 'f']
            new_value = ['10', '11', '12', '13', '14', '15']
            for i in range(len(decimal_octets)):
                if decimal_octets[i].lower() in [x.lower() for x in value_to_replace]:
                    index = [x.lower() for x in value_to_replace].index(decimal_octets[i].lower())
                    decimal_octets[i] = int(new_value[index])             
            
            for i in range(len(decimal_octets)): decimal_octets[i] = int(decimal_octets[i])

            decimal_ipv4 = str(decimal_octets[0] * 16 + decimal_octets[1] * 16 ** 0) + '.' + \
                           str(decimal_octets[2] * 16 + decimal_octets[3] * 16 ** 0) + '.' + \
                           str(decimal_octets[4] * 16 + decimal_octets[5] * 16 ** 0) + '.' + \
                           str(decimal_octets[6] * 16 + decimal_octets[7] * 16 ** 0)

            # Splitting the decimal IP address into octets
            octets = decimal_ipv4.split(".")

            binary_octets = []
            # Converting each octet to binary
            for octet in octets:
                value = int(octet)            
                binary_octet = ""
                for shortcut in [128, 64, 32, 16, 8, 4, 2, 1]:
                    if value >= shortcut:
                        binary_octet += "1"
                        value -= shortcut
                    else:
                        binary_octet += "0"
                binary_octets.append(binary_octet)

            binary_ip = "".join(binary_octets)
            binary_ip_dot = ".".join(binary_octets)

            # Displaying the binary IP address
            print("binary~>", binary_ip)
            print("binary~>", binary_ip_dot, "\n------------------------------------------------------")


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    while True:
        print("------------------------------------------------------")
        option = input("\n1. Decimal ~> Binary\n2. Decimal ~> Hexadecimal\n3. Binary ~> Decimal\n4. Binary ~> Hexadecimal\n"
                       "5. Hexadecimal ~> Decimal\n6. Hexadecimal ~> Binary\n\nh. Help\n0. Exit\n\noption~> ")
        print("------------------------------------------------------")

        if option == "clear": clear_terminal(), menu()

        if option == "h": print("\nType 'dec2bin' to convert from decimal to binary."
                                "\nType 'dec2hex' to convert from decimal to hexadecimal."
                                "\nType 'bin2dec' to convert from binary to decimal."
                                "\nType 'bin2hex' to convert from binary to hexadecimal."
                                "\nType 'hex2dec' to convert from hexadecimal to decimal."
                                "\nType 'hex2bin' to convert from hexadecimal to binary."
                                "\n\nType 'menu' to get back the screen menu."
                                "\nType 'clear' to clear the screen.\n"); continue
        
        if not re.match(r'^\d{1}$', option): print("\nChose between 1, 2, 3, 4, 5, 6 or 0 and h for help !\n"); continue
        if int(option) > 6 or int(option) < 0: print("\nChose between 1, 2, 3, 4, 5, 6 or 0 and h for help !\n"); continue

        if int(option) == 1: decimal_to_binary()
        if int(option) == 2: decimal_to_hexadecimal()
        if int(option) == 3: binary_to_decimal()
        if int(option) == 4: binary_to_hexadecimal()
        if int(option) == 5: hexadecimal_to_decimal()
        if int(option) == 6: hexadecimal_to_binary()
        if int(option) == 0: print("Goodbye !\n------------------------------------------------------\n"), quit()


menu()
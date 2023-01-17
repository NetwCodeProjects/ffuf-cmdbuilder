import subprocess
import os
import time

username = os.environ.get('username')

file_path = f"C:\\users\\{username}\\desktop\\output.txt"
yeslist = ["y", "Y", "yes", "Yes", "YES"]
nolist = ["n", "N", "no", "No", "NO"]

wordlist_path = f"C:\\Users\\{username}\\Desktop\\WordLists\\Discovery\\Web-Content\\common.txt"
param_path = f"C:\\Users\\{username}\\Desktop\\WordLists\\Discovery\\Web-Content\\parameters.txt"
basic_scan = "-b"
recursive_scan = "-rb"
param_mining = "-p"
flag = False

print("write output to file\n [y]yes or [n]no")
user_input = input()

if user_input in yeslist:
    while not flag:
        print("choose scan:\n [-b] Basic Scan\n [-rb] Recursive Basic Scan\n [-p] Param Mining")
        scan_type = input()
        if scan_type == basic_scan:
            flag = True
        elif scan_type == recursive_scan:
            flag = True
        elif scan_type == param_mining:
            flag = True
        else:
            print("Invalid input: please use -b or -rb or -p")
    
    if flag:
        print("Enter target url:")
        target_url = input()
    
    else:
        print("Invalid input provided for scan_type. Exiting...")
        exit()
    
    if scan_type == basic_scan:
        with open(file_path, "w") as f:
            subprocess.run(["cmd.exe", "/k", f"ffuf -w {wordlist_path} -u {target_url}/FUZZ"], stdout=f, stderr=f)
    
    elif scan_type == recursive_scan:
        with open(file_path, "w") as f:
            subprocess.run(["cmd.exe", "/k", f"ffuf -w {wordlist_path} -recursion -u {target_url}/FUZZ"], stdout=f, stderr=f)
    
    elif scan_type == param_mining:
        with open(file_path, "w") as f:
            subprocess.run(["cmd.exe", "/k", f"ffuf -w {param_path} -u {target_url}FUZZ=1"], stdout=f, stderr=f)

    else:
        print("Invalid input: please use -b or -rb or -p")

elif user_input in nolist:
    while not flag:
        print("choose scan:\n [-b] Basic Scan\n [-rb] Recursive Basic Scan\n [-p] Param Mining")
        scan_type = input()
        if scan_type == basic_scan:
            flag = True
        elif scan_type == recursive_scan:
            flag = True
        elif scan_type == param_mining:
            flag = True
        else:
            print("Invalid input: please use -b or -rb or -p")
    
    if flag:
        print("Enter target url:")
        target_url = input()
    
    else:
        print("Invalid input provided for scan_type. Exiting...")
        exit()

    if scan_type == basic_scan:
        subprocess.run(["cmd.exe", "/k", f"ffuf -w {wordlist_path} -u {target_url}/FUZZ"])
    
    elif scan_type == recursive_scan:
        subprocess.run(["cmd.exe", "/k", f"ffuf -w {wordlist_path} -recursion -u {target_url}/FUZZ"])

    elif scan_type == param_mining:
        subprocess.run(["cmd.exe", "/k", f"ffuf -w {param_path} -u {target_url}FUZZ=1"])

    else:
        print("Invalid input: please use -b or -rb or -p")

else:
    print("Invalid input! use 'y' or 'yes' or 'n' 'no'")
    time.sleep(1)
    print("exiting...")
    time.sleep(3)
    exit()

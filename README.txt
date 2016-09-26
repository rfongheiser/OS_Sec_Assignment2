This project is an assignment for COSC 440 (Operating Systems Security) at Towson University.

The project goal is to:

Write a program using Python to implement a password cracker for Linux.
The program should take the shadow file and a username as aprguments and recover the specified user's password.  
The program quits with a warning if the user does not exist or does not have a password.  
On completion, the program should display a recovered password.  
If the password is not in the dictionary, the program should state “password not in dictionary” upon completion.

INSTRUCTIONS: 

1) Clone this repository (make sure git is installed)
      i.) git clone https://github.com/rfongheiser/OS_Sec_Assignment2 /rfongheiser (SPACE BETWEEN OS_SEC_ASSIGNMENT2 and /rfongheiser)
2) Change the directory to the repository
      i.) cd /rfongheiser
3) Give the script executable permissions
      i.) sudo chmod +x assignment2.py
4) Ensure the user has permissions to access shadow file
5) Ensure there is a dictionary in the file path "/usr/share/dict/american-english"
6) Run the script with the correct arguments
      i.) python assignment2.py <username> <shadow_file_path>
      ii.) Example: python assignment2.py csuser /etc/shadow
      

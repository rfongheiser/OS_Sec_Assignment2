#Assignment 2 
import sys, crypt

def main():
	
	if len(sys.argv) != 3:                                                                #If the arguments length is not correct
		print "Invalid arguments." 
		print "Example: python assignment2.py <username> <shadow_file_path>"
		exit(1)
	
	user = sys.argv[1]
	shadow_file = sys.argv[2]
	print "Entered user: {}".format(user)
	print "Entered file path: {}".format(sys.argv[2])

	hash_list = {}

	#Open the shadow file and put the found users and their ASH (algorithm, salt, hash) in hash_list

	try:
		with open(shadow_file, 'r') as shadow_file:
			for line in shadow_file:
				username = line.split(':')[0]                #Username is the string before the first ':'
				rest = line.split(':')[1]                    #The rest of the string consists the ASH
				if rest not in ['!', '*']:
					hash_list.update({username: rest})
			shadow_file.close()

	except IOError:
		print "File {} not found. Please enter correct file path.".format(shadow_file)
		exit(1)

	if user in list(hash_list.keys()):
		print "User {} found.".format(user)
	else:
		print "User {} not found.".format(user)
		exit(1)

	ASH = hash_list[user]

	#Split the ASH up into respective variables

	temp = ASH.split('$')
	hash = temp[-1]
	salt = temp[-2]
	alg = temp[-3]

	#Open dictionary in the path "/usr/share/dict/american-english" to crack the hash. If there is a hash
	#collision between temp and ASH then the password has been recovered. 
	
	print "Trying to crack password. Please wait patiently."

	try:
		with open("/usr/share/dict/american-english", 'r') as dictionary:
			for line in dictionary:
				temp = crypt.crypt(line.rstrip('\n'), "${}${}".format(alg, salt)) #Encrypting each line in dictionary with the algorithm and salt used in the given shadow file
				if temp == ASH:
					print "The password was recovered!"
					print "The password is: {}".format(line)
					exit(0)
			dictionary.close()
	except IOError:
		print "Dictionary not in folder."
		print "Check path '/usr/share/dict/american-english'. Make sure dictionary exists."
		exit(1)
	
	print "Password not in dictionary."
	exit(1)

	
if __name__ == '__main__':
	main()
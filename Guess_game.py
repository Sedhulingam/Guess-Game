import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',8000)) 

name = input("\nEnter Player Name: ")  
print("\nGood Luck ! ", name) 


print("\nPlease Wait for the Admin to Give you the word:")
s.listen()
conn,addr=s.accept()
words=conn.recv(1024).decode('utf-8')

word=words.lower()

print("\nGuess the characters") 

guesses = '' 
turns = 12

while turns > 0: 

    failed = 0
    for char in word: 

        if char in guesses: 
            print(char,end='') 
            
        else: 
            print("_ ",end="") 
            failed += 1

    print("\n")        
    if failed == 0: 
    
        print("You Win") 
     
        print("The Word is: ", word)
        print("\n") 
        break

    guess = input("Guess a character:") 
     
    guesses += guess 
 
    if guess not in word: 
        
        turns -= 1

        print("Wrong\n") 
     
        print("You have", + turns, 'more Guesses') 
        
        if turns == 0: 
            print("You Loose\n")
            

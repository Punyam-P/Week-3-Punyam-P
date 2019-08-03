Q = "Which question number you wish to go to (press enter to exit)"
print(Q)
Qs=input()
Question = [1,2,3,4,5,6,7,8,9]

#if isinstance(Qs, Question):
#    print("works")
if True:
    while int(Qs) in Question:
        if int(Qs) == 1:
            message1 = "This was inside a variable" #this is a variable
            print(message1)
        elif int(Qs) == 2:
            message2 = "This had been inside a variable"
            print(message2)
            message2 = "This was just inside a variable"
            print(message2)
        elif int(Qs) == 3:
            name = "John"
            print("Hi "+name+" ,you were inside a variable")
        elif int(Qs) == 4:
            name2 = "Olivia"
            print(name2.lower())
            print(name2.upper())
            print(name2.title())
        elif int(Qs) == 5:
            print("Friedrich Nietzsche once said, God is dead.")
        elif int(Qs) == 6:
            famous_person = "Friedich Nietzsche"
            print(famous_person + " once said, God is dead.")
        elif int(Qs) == 7:
            name3 = " \n \t Rohan \t Thomas \t mathew \t "
            print(":"+name3+":")
            print(":"+name3.lstrip+":")
            print(":"+name3.rstrip+":")
            print(":"+name3.strip+":")
        elif int(Qs) == 8:
            print(2**2+4)
            print(2*4)
            print(2+6)
            print(1+2+3+2)
        elif int(Qs) == 9:
            fav_num = 42
            print(str(fav_num))
        print(Q)
        Qs=input()
    


'''
else:
    print("Thank You.") 
    '''




    
    


 
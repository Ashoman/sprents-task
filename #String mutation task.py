#String mutation task 
# We created a function and gave it the string and position and character

def function(string='abracadabra' ,position=6 ,character='a'):     
    mylist= list(string) #Here we put the string in a list 
    mylist[position]= character #Replace the character 'd' with 'a'
    string = ''.join(mylist) #Return the list to string again 
    print (string)   #Print string
function() # Call function

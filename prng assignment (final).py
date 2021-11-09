import random


from datetime import datetime

c=open("numbers.txt", "r") # we type the file name here
notepad_code= int(c.read())



    
# 1. here we take the seed input given by the user
while True:
    user_gen_choice = str(input("for file press 'f' and for seed input press 's': " ))
    if user_gen_choice =='f':
         seed = notepad_code
    elif user_gen_choice =='s':
             seed = int(input("please enter seed: "))
      
        
    else:
          print("wrong input ")
          
    starting_seed = seed
          
              
    

    
        

# 2.""" here we start using the datetime function to obtain the current date and time 
  #     of the computer


    date_time_now = datetime.now()
# 3. we turn the date and time into a whole integer number then turn that number into a list
    int_date_time_now = int(date_time_now.strftime("%Y%m%d%H%M%S"))



    digit_string = str(int_date_time_now)
 #Convert `an_ to a string


    digit_map = map(int, digit_string)
#Convert each character of `digit_string` to an integer


    digit_list = list(digit_map)
#Convert `digit_map` to a list



#we use the random function to shuffle that list then turn it into an integre again

    random.shuffle(digit_list)



    l = [str(digit) for digit in digit_list]
    a_string="".join(l)
    final_shuffled_datetime = int(a_string)

# LCM = ax + b (mod M)

 


    for N in range(19):
        
        seed = (seed + 2)
        a = 2346536254
        b = 1
        m = 2**43
    
        x_1 = ((int)(a)*(int)(seed)+(int)(b))
        x_1 = (x_1 %m)
   
    x_1 = str(x_1)

# ----------------------------------




    unshuflled_pass = (str(x_1) + str(final_shuffled_datetime))



    shuffled_pass = str(unshuflled_pass)
 

    shuffled_pass = map(int, unshuflled_pass)


    final_pass = list(shuffled_pass)

    random.shuffle(final_pass)



    l = [str(digit) for digit in final_pass]
    a_string="".join(l)
    final_pass_code = int(a_string)
   
    print(final_pass_code)
    
    print("starting seed was:" + str(starting_seed))
    
    
          
    
    while True:
        
              answer = str(input('Run again? (y/n): '))
              if answer in ('y', 'n'):
                  break
              print("invalid input.")
              if answer == 'y':
               continue
              else:
               print("Goodbye")
               break     



# LCM = ax + b (mod M)












    
     
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

    
#        with FOR LOOP    

for x in range(6):
    move()
    jump()
    
#        with WHILE LOOP
   
#number_of_hurdles = 6
#while number_of_hurdles > 0:
#    jump()
#    number_of_hurdles -= 1


#        with at_goal() WHILE LOOP (function applies to Reeborgs world only)

#while at_goal() == False:
#    jump()

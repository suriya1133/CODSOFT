import random
#winnig rules for rock,paper,scissor
print('Winning rules of Rock,Paper,Scissor are: \n'
      + 'Rock vs Paper -> Paper wins \n'
      + 'Rock vs Scissors -> Rock wins \n'
      + 'Paper vs Scissor -> Scissor wins \n')
while(True):
    print("Enter your choice \n 1.Rock \n 2.Paper \n 3.Scissor \n")
    choice=int(input("Enter your choice: "))
    # if choice is more than 3 or less than 1 
    while choice > 3 or choice < 1:
        choice=int(input("Please enter valid chocie "))
        # initializse the choice for rock,paper,scissors
    if (choice == 1):
        choice_name='Rock'
    elif (choice == 2):
        choice_name='Paper'
    else:
        choice_name='Scissors'
        # print user chocie
    print('User choice is \n',choice_name)
    print('Now its computer turn....')
    # let the comuter uses random module to take choice
    comp_choice=random.randint(1,3)
    while comp_choice == choice:
        comp_choice=random.randint(1,3)

        #intializse for computer to pick choice like user
    if (comp_choice == 1):
        comp_choice_name = 'rocK'
    elif(comp_choice == 2):
        comp_choice_name = 'papeR'
    else:
        comp_choice_name = 'scissorS'
    print('computer choice is \n',comp_choice)
    print(choice_name,'Vs',comp_choice_name)
    if choice == comp_choice:
        print('Draw')
        result='DRAW'
    if(choice == 1 and comp_choice == 2):
        print("papeR wins =>\n",end="")
        result='papeR'
    elif(choice == 2 and comp_choice == 1):
        print("Paper wins =>\n",end= "")
        result='Paper'

    if(choice == 1 and comp_choice == 3):
        print("Rock wins =>\n",end="")
        result='Rock'
    elif(choice == 3 and comp_choice == 1):
        print("rocK wins =>\n",end="")
        result='rocK'

    if(choice == 2 and comp_choice == 3):
        print("Scissors wins =>\n",end="")
        result='scissorS'
    elif(choice == 3 and comp_choice == 2):
        print("Scissors wins =>\n",end="")
        result='Rock'
        #print either if user and computer wins and draw
    if result == 'Draw':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? ")
    ans=input()
    if(ans == 'NO'):
        break
    # #we print thanks for playing the game
print("Thanks for playing")

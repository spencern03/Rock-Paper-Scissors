print"Welcome to Rock Paper Scissors! Make sure to have your item already in mind before you start. Ready,set,go!"
import time
i=0
while i<5:
    time.sleep(5)
    your_choice_is_=raw_input("Your Choice")
    print"What Is Your Choice?"
    print(your_choice_is_)
    import random
    a=random.randint(0,2)
    array=["rock","paper","scissors"]
    comp=array[a]
    print(comp)
    if comp=="rock" and your_choice_is_=="paper":
        print"You Win!"
    elif comp=="rock" and your_choice_is_=="rock":
        print"You Tied"
    elif comp=="rock" and your_choice_is_=="scissors":
        print"You Lost :("
    elif comp=="paper" and your_choice_is_=="rock":
        print"You Lost :("
    elif comp=="paper" and your_choice_is_=="paper":
        print"You Tied"
    elif comp=="paper" and your_choice_is_=="scissors":
        print"You Win!"
    elif comp=="scissors" and your_choice_is_=="rock":
        print"You Win!"
    elif comp=="scissors" and your_choice_is_=="paper":
        print"You Lost :("
    elif comp=="scissors" and your_choice_is_=="scissors":
        print"You Tied"
    i=i+1


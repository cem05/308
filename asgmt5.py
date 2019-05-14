

#create ten original answers to yes or no questions,
#four positive, three indeterminate, and three negative.
#Extra points will be awarded for the most creative set of answers.
##How to write this application:
#Tell your user to think of a “yes or no” question.
#Then the user asks the Magic 8-Ball for a reply by pressing a key
#Write a random function that returns a random int between 1 and 10.
#Use your random function to select your reply
#The reply, one of your 10 original answers, appears on the screen


#preliminary variables
#input
##processing
##output


#preliminary variables
#input
import random
import time

intro = input('Welcome to the Ualbany magic-8ball!  Please enter your name:  ')

def nom_de_guerre():
    return(intro)
def think_hold():
    print('Thinking...')
    return(time.sleep(3))
def randy ():
    return(random.randint(0,10))

print('Hi',nom_de_guerre(),". Please think of a 'Yes or No' question.")
print('\n')
print('If you have your question the Ualbany magic-8ball is ready with your answer.')
print('Ok',nom_de_guerre(),"please press the 'Enter' key to continue...")
print(input(''))


##processing
##output
#answers for 8ball
if randy() == 1:
    think_hold()
    print('This might be a good time for some shots')
elif randy() == 2:
    think_hold()
    print('Southwest is running a sale on flights right now...')
elif randy() == 3:
    think_hold()
    print("I've got nothing...")
elif randy() == 4:
    think_hold()
    print("Did someone say 'Tacos??'")
elif randy() == 5:
    think_hold()
    print("I'd say ask again later, but honestly, just go away")
elif randy() == 6:
    think_hold()
    print('Shit yeah! What a great idea!')
elif randy() == 7:
    think_hold()
    print("You can get a hell of a good look at a T-Bone steak by sticking your head up a bull's ass, but wouldn't you rather take the butcher's word for it?")
elif randy() == 8:
    think_hold()
    print("What you’ve just said is one of the most insanely idiotic things I have ever heard. At no point in your rambling, incoherent response were you even close to anything that could be considered a rational thought.\nEveryone in this room is now dumber for having listened to it.\nI award you no points, and may God have mercy on your soul.")
elif randy() == 9:
    think_hold()
    print('I think you might just have something there!')
elif randy() == 10:
    think_hold()
    print('You the real MVP!')
else:
    print('Our apologies, there was a technical problem with the 8-ball.  Please try again later. ')
print('Thanks for playing',nom_de_guerre())



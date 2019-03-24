# -*- coding: utf-8 -*-

'''
This is under construction, still

'''

# madlib story using Python 3.5
# I'll be writing one in Python 2.x in the future, for just for fun.



import time, sys; 



def newline():
    print("\n");

vowels = ('a','e','i','o','u','A','E','I','O','U')

# function to determine first letter of the input, to choose "a" or "an"
# that comes before the user's word
def aan1():  # for word1 only
    if word1.startswith(vowels): 
        print("an", end=" ");
    else:
        print("a", end=" ");

def countdown():
    countdown = 3;
    while (countdown > 0):
        print("...", sep = " ");
        time.sleep(0.5)
        countdown -= 1;

newline(); newline();

initial_agreement = input("Hello!  would you like to create a story together? \n Type y for yes, or n for no.\n ")

if (initial_agreement == "y"):
    print("Great!  Let's get started!")
    countdown();
else:
    print("OK, bye!.");
    newline();
    KeyboardInterrupt();
    

#begin user input section
print("\n I'm going to ask you for a word, then you type your word and press enter.");
print("After we do that several times, I'll randomly put those words into a story."); 
word1 = input("\n First word:  Name verb (something you do):  \n");
word2 = input("\n Great.  Now give me an adjective (a word that describes something):  \n"); 
word3 = input("\n How about a another adjective (description word):   \n");
word4 = input("\n Now, name a thing:  \n");
word5 = input("\n Another verb, please (something you do):  \n");
word6 = input("\n And another verb:  \n");
word7 = input("\n Name an emotion, or feeling, that you express to someone (good or bad):  \n");
word8 = input("\n Another noun, please (a thing):  \n");
word9 = input("\n A verb (something you do: \n");
word10 = input("\n And another verb: \n");
word11 = input("\n A tool, or something useful in a tricky situation: \n");
word12 = input("\n A thing, but in plural form (more than one): \n");
word13 = input("\n Another thing, in plural form (more than one): \n");
word14 = input("\n Adjective (a word that describes something), but something bad: \n");
word15 = input("\n A verb (something you do): \n");
word16 = input("\n Something you say to someone you're arguing with (1-5 words): \n");
word17 = input("\n A verb ending in 'ing' (like running, instead of run): \n");
word18 = input("\n Another verb, ending in 'ing': \n");
word19 = input("\n A verb (something you do): \n");
word20 = input("\n An adjective, ending in 'ly' (like beautifully, stupidly, quickly, etc.): \n");
word21 = input("\n And, lastly... another verb (something you do): \n");





# story time. 
newline();
print("Please wait while I put our story together"); 
time.sleep(1);
newline(); countdown();


'''
print("\n Once upon ", end="") 
aan1();
print(word1, end="");
print(" there was a dog that would always " + word2 + ".");
print("This dog was from " + word3 + ".");

'''

newline();

print("HOW TO DEAL WITH DIFFICULT PEOPLE");
print("By you and me");

newline();

print("1. You have to remember to " + word1 + ".");
print("It's the number one step in dealing with 'unreasonable' people. ");
print("Everyone wants to feel " + word2 + ".");
print("No progress can take place until the other person feels acknowledged.");
print("While you're listening, really focus on what the other person is saying, not what you want to say next.");

newline();

print("2.  Stay " + word3 + ".");
print("When a situation is emotionally charged, it's easy to get caught up in the ", end = "");
print(word4, end = "");
print(" of the moment.  \nMonitor your breathing. Try to take some slow, deep breaths.");

newline();
input("Press enter to continue");
newline();

print("3.  Don’t " + word5 + ".");
print("You don't know what the other person is going through.  ");

newline();

print("4.  " + word6 + " respect and dignity toward the other person. ");
print("No matter how a person is treating you, showing " + word7, end = "");
print(" will not help productively resolve the situation. ");

newline();

print("5.  Look for the hidden " + word8 + "." );
print("What is this person really trying to gain? What is this person trying to " + word9 + "?");
print("Look for others around you who might be able to help. ");
print("If you’re at work and there’s an irate customer, quickly " + word10, end = "");
print(" to see if a " + word11 + " is close by. ");

newline();
input("Press enter to continue the story.");
newline();

print("6.  Don't demand " + word12 + " or " + word13 + ".");
print("For example, telling someone who's upset to be quiet and calm down ", end = "");
print("will just make him or her " + word14 + ".");
print("  Instead, ask the person what they are upset about, and allow them to " + word15 + ".");

newline();

print("7.  Saying, 'I understand,' usually makes things worse. Instead, say '" + word16 + "."); 

newline();

print("8.  Avoid " + word17 + ", as this may look like you are " + word18 + "the person.");
print("Similarly, humor can sometimes lighten the mood, but more often than not,");
print("it’s risky and it may " + word19 + ".");

newline();

print("9.  Don’t act " + word20 + ". This might be tough.");
print("You’re naturally not enjoying the other person saying nasty things or things that you know aren’t true.");
print("You’re going to want to " + word21 + " yourself.");
print("But the other person is so emotionally revved up, it’s probably not going to help. ");
print("Remember, this is not about you. Don’t take it personally, and remind yourself: ");
print("Hurt people hurt people.  You can help by showing that you care."); 

newline();
input("Press enter to continue...");
newline();

print("Thank you for playing!  Watch for more stories coming in the future!");

time.sleep(5);

exit();


'''
ADD THIS HELP TEXT, ALSO.
ALLOW THE USER TO TYPE A CHARACTER / SEQUENCE TO HAVE HELP SHOW ON COMMAND, WHENEVER THEY'D LIKE.

        <div id = 'helpDiv'> 
            <hr id='helpDivider'/>
            <h3>HELP & HINTS</h3><br/>
            <ul id='helpList'>
                <li>TIPS:  think outside the box!  With each answer, think of 
                    scenarios, groups, places and cultures that are not common to you. 
                <li>NOUN: a person, place or thing.</li>
                <li>-  Examples:  janitor, ball, house, bathroom, ocean, 
                    dog, fever... </li><br/><br/>
                <li>PLURAL NOUN: A person, place or thing, but <em>more than one</em>.</li>
                <li>-  Examples:  janitors, balls, houses, bathrooms, 
                    oceans, dogs... </li><br/><br/>
                <li>ADJECTIVE:  A word that describes a noun.  
                <li>-  Examples:  fast, hairy, tired, insane, wonderful, 
                    shiny...</li><br/><br/>
                <li>VERB:  An action word.  An action you do, or something that is done.
                <li>-  Hint: DO NOT put "ing" , "s" or "es" on the end.  
                       (unless that's how it normally is, like "guess, pass, etc...") 
                    </li>
                <li>-  Examples:  run, discover, blow, press, yell, think, call
                    </li><br/><br/>
                <li>VERB ENDING IN "ING":    
                <li>-  Examples:  running, discovering, blowing, pressing, 
                    yelling, galavanting, hallucinating, criticizing, farting, unicycling, ... </li><br/><br/>
            </ul>



'''










newline();
newline();


# end program



'''
NOTES: 
*  make a help section: 
*  for places, include the word "the".  ex: the hallway, etc.
*  make all nouns have condition: if first letter is consonant, use "a", if vowel, use "an".

'''




# IPND Stage 2 Final Project

difficulty = raw_input('Please select a game difficulty by typing it in!\nPossible choices include easy, medium, and hard.   \n\n')
print "\n\nYou have chosen " + difficulty + "  !" 
print "\nDepending on your answer to the previous question, you are going to read about data mining, machine learning or deep learning.\nGood luck!\n"

easy = "Data __1__ can be considered a superset of many different methods to extract __2__ from data. It might involve traditional statistical methods and machine learning. Data mining applies methods from many different areas to identify previously unknown __3__ from data. This can include statistical __4__, machine learning, text analytics, time series analysis and other areas of analytics. Data mining also includes the study and practice of data storage and data __5__."
easy_answer = ["mining", "insights",  "patterns",  "algorithms",  "manipulation"]

medium = "The main difference with machine learning is that just like statistical models, the goal is to understand the structure of the data, fit theoretical __1__ to the data that are well understood. So, with statistical models there is a __2__ behind the model that is mathematically proven, but this requires that data meets certain strong __3__ too. Machine learning has developed based on the ability to use computers to probe the data for structure, even if we do not have a theory of what that structure looks like. The test for a machine learning model is a __4__ error on new data, not a theoretical test that proves a null hypothesis. Because machine learning often uses an __5__ approach to learn from data, the learning can be easily automated. Passes are run through the data until a robust pattern is found."
medium_answer = ["distributions", "theory", "assumptions", "validation", "iterative"]

hard ="Deep learning combines advances in computing power and special types of __1__ networks to learn complicated patterns in large amounts of data. Deep learning techniques are currently state of the art for identifying __2__ in images and words in sounds. Researchers are now __3__ to apply these successes in pattern __4__ to more complex tasks such as automatic language __5__, medical diagnoses and numerous other important social and business problems."
hard_answer = ["neural", "objects", "looking", "recognition",  "translation"]

sub = ["__1__", "__2__", "__3__", "__4__", "__5__"]


#this procedure helps us to avoid repetition in our code
def selectdif(difficulty):
    if difficulty == 'easy':
        print easy
        return easy, easy_answer
    if difficulty == 'medium':
        print medium
        return medium, medium_answer
    if difficulty == 'hard':
        print hard
        return hard, hard_answer
    
level_string, answer_string = selectdif(difficulty)
  
#this procedure check if the expression is correct
def play_game(level_string, answer_string):
    guesses = raw_input('\nplease inform how many guesses do you want to have    \n')
    print "\nYou will get " + guesses + " guesses per problem"
    i = 0 #index
    c = 0 #count
    d = int(guesses)

    while(i<=5 or c <= d):
        guess = raw_input ("\nType in a guess for blank  \n" + str(i+1) )
        if guess==answer_string[i]:
           level_string = level_string.replace(sub[i], answer_string[i])
           print "\nGreat job, This is the correct answer.\n"
           print level_string
           i = i + 1
        else:
            print "\n\nThis is not the correct answer, please try again."
            c = c + 1
        if(c>d or i==5):
            break
    if (c >= d):
        print "\nsorry, game over."
    if (i >= 5):
        print "\nCongratulations, you have successfully answered the quiz."
     
        
play_game(level_string, answer_string)

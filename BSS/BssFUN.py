import random
import os
import fontstyle


def foody_table():
    num = int(input("Enter the number of people/animals:\n"))
    namelist = []
    foodlist = []

    for i in range(0, num):
        name = input(f"Enter the name here:\n")
        food = input(f"Enter food eaten by {name}:\n")
        namelist.append(name)
        foodlist.append(food)

    for i in range(0, num):
        print(f"{namelist[i]} eats {foodlist[i]}")


def guess_game_v5():
    os.system("CLS")
    num = random.randint(1, 100)
    guess = 1
    print("You have to guess a number between 1 to 100\n You will only get 9 chances!\n Enjoy :-)")

    while (guess <= 9):
        guessed_number = int(input("Enter the number:\n"))
        if guessed_number == num:
            congo = fontstyle.apply(
                "Congratulations!\nYou have guessed the number!", "bold/italic/white/yellow_bg")
            print(congo)
            print(f"You took {9-guess} turns!")
            guess = guess + 1
            break

        elif guessed_number < num:
            print(f"Turns remaining: {9-guess}")
            smaller = fontstyle.apply(
                "The number you have entered is smaller than the number to be guessed!", "bold/italic/blue")
            print(smaller)
            guess = guess + 1
            continue

        elif guessed_number > num:
            print(f"Turns remaining: {9-guess}")
            greater = fontstyle.apply(
                "The number you have entered is greater than the number to be guessed!", "bold/italic/red")
            print(greater)
            guess = guess + 1
            continue

        else:
            exit()

    if guess > 9:
        lose = fontstyle.apply("Game Over!", "bold/italic/yellow")
        print(lose)
        print("The number was", num)
        input("Press Enter to continue:\n")


def num_fight():
    while True:
        os.system("CLS")
        ai = random.randint(-100, 101)
        score = 0
        player_print = fontstyle.apply(
            "Enter your number here [from -100 to 100] [let's see who wins...]:", "bold/italic/purple")
        print(player_print)
        inp = int(input())

        if ai > inp:
            greater = fontstyle.apply("HEHE, You lost! [score -1]", "bold/red")
            print(greater)
            score -= 1
            print("Your opponent guessed", ai)
            inp = input("Press Enter to continue of Q to quit")
            inp = inp.upper()
            if inp == "":
                continue
            elif inp == "Q":
                break
            else:
                print()

        elif ai < inp:
            smaller = fontstyle.apply("You Won! [score  +1]", "bold/green")
            print(smaller)
            score += 1
            print("Your opponent guessed", ai)
            inp = input("Press Enter to continue of Q to quit")
            inp = inp.upper()
            if inp == "":
                continue
            elif inp == "Q":
                break
            else:
                print()

        else:
            equal = fontstyle.apple("TIE [score +0]", "bold/blue")
            print(equal)
            print("Your opponent guessed", ai)
            inp = input("Press Enter to continue of Q to quit")
            inp = inp.upper()
            if inp == "":
                continue
            elif inp == "Q":
                break
            else:
                print()


def calcy():
    choice3 = int(input("Enter your operation here\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Remainder\n 6. Exponential Powers\n 7. Square\n 8. Cube\n"))
    num1 = float(input("Enter first number:\n"))
    num2 = float(input("Enter second number:\n"))
    if choice3 == 1:
        print(num1, "+", num2, "=", format(num1 + num2, '.2f'))
    elif choice3 == 2:
        print(num1, "-", num2, "=", format(num1 - num2, '.2f'))
    elif choice3 == 3:
        print(num1, "x", num2, "=",format(num1 * num2, '.2f'))
    elif choice3 == 4:
        print(num1, "÷", num2, "=", format(num1 / num2, '.2f'))
    elif choice3 == 5:
        print("The remainder of", num1, "and", num2, "is", int(num1 % num2))
    elif choice3 == 6:
        try:
            print(num1, "raised to the power of", num2, "=", num1 ** num2)
        except OverflowError:
            result_too_large = fontstyle.apply(
                "Result too LARGE!", "bold/italic/red")
            print(result_too_large)
    elif choice3 == 7:
        try:
            print("The square of", num1, "=", num1 ** 2)
            print("The square of", num2, "=", num2 ** 2)
        except OverflowError:
            result_too_large = fontstyle.apply(
                "Result too LARGE!", "bold/italic/red")
            print(result_too_large)

    elif choice3 == 8:
        try:
            print("The cube of", num1, "=", num1 ** 3)
            print("The cube of", num2, "=", num2 ** 3)
        except OverflowError:
            result_too_large = fontstyle.apply(
                "Result too LARGE!", "bold/italic/red")
            print(result_too_large)


def quizy():
    numc = random.randint(1, 4)
    congo1 = fontstyle.apply(
        "Right answer! You will get 10M rupees!", "bold/italic/green")
    congo2 = fontstyle.apply(
        "Wrong answer! You may better pay Rs. 100k to BSS!", "bold/italic/red")

    if numc == 1:
        print("Which is the largest continent in the world?")
        print("a. Antarctica")
        print("b. Asia")
        print("c. America")
        print("d. South Australia")
        answer = input("")
        if answer == "b":
            print(congo1)
        else:
            print(congo2)

    elif numc == 2:
        print("Name the only non-metal which is found in liquid state.")
        print("a. Mercury")
        print("b. Bromine")
        print("c. Water")
        print("d. Hydroxide")
        answer = input("")
        if answer == "b":
            print(congo1)
        else:
            print(congo2)

    elif numc == 3:
        print("Name the only metal which is found in liquid state.")
        print("a. Mercury")
        print("b. Molten Magma")
        print("c. Molten Iron")
        print("d. Liquisteel")
        answer = input("")
        if answer == "a":
            print(congo1)
        else:
            print(congo2)

    elif numc == 4:
        print("Which of the following is a semiaquatic mammal?")
        print("a. Killer Whale")
        print("b. Tiger Shark")
        print("c. Hippopotamus")
        print("d. both a and b ")
        answer = input("")
        if answer == "c":
            print(congo1)
        else:
            print(congo2)

    elif numc == 5:
        print("Which of the following trees have roots above the ground?")
        print("Mango Tree")
        print("b. Spade cactus")
        print("c. Mangrove tree")
        print("d. there's no tree which grow roots above the ground")
        answer = input("")
        if answer == "c":
            print(congo1)
        else:
            print(congo2)

    elif numc == 6:
        print("Who discovered the vaccine for small pox?")
        print("a. Poxes Vacenito")
        print("b. Galileo Galilei")
        print("c. Edward Jenner")
        print("d. Louis Pasteur")
        answer = input("")
        if answer == "c":
            print(congo1)
        else:
            print(congo2)

    elif numc == 7:
        print("Wine is made from __")
        print("a. grapes")
        print("b. alchohol")
        print("c. Whisky")
        print("d. mango")
        answer = input("")
        if answer == "a":
            print(congo1)
        else:
            print(congo2)


def animals():
    os.system("CLS")
    while(True):
        cat = "The cat is a domestic species of small carnivorous mammal. It is the only domesticated species in the family Felidae and is often referred to as the domestic cat to distinguish it from the wild members of the family."
        dog = "The dog or domestic dog is a domesticated descendant of the wolf which is characterized by an upturning tail. The dog is derived from an ancient, extinct wolf, and the modern wolf is the dog's nearest living relative. "
        cow = "Cattle are large, domesticated, cloven-hooved herbivores. They are a prominent modern member of the subfamily Bovinae and the most widespread species of the genus Bos. Adult females are referred to as cows and adult males are referred to as bulls."
        snake = "Snakes are elongated, limbless, carnivorous reptiles of the suborder Serpentes. Like all other squamates, snakes are ectothermic, amniote vertebrates covered in overlapping scales."
        salamander = "Salamanders are a group of amphibians typically characterized by their lizard-like appearance, with slender bodies, blunt snouts, short limbs projecting at right angles to the body, and the presence of a tail in both larvae and adults. All ten extant salamander families are grouped together under the order Urodela"
        elephant = "Elephants are the largest existing land animals. Three living species are currently recognised: the African bush elephant, the African forest elephant, and the Asian elephant. They are an informal grouping within the proboscidean family Elephantidae."
        eagle = "Eagle is the common name for many large birds of prey of the family Accipitridae. Eagles belong to several groups of genera, some of which are closely related. Most of the 60 species of eagle are from Eurasia and Africa"
        shark = "Sharks are a group of elasmobranch fish characterized by a cartilaginous skeleton, five to seven gill slits on the sides of the head, and pectoral fins that are not fused to the head. Modern sharks are classified within the clade Selachimorpha and are the sister group to the rays."
        humans = "Humans are the most abundant and widespread species of primate, characterized by bipedalism and large, complex brains. This has enabled the development of advanced tools, culture, and language."

        cath = "बिल्ली छोटे मांसाहारी स्तनपायी की घरेलू प्रजाति है। यह फेलिडे परिवार में एकमात्र पालतू प्रजाति है और इसे अक्सर परिवार के जंगली सदस्यों से अलग करने के लिए घरेलू बिल्ली के रूप में जाना जाता है।"
        dogh = "कुत्ता या घरेलू कुत्ता भेड़िये का एक पालतू वंशज है जो एक उलटी पूंछ की विशेषता है। कुत्ता एक प्राचीन, विलुप्त भेड़िये से निकला है, और आधुनिक भेड़िया कुत्ते का निकटतम जीवित रिश्तेदार है।"
        cowh = "मवेशी बड़े, पालतू, कटे हुए खुर वाले शाकाहारी होते हैं। वे सबफ़ैमिली बोविना के एक प्रमुख आधुनिक सदस्य हैं और जीनस बोस की सबसे व्यापक प्रजाति हैं। वयस्क मादा को गाय और वयस्क नर को बैल कहा जाता है।"
        snakeh = "सांप उप-वर्ग सर्पों के लंबे, अंगहीन, मांसाहारी सरीसृप हैं। अन्य सभी स्क्वैमेट्स की तरह, सांप एक्टोथर्मिक होते हैं, एमनियोट कशेरुक अतिव्यापी तराजू में ढके होते हैं।"
        salamanderh = "सैलामैंडर उभयचरों का एक समूह है जो आमतौर पर उनकी छिपकली जैसी उपस्थिति की विशेषता होती है, जिसमें पतले शरीर, कुंद थूथन, शरीर के समकोण पर प्रक्षेपित छोटे अंग और लार्वा और वयस्कों दोनों में एक पूंछ की उपस्थिति होती है। सभी दस मौजूदा समन्दर परिवारों को यूरोडेल के क्रम में एक साथ समूहीकृत किया गया है"
        elephanth = "हाथी सबसे बड़े मौजूदा भूमि जानवर हैं। तीन जीवित प्रजातियों को वर्तमान में मान्यता प्राप्त है: अफ्रीकी झाड़ी हाथी, अफ्रीकी वन हाथी और एशियाई हाथी। वे सूंड परिवार एलिफेंटिडे के भीतर एक अनौपचारिक समूह हैं।"
        eagleh = "ईगल परिवार Accipitridae के शिकार के कई बड़े पक्षियों का सामान्य नाम है। ईगल पीढ़ी के कई समूहों से संबंधित हैं, जिनमें से कुछ निकट से संबंधित हैं। ईगल की 60 प्रजातियों में से अधिकांश यूरेशिया और अफ्रीका से हैं"
        sharkh = "शार्क एक कार्टिलाजिनस कंकाल, सिर के किनारों पर पांच से सात गिल स्लिट्स, और चोटीदार पंख जो सिर से जुड़े नहीं हैं, की विशेषता इलास्मोब्रांच मछली का एक समूह है। आधुनिक शार्क को क्लैड सेलाचिमोर्फा के भीतर वर्गीकृत किया गया है और वे किरणों की बहन समूह हैं।"
        humansh = "मनुष्य प्राइमेट की सबसे प्रचुर और व्यापक प्रजाति है, जो द्विपादवाद और बड़े, जटिल दिमाग की विशेषता है। इसने उन्नत उपकरणों, संस्कृति और भाषा के विकास को सक्षम बनाया है।"

        name = input(
            "Choose your animal:\n cat\n dog\n cow\n snake\n salamander\n elephant\n eagle\n shark\n humans\n")
        l = input("Choose your language:\n H[HINDI]\n E[ENGLISH]\n")
        name = name.lower()
        l = l.upper()
        if name == "cat" and l == "H":
            print(cath)
        elif name == "cat" and l == "E":
            print(cat)
        elif name == "dog" and l == "H":
            print(dogh)
        elif name == "dog" and l == "E":
            print(dog)
        elif name == "cow" and l == "H":
            print(cowh)
        elif name == "cow" and l == "E":
            print(cow)
        elif name == "snake" and l == "H":
            print(snakeh)
        elif name == "snake" and l == "E":
            print(snake)
        elif name == "salamander" and l == "E":
            print(salamander)
        elif name == "salamander" and l == "H":
            print(salamanderh)
        elif name == "salamander" and l == "E":
            print(elephant)
        elif name == "elephant" and l == "H":
            print(elephanth)
        elif name == "elephant" and l == "E":
            print(elephant)
        elif name == "eagle" and l == "H":
            print(eagleh)
        elif name == "eagle" and l == "E":
            print(eagle)
        elif name == "shark" and l == "H":
            print(sharkh)
        elif name == "shark" and l == "E":
            print(shark)
        elif name == "humans" and l == "H":
            print(humansh)
        elif name == "humans" and l == "E":
            print(humans)
        else:
            print("The entered name, language or both are WRONG!\n Please try again.")
        inp1 = input("Press enter to continue or Q to quit!:\n")
        if inp1 == "":
            continue
        elif inp1 == "Q":
            exit()
        else:
            hehe = fontstyle.apply(
                "|---Please come again soon---|", "bold/Italic/black")
            print(hehe)



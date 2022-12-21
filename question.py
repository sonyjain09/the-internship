import requests
import random
import html

urlNS = (
    "https://opentdb.com/api.php?amount=50&category=17&difficulty=medium&type=multiple"
)

NS = requests.get(urlNS)

urlNSE = (
   "https://opentdb.com/api.php?amount=20&category=17&difficulty=easy&type=multiple"
)
NSE = requests.get(urlNSE)


urlVG = (
    "https://opentdb.com/api.php?amount=50&category=15&difficulty=medium&type=multiple"
)
VG = requests.get(urlVG)

urlTV = (
    "https://opentdb.com/api.php?amount=50&category=14&difficulty=easy&type=multiple"
)
TV = requests.get(urlTV)


urlG = (
    "https://opentdb.com/api.php?amount=25&category=22&difficulty=medium&type=multiple"
)
G = requests.get(urlG)

urlH = (
    "https://opentdb.com/api.php?amount=25&category=23&difficulty=medium&type=multiple"
)
H = requests.get(urlH)

urlHE = (
    "https://opentdb.com/api.php?amount=50&category=23&difficulty=easy&type=multiple"
)
HE = requests.get(urlHE)

urlGK = "https://opentdb.com/api.php?amount=50&category=9&difficulty=hard&type=multiple"
GK = requests.get(urlGK)

urlGKE = "https://opentdb.com/api.php?amount=50&category=9&difficulty=easy&type=multiple"
GKE = requests.get(urlGKE)


def createList(r1, r2):
    return list(range(r1, r2 + 1))


available_questions = {
    "NS": createList(0, 49), #50 natural science questions on medium difficulty
    "NSE": createList(0,19), #20 natural science questions on easy difficulty
    "VG": createList(0, 49), #50 video game questions on medium pools with TV
    "TV": createList(0,49), #50 TV questions on TV pools with vg
    "G": createList(0, 24), #25 geography questions pools with H, he
    "H": createList(0, 24), #25 History questions pools with g, he
    "HE": createList(0,49), #50 History questions on easy pools with h, g
    "GK": createList(0, 49),#50 gen knowledge pools with gke
    "GKE": createList(0,49) #50 gen knowledge easy pools with gk
}


def cleanUnicode(question, options):
    for i in range(4):
        options[i] = html.unescape(options[i])
    question = html.unescape(question)

def getQuestion(category, category_name):
    
    questionNum = random.choice(available_questions[category_name])
    question = category.json()["results"][questionNum]["question"]
    correct_string = category.json()["results"][questionNum]["correct_answer"]
    options = category.json()["results"][questionNum]["incorrect_answers"]
    correct_answer_index = random.randint(0, 3)
    options.insert(correct_answer_index, correct_string)

    for i in range(4):
        options[i] = html.unescape(options[i])

    question = html.unescape(question)

    print("\n")
    print(question)
    print(options)

    player_answer = input("Type A,B,C,D or 1,2,3,4 `for your corresponding answer\n")
    player_answer = player_answer.lower()
    player_answer_index = None
    while player_answer_index == None:
        match player_answer:
            case "a":
                player_answer_index = 0
            case "b":
                player_answer_index = 1
            case "c":
                player_answer_index = 2
            case "d":
                player_answer_index = 3
            case "1":
                player_answer_index = 0
            case "2":
                player_answer_index = 1
            case "3":
                player_answer_index = 2
            case "4":
                player_answer_index = 3
            case other:
                player_answer = input("Invalid input. Type A,B,C,D or 1,2,3,4 for your corresponding answer\n")

    print("\n")

    if player_answer_index == correct_answer_index:
        print("    ****Correct****    ")
    else:
        print("    ****Incorrect****    ")
        print("Correct Answer: " + correct_string)

    print("\n")

    available_questions[category_name].remove(questionNum)



game = True

while game:
    ind = input(
        "What category are you in?\n1) Natural Science\n2) Entertainment\n3) History and Geography\n4) General Knowledge\n"
    )
    category = None
    category_name = None
    categorylen = 0
    while category == None and category_name == None:
        match ind:
            case "1":
                if len(available_questions["NS"]) == 0 and len(available_questions["NSE"]) == 0:
                    print("No more unique Natural Science Questions. Questions will be repeated now")
                    available_questions["NS"] = createList(0,49)
                    available_questions["NSE"] = createList(0,19)
                while categorylen == 0:
                    horg = random.randint(0, 1)
                    match horg:
                        case 0:
                            category = NS
                            category_name = "NS"
                        case 1:
                            category = NSE
                            category_name = "NSE"
                    categorylen = len(available_questions[category_name])
            case "2":
                if len(available_questions["VG"]) == 0 and len(available_questions["TV"]) == 0:
                    print("No more unique Entertainment Questions. Questions will be repeated now")
                    available_questions["VG"] = createList(0,49)
                    available_questions["TV"] = createList(0,49)
                while categorylen == 0:
                    horg = random.randint(0, 1)
                    match horg:
                        case 0:
                            category = VG
                            category_name = "VG"
                        case 1:
                            category = TV
                            category_name = "TV"
                    categorylen = len(available_questions[category_name])
            case "3":
                if len(available_questions["H"]) == 0 and len(available_questions["G"]) == 0 and len(available_questions["HE"]) == 0:
                    print("No more unique History and Geography Questions. Questions will be repeated now")
                    available_questions["H"] = createList(0,24)
                    available_questions["G"] = createList(0,24)
                    available_questions["HE"] = createList(0,49)
                while categorylen == 0:
                    horg = random.randint(0, 2)
                    match horg:
                        case 0:
                            category = H
                            category_name = "H"
                        case 1:
                            category = G
                            category_name = "G"
                        case 2:
                            category = HE
                            category_name = "HE"
                    categorylen = len(available_questions[category_name])
            case "4":
                if len(available_questions["GK"]) == 0 and len(available_questions["GKE"]) == 0:
                    print("No more unique General Knowledge Questions. Questions will be repeated now")
                    available_questions["GK"] = createList(0,49)
                    available_questions["GKE"] = createList(0,49)
                while categorylen == 0:
                    horg = random.randint(0, 1)
                    match horg:
                        case 0:
                            category = GK
                            category_name = "GK"
                        case 1:
                            category = GKE
                            category_name = "GKE"
                    categorylen = len(available_questions[category_name])
            case other:
                ind = input("Invalid input. What category are you in?\n1) Natural Science\n2) Entertainment\n3) History and Geography\n4) General Knowledge\n")
    getQuestion(category, category_name)

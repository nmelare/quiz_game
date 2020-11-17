import json
import time

questions = "questions"

def askQuestion(question):
    print(question)
    choise = input("Insira sua resposta entre a, b, c, d, e: ")
    while (True):
        if choise.lower() in ["a","b","c","d","e"]:
            return choise
        else:
            print("Escolha invalida, escolha de novo")
            choise = input("Insira sua resposta entre a, b, c, d, e: ")

def loadQuestions(filename):
    questions = None
    with open(filename, "r") as read_file:
        questions = json.load(read_file)
    return (questions)

def scoreCheck(key, meta) -> int:
    actual = meta["rightAnswer"]
    easy = "easy"
    medium = "medium"
    hard = "hard"
    if meta["user"].lower() == actual.lower():
        print("Q.{0} Correto, parabéns!\n".format(key))
        if easy == meta["level"]:
            return 5
        elif medium == meta["level"]:
            return 10
        else:
            return 15
    else:
        print("Q.{0} Está errada!\n".format(key))
        print ("A resposta correta é: " + meta["info"] + "\n")
        time.sleep(5)
        return 0

def scoreCount(questions):
    score = 0
    for key, meta in questions.items():
        questions[key]["user"] = askQuestion(meta["question"])
        score += scoreCheck(key, meta)
    print("Pontuação: ", score)
    if score >= 60:
        print("Parabéns! Você é um ninja conhecedor da comunidade LGBTQI+")
    else:
        print("Parece que você é um pequeno gafanhoto aprendendo sobre a comunidade LGBTQI+. Jogue de novo para aprender um pouco mais!")

def playQuiz():
    question = loadQuestions('quiz/'+questions+'.json')
    scoreCount(question)

playQuiz()
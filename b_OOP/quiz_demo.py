# Question

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
        
    def checkAnswer(self, answer):
        return self.answer == answer
    
class Quiz():
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0 # listenin ilk elemanı 0. index --> random ??
    
    def getQuestion(self):
        return self.questions[self.questionIndex] # asagıdaki quiz. yerine self. çünkü bilmiyoruz gelecek
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1} : {question.text}")
        
        for q in question.choices:
            print('- '+ q)
        
        answer = input('cevap: ')
        #print(question.checkAnswer(answer))
        self.guess(answer)
        self.loadQuestion()
        
    def guess(self, answer):
        question = self.getQuestion()  
        
        if question.checkAnswer(answer):
            self.score +=1
            
        self.questionIndex +=1
        #self.displayQuestion()
         
    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()
            
            
    def showScore(self):
        print('score: ', self.score)
        
    def displayProgress(self):
        totalQuestion = len(self.questions) # soru sayısı
        questionNumber = self.questionIndex + 1 # kaçıncı sorudayız
        
        if questionNumber > totalQuestion:
            print('Quiz bitti')
        else:
            print(f'  Question {questionNumber} of {totalQuestion}  '.center(100, '*'))
        
            
q1 = Question('En iyi programlama dili hangisidir?', ['C#','Python','Javascrit','Java'], 'Python') # questionIndex = 0
q2 = Question('En popüler programlama dili hangisidir?', ['Python','C#','Javascrit','Java'], 'Javascript') # questionIndex = 1
q3 = Question('En çok kazandıran programlama dili hangisidir?', ['Java','Python','Javascrit','C#'], 'Java') # questionIndex = 2
#q4 
#q5

# sorular listeye alınacak ve yeni Quiz class a gönderilecek liste = [q1, q2, q3]
questions = [q1, q2, q3] # list  of questions

quiz = Quiz(questions) # quiz objesi questions tutuyor. 
# question = quiz.questions[quiz.questionIndex] # yerine getQuestion 

# question = quiz.getQuestion() # yerlerine displayQuestion
# print(question.text)

#quiz.displayQuestion()
quiz.loadQuestion()

# print(q1.checkAnswer('Python'))  # Quiz sınıfı oluşmadan evvel
# print(q2.checkAnswer('Python'))
# print(q3.checkAnswer('Python'))


 ## https://www.btkakademi.gov.tr/portal/course/player/deliver/sifirdan-ileri-seviye-python-programlama-5877
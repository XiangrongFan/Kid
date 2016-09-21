import random
import datetime

def run():
 type = random.randint(1,2)
 if type == 1: ## plus
    a=random.randint(1,100)
    b=random.randint(1,100)
    while a+b > 100 :
        b = random.randint(1,100)
    stat=str(a)+"+"+str(b)+"="
    answer = a+b
 else: ## minus
    a=random.randint(1,100)
    b = random.randint(1,100)
    while a-b<=0 :
        b = random.randint(1,100)
    stat=str(a)+"-"+str(b)+"="
    answer=a-b

 childAnswer = input(stat)

 if childAnswer == answer:
    print "Correct"
 else:
    print "Wrong, correct answer is ",answer

times = 0
a = datetime.datetime.now()
while times < 10:
    run()
    times = times+1
b = datetime.datetime.now()
print "used time" , (b-a)
import time
import random
lines = [
    "The beauty of nature is unmatched, and there is nothing quite like a peaceful walk through the woods on a crisp morning.",
    "Learning new programming languages opens up endless possibilities for creativity and problem-solving in the tech world.",
    "There’s always something magical about watching the first snowflakes of the season fall gently to the ground, covering everything in a blanket of white.",
    "The joy of reading a good book is one of life’s simplest pleasures, and it has the power to transport you to another world.",
    "Traveling to new places broadens your horizons and gives you a deeper understanding of different cultures and ways of life.",
    "Greatness is not achieved overnight, but through consistent effort, determination, and a passion for what you do.",
    "A positive attitude can turn even the most challenging situations into opportunities for growth and learning.",
    "Technology has made communication easier than ever, allowing people from all corners of the world to connect and collaborate effortlessly.",
    "Taking time for self-care and mental health is crucial, as it helps recharge and maintain balance in a busy life.",
    "The world is full of amazing opportunities, and sometimes all it takes is a little courage to step out of your comfort zone and seize them."
]
def checkError(line,userinput):
    error=0
    for i in range(len(line)):
        try:
            if line[i]!=userinput[i]:
                error+=1
        except:
            error+=1
    return error
def checkspeed(time1,time2,userinput):
    timedelay=time2-time1
    time_round=round(timedelay,2)
    speed=len(userinput)/time_round
    return round(speed)


line= random.choice(lines)

print("\n***** Typing Speed Test *****\n")
print("Type the following sentence as accurately and quickly as possible:\n")
print(f"\"{line}\"\n")


time1=time.time()
userinput=input("Enter:  ")
time2=time.time()

mistakes=checkError(line,userinput)
speed=checkspeed(time1,time2,userinput)

print(f"\nTyping Speed: {speed} words per second (WPS)")
print(f"Mistakes: {mistakes} errors")
# Final message
if mistakes == 0:
    print("Great job! No mistakes. 🎉")
elif mistakes <= 3:
    print("Good job! Just a few errors. Keep practicing! 👍")
else:
    print("Keep practicing to improve your accuracy and speed! 💪")

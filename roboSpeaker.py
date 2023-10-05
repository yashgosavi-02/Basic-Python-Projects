import pyttsx3

if __name__ == '__main__':
    print("Welcome to Robo Speaker 1.1 created by Yash")
    system = pyttsx3.init()
    while True:
        x = input("Say Something = ")
        if x == "quit":
            system.say("Thankyou for using me!")
            system.runAndWait()
            break
        system.say(x)
        system.runAndWait()

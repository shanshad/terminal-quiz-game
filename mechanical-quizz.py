import random
question_set={
  "q1": {
    "question": "Which law of thermodynamics introduces the concept of entropy?",
    "options": "Choose one:\n1. Zeroth Law\n2. First Law\n3. Second Law\n4. Third Law",
    "ans": "Second Law",
    "copt": 3
  },
  "q2": {
    "question": "Which one of the following is a unit of pressure?",
    "options": "Choose one:\n1. Newton\n2. Pascal\n3. Watt\n4. Joule",
    "ans": "Pascal",
    "copt": 2
  },
  "q3": {
    "question": "In which process is there no heat exchange with the surroundings?",
    "options": "Choose one:\n1. Isothermal\n2. Adiabatic\n3. Isochoric\n4. Isobaric",
    "ans": "Adiabatic",
    "copt": 2
  },
  "q4": {
    "question": "Which instrument is used to measure the rotational speed of a shaft?",
    "options": "Choose one:\n1. Dynamometer\n2. Tachometer\n3. Thermometer\n4. Manometer",
    "ans": "Tachometer",
    "copt": 2
  },
  "q5": {
    "question": "Which of the following materials is most commonly used for making gears?",
    "options": "Choose one:\n1. Brass\n2. Cast Iron\n3. Copper\n4. Plastic",
    "ans": "Cast Iron",
    "copt": 2
  },
  "q6": {
    "question": "Which of these is a scalar quantity?",
    "options": "Choose one:\n1. Force\n2. Velocity\n3. Acceleration\n4. Energy",
    "ans": "Energy",
    "copt": 4
  },
  "q7": {
    "question": "What does a strain gauge measure?",
    "options": "Choose one:\n1. Pressure\n2. Temperature\n3. Deformation\n4. Velocity",
    "ans": "Deformation",
    "copt": 3
  },
  "q8": {
    "question": "Which of the following is a reversible process?",
    "options": "Choose one:\n1. Combustion\n2. Mixing of fluids\n3. Friction\n4. Isothermal expansion",
    "ans": "Isothermal expansion",
    "copt": 4
  },
  "q9": {
    "question": "Which machining operation uses a rotating tool to remove material?",
    "options": "Choose one:\n1. Turning\n2. Milling\n3. Planning\n4. Shaping",
    "ans": "Milling",
    "copt": 2
  },
  "q10": {
    "question": "Which of the following is not a type of welding?",
    "options": "Choose one:\n1. MIG\n2. TIG\n3. Casting\n4. Arc",
    "ans": "Casting",
    "copt": 3
  },
  "q11": {
    "question": "What is the SI unit of thermal conductivity?",
    "options": "Choose one:\n1. W/m·K\n2. J/kg·K\n3. N/m\n4. W/K",
    "ans": "W/m·K",
    "copt": 1
  },
  "q12": {
    "question": "Which of the following is a renewable energy source?",
    "options": "Choose one:\n1. Natural gas\n2. Coal\n3. Solar energy\n4. Petroleum",
    "ans": "Solar energy",
    "copt": 3
  },
  "q13": {
    "question": "Which of these processes increases the hardness of steel?",
    "options": "Choose one:\n1. Annealing\n2. Quenching\n3. Normalizing\n4. Tempering",
    "ans": "Quenching",
    "copt": 2
  },
  "q14": {
    "question": "What type of stress is produced when a material is pulled apart?",
    "options": "Choose one:\n1. Compressive\n2. Torsional\n3. Tensile\n4. Shear",
    "ans": "Tensile",
    "copt": 3
  },
  "q15": {
    "question": "Which component converts reciprocating motion into rotary motion?",
    "options": "Choose one:\n1. Gearbox\n2. Crankshaft\n3. Pulley\n4. Flywheel",
    "ans": "Crankshaft",
    "copt": 2
  },
  "q16": {
    "question": "Which principle does a hydraulic press work on?",
    "options": "Choose one:\n1. Pascal's Law\n2. Bernoulli's Principle\n3. Newton’s Law\n4. Boyle’s Law",
    "ans": "Pascal's Law",
    "copt": 1
  },
  "q17": {
    "question": "Which mechanism is used in reciprocating engines?",
    "options": "Choose one:\n1. Slider-crank\n2. Four-bar linkage\n3. Geneva mechanism\n4. Cam-follower",
    "ans": "Slider-crank",
    "copt": 1
  },
  "q18": {
    "question": "What is the function of a flywheel?",
    "options": "Choose one:\n1. Store kinetic energy\n2. Cool the engine\n3. Increase speed\n4. Lubricate parts",
    "ans": "Store kinetic energy",
    "copt": 1
  },
  "q19": {
    "question": "Which process is used to remove material using a high-speed rotating abrasive wheel?",
    "options": "Choose one:\n1. Turning\n2. Drilling\n3. Grinding\n4. Milling",
    "ans": "Grinding",
    "copt": 3
  },
  "q20": {
    "question": "Which type of gear is used to transmit motion between intersecting shafts?",
    "options": "Choose one:\n1. Helical gear\n2. Spur gear\n3. Bevel gear\n4. Worm gear",
    "ans": "Bevel gear",
    "copt": 3
  }
}

keys = list(question_set.keys())
random.shuffle(keys)
restart=0
print("*"*10)
print("WELCOME TO THE QUIZ GAME")
print("*"*10)
name=input("Player please input your name : ")
level=input("at what level you want to play (easy/medium/hard) : ").lower()
while restart==0:
    score=0
    count=0
    for i in keys:
        if level=="easy" and count==5:
            break
        elif level=="medium" and count==10:
            break
        elif level=="hard" and count==20:
            break
        print(question_set[i]["question"])
        print(question_set[i]["options"])
        count+=1
        while True:
            try:
                choice = int(input("Enter an option: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        if choice==question_set[i]["copt"]:
            print("Correct answer")
            score+=1
            print(f"your score is {score}/{count}\n")
        else:
            print("wrong answer")
            print(f"the correct anser is {question_set[i]["ans"]}")
            print(f"your score is {score}/{count}\n")
    restart=int(input("Enter 1 to exit 0 to restart : "))
print("the quizz ends here")
print(f"Your final score is {score} ")
if level=='easy':
    if score==5:
        print(f"you are a Genius {name}")
    elif score>=3:
        print(f"good job {name}")
    else:
        print("you have to work on your basics {name}")
elif level=='medium':
    if score==10:
        print(f"you are a Genius {name}")
    elif score>=6:
        print(f"good job {name}")
    else:
        print("you have to work on your basics {name}")
elif level=='hard':
    if score==20:
        print(f"you are a Genius {name}")
    elif score>=14:
        print(f"good job {name}")
    else:
        print(f"you have to work on your basics {name}")

from flask import Flask, render_template, request
app = Flask(__name__)

computations = []

@app.route("/")
def initial_page():
	return render_template("calculator_page.html", computations=computations)

@app.route("/", methods=['POST'])
def calculation():
	eq = request.form['equation']
    compute(str(eq))
    # if str(eq) != "":
	   # compute(str(eq))
	return render_template("calculator_page.html", computations=computations)

def compute(input):

    #list of chars that are accepted by the calculator
    # validChars = "0123456789/*-+."

    # #split the input string into a list of characters
    # inputList = [char for char in input];

    # #checks to see if input is valid
    # for char in inputList:
    #     if char not in validChars:
    #         return "Not a valid input"


    # computeStack = [];
    # while inputList != []:
    #     nextChar = inputList[-1]

    #     #if next character is a digit must check previous indices to find when the number ends
    #     if inputList[-1].isdigit(): 
    #         i = 0
    #         while i < len(inputList) and (inputList[-1-i].isdigit() or inputList[-1-i] == '.'):
    #             i += 1;
    #         nextChar = inputList[-i:]
    #     computeStack.append(nextChar)

    #     if len(computeStack) > 1:
    #         if computeStack[-2] == '*':
    #             lhs = "".join(computeStack.pop());
    #             computeStack.pop();
    #             rhs = "".join(computeStack.pop());
    #             computeStack.append([str(double(lhs)*double(rhs))])
    #         elif computeStack[-2] == '/':
    #             lhs = "".join(computeStack.pop());
    #             computeStack.pop();
    #             rhs = "".join(computeStack.pop());
    #             computeStack.append([str(double(lhs)/double(rhs))])
                
    #     inputList = inputList[:-i]
       

    # while len(computeStack) > 1:
    #     if computeStack[-2] == '+':
    #         lhs = "".join(computeStack.pop());
    #         computeStack.pop();
    #         rhs = "".join(computeStack.pop());
    #         computeStack.append([str(double(lhs)+double(rhs))])
    #     elif computeStack[-2] == '-':
    #         lhs = "".join(computeStack.pop());
    #         computeStack.pop();
    #         rhs = "".join(computeStack.pop());
    #         computeStack.append([str(double(lhs)-double(rhs))])
    # if len(computations) > 9:
    #     computations.pop();
    # computations.insert(0, input + " = " + str(computeStack[0][0]))

    # return computeStack[0][0]
    pass

#TODO:
#connect number/computation buttons to input box
#update below paragraphs based on input
	#hide empty paragraphs 
	#shift paragraphs down after each computation
	#show a max of the last 10 computations
#show error message if characters outside of 0,1,2,3,4,5,6,7,8,9,/,*,-,+ are entered into input
#if time add '(' and ')' to calculator
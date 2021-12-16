import addition
import Substration
import Multiplication
import dividation
def main():

    #a=0
    a=int(input(" 1.Addition \n 2.Substration \n 3.Multiplication \n 4.Divide \n"))
   
    if a == 1:
        print("You are select Addition of two numbers")
        addition.add()
    if a == 2:
        print("You are select Substration of two numbers")
        Substration.sub()
    if a == 3:
        print("You are select Multiplication of two numbers")
        Multiplication.mult()
    if a == 4:
        print("You are select Divide of two numbers ")
        dividation.div()
    if a > 4 :
        print("You are entered wrong number please select again !")
        main()
    if a < 1 :
        print("You are entered wrong number please select again !")
        main()
if __name__ == "__main__":
    print("!!Welcome to Jay Ganesh Calculator!!")
    print("Please select opreation")
    main()
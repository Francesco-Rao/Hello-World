##How do I use this to code?

print"how do I use this website to code?";

##FehrenheitConverter.py
##Fahrenheit to celsius converter
##By: Francesco Rao
##Formula: ((F -32)*(5/9))

def main():

    print "This program will convert tempertures from Fahrenheit to Celsius."

    print

    f = input ("Please enter a temperture in degrees fehrenheit: ")

    c = ((f - 32)*(5.0/9.0))

    print "The temperature is", c , "degrees celsius."

    end = input ("Hit any key to exit.")
    

main()

import RPi.GPIO as GPIO
import time

# Set the Row Pins
ROW_1 = 14
ROW_2 = 15
ROW_3 = 18
ROW_4 = 23

# Set the Column Pins
COL_1 = 2
COL_2 = 3
COL_3 = 4
COL_4 = 26

GPIO.setwarnings(False)
# BCM numbering
GPIO.setmode(GPIO.BCM)

# Set Row pins as output
GPIO.setup(ROW_1, GPIO.OUT)
GPIO.setup(ROW_2, GPIO.OUT)
GPIO.setup(ROW_3, GPIO.OUT)
GPIO.setup(ROW_4, GPIO.OUT)

# Set column pins as input and Pulled up high by default
GPIO.setup(COL_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(COL_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(COL_3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(COL_4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Function to read each row and each column
def readRow(line, characters):
    GPIO.output(line, GPIO.LOW)
    if GPIO.input(COL_1) == GPIO.LOW:
        return characters[0]
    if GPIO.input(COL_2) == GPIO.LOW:
        return characters[1]
    if GPIO.input(COL_3) == GPIO.LOW:
        return characters[2]
    if GPIO.input(COL_4) == GPIO.LOW:
        return characters[3]
    GPIO.output(line, GPIO.HIGH)
    return None

# Initialize an empty variable to store entered characters
entered_string = ""

# Use a for loop to get 4 characters
for _ in range(4):
    char = None
    while char is None:
        char = readRow(ROW_1, ["1", "2", "3", "A"]) or readRow(ROW_2, ["4", "5", "6", "B"]) or readRow(ROW_3, ["7", "8", "9", "C"]) or readRow(ROW_4, ["*", "0", "#", "D"])
    entered_string += char
    #print("Entered characters:", entered_string)
    time.sleep(0.2)  # adjust this per your own setup

print("Final entered string:", entered_string)
if entered_string == "1234":
    print("access")
else:
    print("denied")
    

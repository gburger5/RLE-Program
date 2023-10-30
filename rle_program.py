from console_gfx import ConsoleGfx
dictionary = {
    0:0,
    1:1,
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9,
    10:"a",
    11:"b",
    12:"c",
    13:"d",
    14:"e",
    15:"f",
    16:"g",
    "A":10,
    "B":11,
    "C":12,
    "D":13,
    "E":14,
    "F":15,
    "G":16,
    "a":10,
    "b":11,
    "c":12,
    "d":13,
    "e":14,
    "f":15,
    "g":16,
    "9": 9,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "10": "a",
    "11": "b",
    "12": "c",
    "13": "d",
    "14":"e",
    "15":"f",

}

def to_hex_string(data):
    new_list = [] # creates a new list to fill with correct data
    answer = ""
    for c in data:
        if c in dictionary: # iterates through the dictionary
            new_list.append(dictionary[c]) # appends the dictionary value of c
            answer = ''.join(map(str, new_list))# joins the list together as a string
    return answer

def count_runs(flat_data): # Counts the number of runs in a flat data set
    if not flat_data:
        return 0

    count = 1 # helper variable
    run_length = 1 # helper variable
    for j in range(1, len(flat_data)): # for loop iterating through the list
        if flat_data[j] == flat_data[j - 1]: # checks if the number is equal to the one previous to it
            run_length += 1
            if run_length > 15:
                run_length = 1
                count += 1
        else:
            if run_length >= 1:
                count += 1 # tallys the amount of runs
                run_length = 1

    return count # returns run amount





def encode_rle(flat_data):
    count = 1 # helper variable
    encode = [] # new list
    run = flat_data[0] # helper variable
    for j in range(1, len(flat_data)):  # loop that goes through the list
        if flat_data[j] == run:
            count += 1
            if count >= 15: # makes sure that if count goes to 15 that it restarts at 1 again
                encode.extend([count, run])
                count = 0
        else:
            encode.extend([count, run])
            run = flat_data[j]
            count = 1
    encode.extend([count, run]) # final list
    return encode


def get_decoded_length(rle_data):
    n = 2
    total = sum(rle_data[0::n]) # sums every other number in the list
    return total

def decode_rle(rle_data):
    final_list = []
    for c in range(len(rle_data)):
        if c % 2 == 0:
            for i in range(int(rle_data[c])):
                final_list.append(rle_data[c + 1])
    return final_list

def string_to_data(data_string):
    final_list = [] # new list
    for c in data_string:
        if c.isdigit(): # if the c is a digit now need to pull from dictionary
            final_list.append(int(c))
        else: # if c is a letter then pull from dictionary and turn to integer
            final_list.append(c)
    return final_list

def to_rle_string(rle_data):
    new_list = [] # creates new list
    answer = ""
    count = 0
    pair = 0
    for c in rle_data:
        count += 1
        if count % 2 != 0: # if count is not even, so if c's index isnt even were gonna use dict val
            new_list.append(str(dictionary[c]))
            pair += 1 # tallys to add delimeter
        elif count % 2 == 0: # if count is even, then no dict
            new_list.append(str(c))
            pair += 1
            if pair == 2:
                new_list.append(":")
                pair = 0
    new_list.pop(-1)
    return "".join(new_list)

def string_to_rle(rle_string):
    rle_list = []
    temp_list = []
    for number in rle_string:
        if number == ":":
            rle_list.append("".join(temp_list)) # joins the list w delimeter
            temp_list = []
        else:
            temp_list.append(number)
    rle_list.append("".join(temp_list)) # puts together rle list
    final_list = []
    for num in rle_list:
        final_list.append(num[0:-1])
        final_list.append(num[-1]) # slices last delimeter
    for c in range(len(final_list)):
        if c % 2 != 0:
            try:
                int(final_list[c])
                continue
            except ValueError:
                final_list[c] = dictionary[final_list[c]]
    return final_list


menu_show = 0
def menu_display(): #  Function to display the menu
    global menu_show
    if menu_show == 0:
        menu_show += 1
        print("Welcome to the RLE image encoder!\n")
        print("\nDisplaying Spectrum Image:")
        ConsoleGfx.display_image(ConsoleGfx.test_rainbow)
    print("\nRLE Menu")
    print("--------")
    print("0. Exit")
    print("1. Load File")
    print("2. Load Test Image")
    print("3. Read RLE String")
    print("4. Read RLE Hex String")
    print("5. Read Data Hex String")
    print("6. Display Image")
    print("7. Display RLE String")
    print("8. Display Hex RLE Data")
    print("9. Display Hex Flat Data\n")


if __name__ == '__main__':
    user_input = 0 # Sets the variable for user inputs in the future
    image_data = None # makes sure image data is empty
    run = True
    while run == True: # While loop to run through menu until exit
        menu_display()
        user_input = int(input("Select a Menu Option: "))
        if user_input == 1:
            file_name = input("Enter name of file to load:")
            image_data = ConsoleGfx.load_file(file_name)
        elif user_input == 6:
            print("Displaying image...")
            ConsoleGfx.display_image(show)
        elif user_input == 2:
            print("Test image data loaded. \n")
            show = ConsoleGfx.test_image
        elif user_input == 3:
            inputdata = input("Enter an RLE string to be decoded: ")
            image_data = string_to_rle(inputdata)
        elif user_input == 4:
            inputdata = input("Enter the hex string holding RLE data: ")
            image_data = string_to_data(inputdata)
        elif user_input == 5:
            inputdata = input("Enter the hex string holding flat data: ")
            image_data = encode_rle(inputdata)
        elif user_input == 7:
            try: # used try/except to make sure (no data) passed unit test
                if ":"  in image_data:
                    print(image_data)
                    break
                else:
                    answer = to_rle_string(image_data)
                    print(f"RLE representation: {answer}")
            except ValueError:
                print("RLE representation: (no data)")
        elif user_input == 8:
                answer_2 = to_hex_string(image_data) # prints this func, to get hex string
                print(f"RLE hex values: {answer_2}")
        elif user_input == 9:
                answer = "".join(decode_rle(image_data)) # prints it as a joined string
                print(f"Flat hex values: {answer}")
        elif user_input == 0:
            run = False
        else:
            print("Error! Invalid input.")





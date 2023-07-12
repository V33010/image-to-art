# install PIL: pip install Pillow
# install numpy: pip install numpy


from PIL import Image
import numpy as np
import time
import os
import sys

def cool_print(string):
    x = list(string)
    for i in x:
        print(i, end='', flush=True)
        time.sleep(0.03)

def clear_terminal():
    # Clear terminal for Windows and other platforms
    os.system('cls' if os.name == 'nt' else 'clear')

clear_terminal()

cool_print("\nThis program will convert an image into ASCII art\n\n")
print()
masterkey = 0
while masterkey == 0:
    key = 0
    while key == 0:
        
        cool_print("Enter the name of the image file: ")
        x = input()


        try:
            img = Image.open(x)
        except:
            cool_print("Error: Image not found\n")
            continue
        cool_print("Image will now be shown for confirmation")
        # wait 5 seconds
        time.sleep(2)
        img.show()
        print()
        cool_print("\nWas the image shown correct? (y/n): ")
        y = input()
        if y == 'y' or y == 'Y' or y == 'yes' or y == 'Yes' or y == 'YES':
            key = 1
            clear_terminal()
            break
        else:
            clear_terminal()
            continue


    
    # print dimensions of image
    cool_print("\nCurrent dimensions of image are: ")
    cool_print(str(img.size)) 

    cool_print("\nEnter the new dimensions of the image (It is recommended to keep the ratio same, and to keep the largest dimension below 180)\n")
    key = 0
    while key == 0:
        img = Image.open(x)
        try:
            cool_print("\nEnter width: ")
            width = int(input())
        except:
            cool_print("Error: Invalid input\n")
            continue

        smallkey = 0
        while smallkey == 0:
            try:
                cool_print("\nEnter height: ")
                height = int(input())
                smallkey = 1
                break
            except:
                cool_print("Error: Invalid input\n")
                continue

        clear_terminal()
        
        cool_print(f"New dimensions are {width}x{height}. The new image will be shown for confirmation")
        img = img.resize((width, height), Image.Resampling.LANCZOS); # reduce image size
        img.show()
        print()
        cool_print("Is this image correct? (y/n): ")
        y = input()
        if y == 'y' or y == 'Y' or y == 'yes' or y == 'Yes' or y == 'YES':
            key = 1
            print("")
            break
        else:
            clear_terminal()
            continue


    arr = np.array(img)


    for i in range(height):
        for j in range(width):
            arr[i][j] = max(arr[i][j][0],arr[i][j][1],arr[i][j][2])

    chars = ' .,:;\'`-_^/\\|!()[]<>#$@%'

    # creat array of size width x height
    arrnew = np.empty([height, width], dtype=str)



    for i in range(height):
        for j in range(width):
            val = int(arr[i][j][0] / 11)
            chosenchar = chars[val]
            arrnew[i][j] = chosenchar

    clear_terminal()

    cool_print("Art will be saved to a text file\nEnter filename (without extension)\n")
    cool_print("Filename: ")
    filename = input()

    filename = filename + ".txt"


    # create a new file and write the array to it
    with open(filename, 'w') as f:
        for i in range(height):
            for j in range(width):
                f.write(arrnew[i][j])
                f.write(' ')
            f.write('\n')


    cool_print(f'\nArt saved to file {filename}\n')
    time.sleep(3)
    clear_terminal()

    cool_print("Thank you for using this program\n")

    # press 1 to run again
    cool_print("Enter 1 to run again, or any other key to exit: ")
    x = input()
    if x == '1':
        clear_terminal()
        continue
    else:
        clear_terminal()
        sys.exit()

import os

def main():

    i = 0
    path = input("Input the folder location: ")
    for filename in os.listdir(path):
        my_dest = "img" + str(i) + ".jpg" #It can be changed to any value, contact @Spetsam for additional information
        my_source = path + filename #Source value
        my_dest = path + my_dest
        os.rename(my_source, my_dest)
        i+=1 #Increment at the end

if __name__ == '__main__':
    main()
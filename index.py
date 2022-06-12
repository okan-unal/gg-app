from encodings import utf_8
import sys

# count words for the target file
def count_words(file_name):
    with open(file_name, encoding="utf_8") as data: # closes the file automatically
        list = data.read().split() # split each word
        print("Number of words in file: ", len(list)) # print the words count


def count_frequency(file_name, iteration_time):
    with open(file_name, encoding="utf_8") as data:
        d = dict()
        for line in data: # check the lines in file
            line = line.strip().lower().split(" ")      
            for word in line:  # Paragraflardaki kelimeleri tek tek itere eder
                if word in d:
                    d[word] = d[word] + 1
                else:
                    d[word] = 1 # ilk sefer

        for x in range(0,iteration_time):
            maximum = max(d, key=d.get) # gets the maximum value of the dictionary with its key
            print("word name:", "\""+ maximum + "\"","usage:",d[maximum]);
            d.pop(maximum); # remove the max to get the next maximum from dict
            

method_name = sys.argv[2] 
file_name = sys.argv[4]


if(method_name == "count_words"):
    # addresses the function instance by calling it with file_name variable
    locals()[method_name](file_name)
if(method_name == "count_frequency"):
    iteration_time = 10;
    if(len(sys.argv) > 6):
        iteration_time = int(sys.argv[6])
    locals()[method_name](file_name, iteration_time)
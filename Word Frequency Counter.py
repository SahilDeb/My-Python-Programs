import fileinput

def main():
    contents = [] #list to store the contents read
    for line in fileinput.input("Question_2_Sample_Text.txt"):
        line = line.replace('\n', '')
        contents.append(line.lower()) #convert the whole text to lowercase
        temp = ''.join(contents) #join each parts into a single string
        temp = temp.split() #split the complete string

    count = [] #list to store the count of individual words
    for i in temp:
        count.append(temp.count(i))

    res = dict(zip(temp, count))
    sortedDict = sorted(res.items(), key = lambda x : x[1], reverse = True) #sort the dictionary based on values in decending order

    #print the top 3 most frequently appearing words along with their frequency
    print("WORD FREQUENCY")
    for i in range(3):
        print('"'+str(sortedDict[i][0]).capitalize()+'" '+str(sortedDict[i][1]).capitalize())

if __name__ == "__main__": #call main function
    main()

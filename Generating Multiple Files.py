import fileinput

def createFile(wordList):
    dataFile = open("Question_1_Data.txt", "r")
    data = dataFile.readlines()
    data = data[1:] #ignore the first line of the data file
    tempD = [] #List to store the respective values for each file
    for x in data:
        tempD.append(x.strip().replace('"', '').split(','))

    no = 0 #to create a numbered file with each data
    for item in tempD: #Loop through each set of data to create a new file
        no += 1
        replaceItems = [item[0], item[1], item[2]] #List to store a particular individual values

        make = open("File %d.txt" % no, "w+") #Create a file with a number
        #take line by line from the template file and check to replace
        for line in fileinput.input("Question_1_Template.txt"):
            for i in range(len(replaceItems)):
                line = line.replace(wordList[i], replaceItems[i]) #replace the placeholders with respective individual values
            make.write(line) #Write the modified line in the new file
        make.close() #Close the created file
        
def main():
    template = open("Question_1_Template.txt", "r") #Open the template file

    contents = template.readlines() #Read the template line by line
            
    wordList = [] #List to store the placeholders
    index1, index2 = (None, None) #Indexes to store the start and end pos of a placeholder

    #Traverse through each line read from template
    for line in contents:
        #Traverse through each character in a line
        for i in range(len(line)):
            if line[i] == "{":
                index1 = i #Store pos of '{'
            if line[i] == "}":
                index2 = i+1 #Store pos of '}'
            if index1 != None and index2 != None: #Check if index1 and index2 are not empty
                wordList.append(line[index1:index2]) #Get the placeholder value in that line and store in wordList list
                index1, index2 = (None, None) #Re-Initialize the index values for next placeholder
    createFile(wordList) #Call the createFile function and pass the wordList list as parameter
    template.close() #Close the template file

if __name__ == "__main__": #Run the main function
    main()

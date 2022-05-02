import copy

#<---------------------------------File opening-------------------------------------------->
#open input file
f = open("sample_input7.v","r")
f = f.read()
f= f.split('\n')
#<---------------------------------File opening End-------------------------------------------->

#<---------------------------------Functions Definition-------------------------------------------->

#function to return the number of bits to be abstracted in 
def bits(b):
    if b<=1:
        return b
    if b<4:
        return 2
    elif b<=16: 
        return 4
    elif b<=64: 
        return 8
    return b/10  


#function to remove comment
def comment_removal(line):
    return line[:line.index('//')]

#function to replace brackets
def bracketReplacer(contents):
    new_contents = copy.deepcopy(contents)
    for con in new_contents:
        sentence = con[1]
        if ':' in sentence:
            new_range = list(map(bits,[int(i) for i in sentence.split(":")]))
            new_range = [str(i) for i in new_range]
            sentence = ':'.join(new_range)
            con[1] = sentence
    return new_contents

def line_replacer(find,line):
    return line.replace(contents[find][1],new_contents[find][1])

#function to check if a character is a indentation
def isIndentation(char):
    return char == ' ' or char == '\t'



#<---------------------------------Functions Definition End-------------------------------------------->



#<---------------------------------abstraction logic-------------------------------------------->
# Initialization of global variables 
contents = []
line_counter = 0
line_word = []
for line in f:
    if '//' in line:
    #we need to remove the comment if there is any comment at the end of the line
        line = comment_removal(line)
        
    if line.strip() == ' ':
    #the line is empty
        line_counter += 1
        continue
    bracket_content = ''
    paranthesis = 0
    words = line.split(" ")
    if words[0] == "parameter" :
        line_word.append(words) 

    #checking further register whose indices to be truncated

    for character in line:
        if isIndentation(character):
            continue
        if character == '[' or character == ']':
            paranthesis = (1 if (character == '[') else 0)

        elif paranthesis == 1:
            bracket_content += character
    
    if bracket_content != '':
        limits = 0
        if ':' in bracket_content:
            limits = bracket_content.split(':')

            #if the index size is variable
            for k in line_word:
                if isinstance(limits[0],str):
                    if k[1] == limits[0][:len(limits[0])-2]:
                        limits[0] = str(int(k[3])-1)
            
            bracket_content = limits[0] + ":" + ''.join(limits[1:])
        
        elif bracket_content.isdigit():
            continue
        contents.append([line_counter,bracket_content])

    line_counter +=1

# print(contents)
new_contents = bracketReplacer(contents)
# print(new_contents)
abstracted_model = open("newFile.v",'w')
line_counter = 0
find = 0



#<--------------------------------building new abstracted model------------------------------------->

for line in f:
    if find < len(contents):
        if line_counter == contents[find][0]:
            line = line_replacer(find,line)
            find+=1
                
    line_counter +=1
    abstracted_model.write(line+'\n')


#<--------------------------------------------The END------------------------------------------------>
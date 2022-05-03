import copy

#<---------------------------------File opening-------------------------------------------->
#open input file
f = open("./Inputs/sample_input3.v","r")
f = f.read()
f= f.split('\n')
# Initialization of global variables 
line_word = []
contents = []
line_counter = 0
temp=0
parameterr=':'
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
def comment_removal(statement):
    return statement[:statement.index('//')]

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

def line_replacer(find,statement):
    return statement.replace(contents[find][1],new_contents[find][1])

#function to check if a character is a indentation
def isIndentation(char):
    return char == ' ' or char == '\t'



#<---------------------------------Functions Definition End-------------------------------------------->



#<---------------------------------abstraction logic-------------------------------------------->

for statement in f:
    if '//' in statement:
    #we need to remove the comment if there is any comment at the end of the statement
        statement = comment_removal(statement)
        
    if statement.strip() == ' ':
    #the statement is empty
        line_counter += 1
        continue
    bracket_content = ''
    paranthesis = 0
    words = statement.split(" ")
    if words[0] == "parameter" :
        line_word.append(words) 

    #checking further register whose indices to be truncated

    for character in statement:
        if isIndentation(character):
            continue
        if character == '[' or character == ']':
            paranthesis = (1 if (character == '[') else 0)

        elif paranthesis == 1:
            bracket_content += character
    
    if bracket_content != '':
        constraintss = 0
        if parameterr in bracket_content:
            constraintss = bracket_content.split(parameterr)

            #if the index size is variable
            for k in line_word:
                dmiLit=len(constraintss[0])
                if isinstance(constraintss[0],str):
                    if k[1] == constraintss[0][:dmiLit-2]:
                        constraintss[0] = str(int(k[3])-1)
            
            bracket_content = constraintss[0] + ":" 
            bracket_content =bracket_content + ''.join(constraintss[1:])
        
        elif bracket_content.isdigit():
            continue
        contents.append([line_counter,bracket_content])

    line_counter +=1

new_contents = bracketReplacer(contents)
abstracted_model = open("./Outputs/abstracted_model3.v",'w')
line_counter = 0
find = 0



#<--------------------------------building new abstracted model------------------------------------->
temp=len(contents)
for statement in f:
    temp=len(contents)
    if temp > find:
        if line_counter == contents[find][0]:
            statement = line_replacer(find,statement)
            find+=1
                
    line_counter +=1
    abstracted_model.write(statement+'\n')


#<--------------------------------------------The END------------------------------------------------>
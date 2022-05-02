import copy

#<---------------------------------Global variables----------------------------------------->
verilog_keyword = "parameter"
matter = []
line_word = []
find = 0
line_counter = 0
line_counter = 0
temp=0


#<---------------------------------File opening-------------------------------------------->
#open input file
f = open("./Inputs/sample_input6.v","r")
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
def comment_removal(statement):
    return statement[:statement.index('//')]

#function to replace brackets
def bracketReplacer(matter):
    new_contents = copy.deepcopy(matter)
    for con in new_contents:
        sentence = con[1]
        if ':' in sentence:
            new_range = list(map(bits,[int(i) for i in sentence.split(":")]))
            new_range = [str(i) for i in new_range]
            sentence = ':'.join(new_range)
            con[1] = sentence
    return new_contents

def line_replacer(find,statement):
    return statement.replace(matter[find][1],new_contents[find][1])

#function to check if a character is a indentation
def isIndentation(char):
    return char == ' ' or char == '\t'

#function to increment a value
def increment(x):
    return x+1

#function to decrement a value
def decrement(x):
    return x-1

def initialize():
    return 0

#<---------------------------------Functions Definition End-------------------------------------------->



#<---------------------------------abstraction logic-------------------------------------------->

for statement in f:
    constraints = 0
    bracket_content = ''
    if '//' in statement:
    #we need to remove the comment if there is any comment at the end of the statement
        statement = comment_removal(statement)
     
    if statement.strip() == ' ':
    #the statement is empty
        line_counter = increment(line_counter)
        continue
    
    
    words = statement.split(" ")
    if words[0] == verilog_keyword :
        line_word.append(words) 
    paranthesis = 0
    for character in statement:
        if isIndentation(character):
            continue
        if character == '[' or character == ']':
            paranthesis = (1 if (character == '[') else 0)

        elif paranthesis == 1:
            bracket_content = bracket_content+character
    
    if bracket_content != '':
        
        conlonCharacter = ':'
        if conlonCharacter in bracket_content:
            constraints = bracket_content.split(conlonCharacter)

            #if the index size is variable
            for h in line_word:
                len_constraint = len(constraints[0])
                if isinstance(constraints[0],str):
                    if h[1] == constraints[0][:len_constraint-2]:
                        constraints[0] = str(int(h[3])-1)
            
            bracket_content = constraints[0] + ":"
            bracket_content = bracket_content + ''.join(constraints[1:])
        
        elif bracket_content.isdigit():
            continue
        matter.append([line_counter,bracket_content])

    line_counter = increment(line_counter)

# print(matter)
new_contents = bracketReplacer(matter)
# print(new_contents)
abstracted_model = open("abstracted_model.v",'w')




#<--------------------------------building new abstracted model------------------------------------->

for statement in f:
    if find>=len(matter):
        # move
        temp=0
    else:
        if matter[find][0] == line_counter:
            statement = line_replacer(find,statement)
            find = increment(find)
                
    line_counter = increment(line_counter)
    abstracted_model.write(statement+'\n')


#<--------------------------------------------The END------------------------------------------------>
def runLengthEncoding(string):
    lst_of_letters = []
    counter = 1
    for i in range(1,len(string)):
        current_chr = string[i]
        previous_chr = string[i - 1]

        if current_chr != previous_chr or counter == 9:
            lst_of_letters.append(str(counter))
            lst_of_letters.append(previous_chr)
            counter = 0
        
        counter += 1
    
    lst_of_letters.append(str(counter))
    lst_of_letters.append(string[len(string) - 1])
    return "".join(lst_of_letters)

        

from gingerit.gingerit import GingerIt


def text_checking_with_index(text,i):
    result = GingerIt().parse(text)

    if len(result['corrections']) == 0:
        print("Statement {} is correct".format(i))
        return 0

    correct_text = result['result']
    original_text = result['text']
    print("The line number {} is incorrect.".format(i))
    print("\nOriginal Text :{}".format(original_text))
    print("\nCorrected Text: {}\n".format(correct_text))

def text_checking(text):
    result = GingerIt().parse(text)

    if len(result['corrections']) == 0:
        print("Statement is correct")
        return 0

    correct_text = result['result']
    original_text = result['text']
    print("The text is incorrect.")
    print("\nOriginal Text :{}".format(original_text))
    print("\nCorrected Text: {}\n".format(correct_text))

def letter_counting(text):
    text = text.split(" ")
    count = 0
    for words in text:
        count+=len(words)
    return count


if __name__ == '__main__':
    while True:
        print("""
1. Manual type text and check
2. Read text from file
3. Exit
        """)
        print("(Prees 1 or 2 or 3: ) ")
        key = input()
        if key == '1':
            print("Enter the text: ",end="")
            text = input()
            print("The sentance has {} letters\n".format(letter_counting(text)))
            text_checking(text)

        elif key == '2':
            print("Enter the text file path: ")
            filename = input()
            #try:
            with open(filename) as f:
                i=1
                for line in f:
                    print("The sentance {} has {} letters\n".format(i,letter_counting(line)))
                    text_checking_with_index(line,i)
                    i+=1
            #except:
            #    print("Enter the correct file path name.")
        elif key == '3':

            break
        else:
            print("Please press correct key\n")

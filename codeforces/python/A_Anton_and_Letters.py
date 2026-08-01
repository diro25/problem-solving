line=input()
cleaned_line=line[1:-1]
if cleaned_line=='':
    print(0)
else:
    letters=cleaned_line.split(', ')
    unique_letters=set(letters)
    print(len(unique_letters))
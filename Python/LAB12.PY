msg=input("Enter a sentence")

words=0
vowels=0
const=0
digits=0
spaces=0
spcchar=0

for ch in msg:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels+=1
        else:
            const+=1
    elif ch.isdigit():
        digits+=1
    elif ch.isspace():
        spaces+=1
    else:
        spcchar+=1

print(f"Vowels:{vowels}\nconst:{const}\nDigits:{digits}\nspaces:{spaces}\nspcchar:{spcchar}")


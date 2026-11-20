print("=" * 40)
print("        TEXT PROCESSING TOOL")
print("=" * 40)

text = input("Enter a sentence: ")

print("\n--- Processing Results ---")

pos = int(input("Enter position for indexing: "))
print(f"Character at position {pos} : '{text[pos]}'")

start = int(input("Enter start index for slicing: "))
end = int(input("Enter end index for slicing: "))
print(f"Sliced string [{start}:{end}] : '{text[start:end]}'")

print("Uppercase                 :", text.upper())
print("Lowercase                 :", text.lower())

word = input("Enter word to replace     : ")
new_word = input("Enter replacement word    : ")
print("After replace             :", text.replace(word, new_word))

print("Length of sentence        :", len(text))

print("\n" + "=" * 40)
print("Analysis Complete!")
print("=" * 40)
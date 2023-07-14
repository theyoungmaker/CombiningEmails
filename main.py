# Create a letter using the draft.txt in the Email folder/directory
# For each name in names.txt in Contacts
# Replace the [name] placehoder in the draft.txt with the real name
# Save the finished letters for each name in Send folder
# You can name the file Letter_for_name.txt where name is the name 
# the person


# Hint 1 (Reading lines in a file): https://www.w3schools.com/python/ref_file_readlines.asp
# Hint 2 (Replace a string with another string): https://www.w3schools.com/python/ref_string_replace.asp
# Hint 3 (remove whitespaces): https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Contacts/names.txt", "r") as file:
    names = file.readlines()


with open("./Email/draft.txt", "r") as draft:
    draft_letter = draft.read()
    for name in names:
        name = name.strip()
        letter = draft_letter.replace(PLACEHOLDER, name)
        with open(f"./Send/Letter_for_{name}.txt", "w") as new_file:
            new_file.write(letter)
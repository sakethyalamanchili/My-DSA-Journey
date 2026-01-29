# Read a text file and count the number of lines, words, and characters.
# Counting lines, words, and characters in a text file.

def read_txt(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count = 0
        char_count = 0
        for line in lines:
            word_count = word_count + len(line.split())
            char_count = char_count + len(line)
    
    return line_count, word_count, char_count

file_path = "basics\\File_Handling\\Sample.txt"
lines, words, characters = read_txt(file_name=file_path)
print(f"Lines: {lines}, Words: {words}, Characters: {characters}")
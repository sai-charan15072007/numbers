# total_lines = 0
# total_words = 0

# with open("questions.txt", "r") as file:
#     lines = file.readlines()
#     for line in lines:
#         total_lines = total_lines + 1
#         total_words = total_lines + len(line.split())
            

# print("Total lines in the file are:", total_lines)
# print("Total words in the file are:", total_words)


with open("questions.txt", "r") as file:
    lines = file.read()

    word_count = len(lines.split())
    line_count = len(lines.splitlines())


    print("Total lines in the file are:", line_count)
    print("Total words in the file are:", word_count)
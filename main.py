AVERAGE_WORDS_PER_MINUTE = 230

file = "text.txt"
output = "output.md"
with open(file, "r", encoding="utf-8") as txt:
    words = txt.read().split()
    word_counter = len(words)

average = word_counter / AVERAGE_WORDS_PER_MINUTE
minutes = int(average)
seconds = int((average - minutes) * 60)

with open(output, "w") as avg:
    if minutes < 1:
        avg.write(f"Estimated reading time: **{seconds}** seconds")
    else:
        avg.write(f"Esitmated reading time: **{minutes} minutes and {seconds} seconds**")

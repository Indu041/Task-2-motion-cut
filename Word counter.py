def count_words(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in punctuations:
        text = text.replace(char, ' ')
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def display_word_counts(word_counts):
    x=0
    for word, count in word_counts.items():
        print(f"'{word}': {count}")
        x=x+count
    print("Total count",x)
    

if __name__ == "__main__":
    text = input("Enter the text to analyze:\n")
    word_counts = count_words(text)
    display_word_counts(word_counts)

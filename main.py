def main():
    file_path = "books/frankenstein.txt"
    text = get_text(file_path)
    words = get_words(text)
    letters = get_letters(text)
    report = generate_report_from_dict(letters, words, file_path)

    print(text, f"\nTotal words: {words}\n", f"\nList of all letters used: {letters}\n", f"\nFull report: {report}")

def get_text(path):
    with open(path) as f:
        return f.read()

def get_words(text):
    total_words = text.split()
    return len(total_words)

def get_letters(text):
    letter_storage = {}
    for word in text.split():
        for char in word:
            if char.isalpha():
                char = char.lower()
                if char in letter_storage:
                    letter_storage[char] += 1
                else:
                    letter_storage[char] = 0
    return letter_storage

def generate_report_from_dict(letters, words, file_path):
    # Sort letters by frequency in descending order
    sorted_letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)

    # Generate report
    report = f"--- Begin report of {file_path} ---\n"
    report += f"{words} words found in the document\n\n"
    for letter, count in sorted_letters:
        report += f"The '{letter}' character was found {count} times\n"
    report += "--- End report ---"

    return report

main()
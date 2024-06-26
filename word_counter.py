# Creating a word_counter program to count the words in a sentence or paragraphs by taking user input.

def count_words(text):
    # Create an empty dictionary to store the word counts
    word_counts = {}
    
    # Split the text into words
    words = text.split()
    
    # Iterate over each word
    for word in words:
        # Convert the word to lowercase to ensure case insensitivity
        word = word.lower()
        
        # Remove punctuation from the word
        word = ''.join(char for char in word if char.isalnum())
        
        # If the word is already in the dictionary, increment its count
        if word in word_counts:
            word_counts[word] += 1
        # Otherwise, add the word to the dictionary with a count of 1
        else:
            word_counts[word] = 1
            
    return word_counts

# Function created to take user input.
def get_user_input():
    while True:
        # Using Error Handling concept for valid input from the user , to run the program smoothly.
        try:
            user_input = input("Enter the text (or type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                print("Exiting the program. Goodbye!")
                break
            if not user_input.strip():
                raise ValueError("Input cannot be empty. Please enter some text.")
            return user_input
        except ValueError as e:
            print(f"Error: {e}")

def main():
    
    print("Welcome to the Word Counter Program!")
    print("This program counts the occurrences of each word in your input text.\n")
     # Making the program user friendly.
    while True:
        text = get_user_input()
        if text:
            word_counts = count_words(text)
            print("\nWord Counts (sorted by frequency):")
            for word, count in sorted(word_counts.items(), key=lambda item: item[1], reverse=True):
                print(f"{word}: {count}")
            print("\n")

if __name__ == "__main__":
    main()
    # Calling main()function to run the program.

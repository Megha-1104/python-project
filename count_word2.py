# CREATING THE COUNT_WORDS PROGRAM TO COUNT THE TOTAL NO. OF WORDS IN A SENTENCE OR PARAGRAPH IN THE INPUT.

def count_words(user_input):
    # Split the input string into words
    words = user_input.split()
    # Return the count of words
    return len(words)

def main():
    print("\nWelcome to the Word Counter Program!")
    print("\nPlease enter a sentence or paragraph to count the words.\n")
    
    try:
        # Take input from the user
        user_input = input("Enter your text: ")
        
        # Check if the input is empty
        if not user_input.strip():
            raise ValueError("Input cannot be empty. Please enter some text.")
        
        # Count the words in the input
        word_count = count_words(user_input)
        
        # Display the word count
        print(f"The number of words in your input is: {word_count}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

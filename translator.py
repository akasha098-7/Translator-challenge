from googletrans import Translator, LANGUAGES

def translate_tweet():
    """A simple command-line tool to translate a tweet."""
    translator = Translator()

    print("Welcome to the Tweet Translator! 🐦")
    print("This tool can translate a tweet into many different languages.")
    print("-----------------------------------------------------")
    
    tweet_text = input("Enter the tweet you want to translate: ")
    
    print("\nSome common language codes:")
    print("English: en, Hindi: hi, Spanish: es, French: fr, German: de, Japanese: ja")
    target_lang = input("\nEnter the target language code (e.g., 'es' for Spanish): ").lower()

    if target_lang not in LANGUAGES:
        print("Invalid language code. Please try again with a valid two-letter code.")
        return

    try:
    
        translated_text = translator.translate(tweet_text, dest=target_lang).text
        
        print(f"\nOriginal Tweet: '{tweet_text}'")
        print(f"Translated Tweet: '{translated_text}'")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your internet connection and try again.")

if __name__ == "__main__":
    translate_tweet()
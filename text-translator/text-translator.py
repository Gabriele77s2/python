from translate import Translator

text = input("Enter text to translate: ")
source_language = input("Enter source language code (e.g., en): ")
target_language = input("Enter target language code (e.g., fr): ")

translator = Translator(source=source_language, target=target_language)
translated_text = translator.translate(text)

print("Translated text:", translated_text)

print("""
==== ANALIZER TEXT ====

Enter a text long or short: Example: paragraph, text, poem, article, etc.

also, you need to enter three letters to analyze: Example: a, e, i, etc.

==== ANALYZER TEXT ====
\n""")

# JMCode is a software developer, He's a very good developer and He wants to learn many leanguages of pograming because he wants to be the better software developer.

text = input("\nEnter a text: ")

first_letter = input("\nEnter the first letter: ")
second_letter = input("\nEnter the second letter: ")
third_letter = input("\nEnter the third letter: ")

paragraphs = text.split(" ")
paragraph_secret = "python"

print("\n\n === RESULTS ===\n")

print("\nThe letter 'a' appears: ", text.lower().count(first_letter), "times")
print("\nThe letter 'e' appears: ", text.lower().count(second_letter), "times")
print("\nThe letter 'i' appears: ", text.lower().count(third_letter), "times")

print("\nThe text has: ", len(paragraphs), "paragraphs")
print("\nThe first letter is: ", text[0])
print("\nThe last letter is: ", text[-1])
print("\nThe reversed text is: ", text[::-1])
print("\nIs the word \"python\" in the text?: ", paragraph_secret in text.lower())

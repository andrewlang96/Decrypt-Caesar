## Decrypt Caesar
This project decrypts encrypted text by analysing the frequency of different letter pairs in the text.

![Some gif of the main program](no gif yet)

A caesar cypher takes in a string of text, **"abcd"** for example, and and some integer **n** mod26, and uses that integer to encrypt the text by adding **n** to the rank of each lette in the text mod26. For example, `caesar("abcd", 3) = "defg"`. this took all the letters
in the original text and shifted them all four letters to the right in terms of their alphabetic rank.

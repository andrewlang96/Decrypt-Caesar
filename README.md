# Decrypt Caesar
This project decrypts encrypted text by analysing the frequency of different letter pairs in the text.

![Some gif of the main program](no gif yet)
## Description
#### Encryption
The text that this program decrypts has been encrypted with a caesar cypher. The 26 letter in the alphabet can each be assigned a rank from "a" = 0 to "z" = 25. A caesar cypher takes in a string of text, **"abcd"** for example, and and some integer **n** mod26, and uses that integer to encrypt the text by adding **n** to the rank of each letter in the text mod26. For example, `caesar("abcd", 3) = "defg"`. In this function, we took all the letters
in the original text and added n = 3 to their rank, and then mapped those ranks back to their corresponding letters to get the encrypted text.
#### Decryption
Because the rank of each letter in the text is shifted by the same amount, the distance from one letter to another in the text does not change afte encryption. By "distance", I mean the difference mod26 between the rank of 2 letters. Because the distance between each adjacent letter has the same value before and after the encryption, a lot of information about the original text is preserved in these letter pairs.

```python
text = "text" #Text before encryption
letter_pairs = ["te", "xt"] #Text broken up into adjacent letter pairs
pair_rank = [(19, 4), (23, 19)] #Letter pairs in terms of their rank
pair_rank_difference = [, 1] #Difference between the rank of each letter in letter pairs
```



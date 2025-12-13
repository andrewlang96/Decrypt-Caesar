# Decrypt Caesar
This project decrypts encrypted text by analysing the frequency of different letter pairs in the text.

![Demo of program](Code/demo.gif)
## Description
#### Encryption
The text that this program decrypts has been encrypted with a caesar cypher. The 26 letter in the alphabet can each be assigned a rank from "a" = 0 to "z" = 25. A caesar cypher takes in a string of text, **"abcd"** for example, and and some integer **n** mod26, and uses that integer to encrypt the text by adding **n** to the rank of each letter in the text mod26. For example, `caesar("abcd", 3) = "defg"`. In this function, we took all the letters
in the original text and added n = 3 to their rank, and then mapped those ranks back to their corresponding letters to get the encrypted text.
#### Decryption
Because the rank of each letter in the text is shifted by the same amount, the distance from one letter to another in the text does not change afte encryption. By "distance", I mean the difference mod26 between the rank of 2 letters. Because the distance between each adjacent letter has the same value before and after the encryption, a lot of information about the original text is preserved in these letter pairs.

```python
text = "text" #Text before encryption
letter_pairs = ["te", "xt"] #Text broken up into adjacent letter pairs
pair_rank = [(19, 4), (23, 19 )] #Letter pair ranks
pair_distance = [11, 22] #Distance between adjacent letters before encryption

encrypted_text = caesar(text, 2) #Encrypt the original text by adding 2 to the rank of each letter
encypted_letter_pairs = ["vg", "zv"] #Encrypted text broken up into adjacent letter pairs
encrypted_pair_rank = [(21, 6), (25, 21)] #Encrypted letter pair ranks
encrypted_pair_distance = [11, 22] #Distance between adjacent letters after encryption
```
Note that the distance between adjacent letters is the same before and after encryption. Now instead of looking at our text as a string of letters that are transformed into a different string of letters, we can look at it as the set of distances between adjacent letter and
ask what letter pairings result in this set of distences. This alone still leaves with with a problem, which that any particular distance can be the reuslt of 26 different letter pairs, so our search space is still exactly as it was to start with, but there is one key piece of information that will help us shrink the search space dramatically as well as give different weights to our options. This insight is that different letter pairs occure at different rates in English. For example, if we look at the encrypted letter pair "ui" we see that it has a distance of 11. While that could mean that this encrypted letter pair came from any of the 26 letter pairs with a distance of 11, it just so happens that about 60% of the adjacent letter pairs with a distance of 11 are "th". Asuming that this letter pair
came from an english text, we can say that there is a 60% chance that the key that was used to encrypt it was 1.






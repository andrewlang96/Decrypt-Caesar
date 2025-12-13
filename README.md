# Decrypt Caesar
This project decrypts encrypted text by analysing the frequency of different letter pairs in the text.

![Demo of program](Code/demo.gif)
## Description
#### Encryption
A rank can be assigned to each letter of the alphabet that represents where it lies from a=0 to z=25. A mathod of encryption know as a caesar cyphre takes in a string of letters, mapps them to their rakns, adds some constant value to all of their letters, and then mapps these new ranks back to letters.
```python
#EXAMPLE
text = "text" #Original string of text
text_ranks = [19, 4, 23, 19] #Ranks of the letters in the iriginal text
n = 2 #Key encryption value to be added to the rank of each letter
new_ranks = [21, 6, 25, 21] #Ranks of the original text plus key value n=2
emcrypted_text = "vgzu"
```
This method of encrypton results in a string of text that doesn't bare any resemblence to the original text.
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







# Decrypt Caesar
This project decrypts encrypted text by analysing the frequency of different letter pairs in the text.

![Demo of program](assets/demo.gif)
## Description
#### Encryption
An integer ***rank*** (0 to 25) can be assigned to each letter of the alphabet to represents where it lies from "a" to "z". A method of encryption know as a caesar ciphre takes in a string of letters, maps them to their ***rank***, adds some constant ***key*** value to each rank, and then maps these new ranks back to letters.
```python
#EXAMPLE
text = "text" #Original string of text
text_ranks = [19, 4, 23, 19] #Ranks of the letters in the iriginal text
key = 2 #Key value to be added to the rank of each letter
new_ranks = [21, 6, 25, 21] #Ranks of the original text plus key value n=2
emcrypted_text = "vgzu" #Encrypte text
```
This method of encrypton results in a string of text that doesn't bare any resemblence to the original text.
#### Decryption
Decrypting a caesar cipher consist of finding what ***key*** value was used to ecrypt it. Becaus the keys are all taken mod26, there are only 26 possible keys which makes it a rather trivial problem. One could simply write a script that atempts to decrypt the text with each of the 26 keys. The user could then review the output from each key to determin which was the right one. However, finding the right key with no user oversight is slightly less trivial. This requires either that the program be able to tell which of the resultant 26 strings is English text, or that the program be able to discerne some pattern from the encrypted text that would reveal the key. The latter is the method used here.
Because the rank of each letter in the text is shifted by the same amount, the ***distance*** from one letter to another does not change afte encryption.By distance, I mean the difference mod26 between the rank of 2 letters.

```python
#DISTANCES ARE NOT CHANGED BY ENCRYPTION
text = "text" #Text before encryption
letter_pairs = ["te", "xt"] #Text broken up into adjacent letter pairs
pair_rank = [(19, 4), (23, 19 )] #Letter pair ranks
pair_distance = [11, 22] #Distance between adjacent letters before encryption

encrypted_text = caesar(text, 2) #Encrypt the original text by adding 2 to the rank of each letter
encypted_letter_pairs = ["vg", "zv"] #Encrypted text broken up into adjacent letter pairs
encrypted_pair_rank = [(21, 6), (25, 21)] #Encrypted letter pair ranks
encrypted_pair_distance = [11, 22] #Distance between adjacent letters after encryption is the same as distance before encryption
```
Because the distance between each adjacent letter has the same value before and after the encryption, a lot of information about the original text is preserved in these letter pairs.
Now instead of looking at our text as a string of letters that is transformed into a different string of letters, we can look at it as the set of distances between adjacent letters that undergoes no transformation. Frome here the question becomes what set of letter pairs result in this set of distances. This fraiming alone isnt much better than the original question because any particular distance can be the reuslt of 26 different letter pairs, so our search space is still exactly the same. There is however, one key piece of information that will help us shrink the search space dramatically as well as give different weights to our options. This insight is that different letter pairs occure at different rates in English. For example, if we look at the encrypted letter pair "ui" we see that it has a distance of 11. While that could mean that this encrypted letter pair came from any of the 26 letter pairs with a distance of 11, it just so happens that about 60% of the adjacent letter pairs with a distance of 11 are "th". Asuming that this letter pair
came from an English text, we can say that there is a 60% chance that the key that was used to encrypt it was 1.









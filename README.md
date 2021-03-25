# Reverse-Hashing
Given first 6, last 4 and hash of a credit card, these programs brute force the remaining numbers. Written in Python for IT&amp;C 515R Encryption Implementation

instructions below:

 

Using the sample code provided (also in Learning Suite), create a program in python to demonstrate the difficulty of obtaining the full card numbers knowing only the hash value and portions of the card number. The sample code creates a small rainbow table of all card numbers with a given first 6 and last 4 digits, with their accompanying hash values. The code does not specify the hash algorithm to be used (it has been replaced with XXX in the code; See reference 4). You will need to modify the code on that line to get it to work properly. Select the appropriate hash algorithm for the code based on what you see in the suspicious file and your knowledge of the output of hash functions. 

 

After you get the program to work, use that program to recover all of the full card numbers represented within the suspicious file. The program as written (with the correct hash function coded, and perhaps some minor debugging) is sufficient to accomplish this task by providing as arguments the first 6 and last 4 digits of the card number, then searching the output for the hash value from the suspicious file.


References used:
https://stackoverflow.com/questions/57233763/python-module-called-with-cat-and-command-line-arguments-parser
https://stackoverflow.com/questions/22101931/passing-more-than-one-variables-to-os-system-in-python
https://runestone.academy/runestone/books/published/thinkcspy/Files/Iteratingoverlinesinafile.html
https://unix.stackexchange.com/questions/288521/with-the-linux-cat-command-how-do-i-show-only-certain-lines-by-number
https://www.w3schools.com/python/
https://www.geeksforgeeks.org/comm-command-in-linux-with-examples/
https://www.tunnelsup.com/hash-analyzer/
https://cryptography.io/en/latest/hazmat/backends/openssl.html
https://cryptography.io/en/latest/hazmat/backends/index.html
https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes.html

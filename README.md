###A repo for scripts I may write while playing around with CTF-type challenges or other programming tasks.

##Scripts added thus far:

- **Decryptor.py:**
  Implementation of the so-called "encryption" in one of the first basic tasks at https://www.hackthissite.org, and a corresponding decryption. The algorithm simply replaces each char with the char X positions farther down the ASCII chart, where x is the position of the initial char in the cleartext password. 
  - Example: 'aaa' would become 'abc', while 'abc' would become 'ace', etc.
  Usage: 
  To encrypt a password:
  `python decryptor.py -encrypt <password>`
  To decrypt a corresponding ciphertext, use:
  `python decryptor.py <ciphertext>`

What is this?
===
A collection of any scripts I may write while playing around with CTF-type challenges or other programming tasks. 

Scripts added thus far
===

- **Decryptor.py:**
  Implementation of the so-called "encryption" algorithm in one of the first basic tasks at https://www.hackthissite.org, and a corresponding decryption. The algorithm itself is extremely naive; it simply replaces each char with the char X positions farther down the ASCII chart, where x corresponds to the position of the initial char in the cleartext password. 
  - Examples: The password '*aaa*' would be enctypted into the ciphertext '*abc*', while '*abc*' would become '*ace*'.  
  Usage:  
  To encrypt a password:    
  `python decryptor.py -encrypt <password>`  
  To decrypt a corresponding ciphertext, use:  
  `python decryptor.py <ciphertext>`

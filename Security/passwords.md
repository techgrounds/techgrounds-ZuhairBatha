# [passwords]
[Password is a word, phrase, or string of characters intended to differentiate an authorized user or process (for the purpose of permitting access) from an unauthorized user]

## Key-terms
[Hashing, Rainbow ]

## Opdracht
- 1-Find out what hashing is and why it is preferred over symmetric encryption for storing passwords.
  - is defined as putting a password through a hashing algorithm (bcrypt, SHA, etc) to turn plaintext into an unintelligible series of numbers and letters..
  - (One-way function, Non-reversible,Increased security).
- 2-Find out how a Rainbow Table can be used to crack hashed passwords.
  - Generating the Rainbow Table.
  - Obtaining the Target Hash.
  - Table Lookup.
  - Applying Reduction Functions.
  -  Password Recovery.
- 3-Below are two MD5 password hashes. One is a weak password, the otheris a string of 16 randomly generated characters. Try to look up both hashes in a Rainbow Table.
- 4-Create a new user in Linux with the password 12345. Look up the hash in a Rainbow Table.
- 5-Despite the bad password, and the fact that Linux uses common hashing algorithms, you won't get a match in the Rainbow Table. This is because the password is salted. To understand how salting works, find a peer who has the same password in etc/shadow, and compare hashes.
  
### Gebruikte bronnen
[https://stytch.com/blog/what-is-password-hashing/]
[https://nordvpn.com/nl/blog/what-is-rainbow-table-attack/]

### Ervaren problemen
[geen]

### Resultaat
[gelukt]
![Rainbow](/techgrounds-ZuhairBatha-main/techgrounds-ZuhairBatha/00_includes/Security/security%204.1.png).
![password12345](../00_includes/Security/security%204.2.png).
![shadow](.././00_includes/Security/security%204.3.png).


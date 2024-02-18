The script first generates a list of all possible 4-character passwords using a given character set. This character set includes digits (0-9), lowercase alphabets (a-z), and special characters (&, *, #).


Once all possible combinations are generated and saved in allpassword.txt, the script then categorizes these passwords into 'strong' and 'weak' based on specific criteria:

Strong Passwords (strong.txt): A password is considered strong if it contains at least one digit, one alphabet character, and one special character.
Weak Passwords (weak.txt): Passwords are deemed weak if they do not meet the criteria for strong passwords. Additionally, any password starting with a digit is automatically categorized as weak.

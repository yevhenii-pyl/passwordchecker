# Password Leak Checker

This script checks if passwords have been exposed in data breaches by using the [Have I Been Pwned API](https://haveibeenpwned.com/API/v3#PwnedPasswords). The script processes a text file containing comma-separated passwords and reports if each password has been found in the breached database.

## Features
- Checks multiple passwords in one run.
- Utilizes the k-anonymity model to securely query the API without exposing full passwords.
- Provides information on how many times a password has been breached (if any).

---

## Requirements
- Python 3.7+
- Internet connection

---

### Dependencies
Install the required Python packages:

```bash
pip install requests
```

---

## Usage
### Input Format
Create a text file with passwords separated by commas. For example:

```
password1,password2,password3
```

## Running the Script
Use the following command to run the script:

```bash
python checkmypass.py <file_path>
```

Replace <file_path> with the path to your text file containing passwords.

---

## Notes
- **Security**: Passwords are hashed locally using SHA-1, and only the first 5 characters of the hash are sent to the API, ensuring privacy.
- **Rate Limits**: Be mindful of the API's rate limits and use the script responsibly.

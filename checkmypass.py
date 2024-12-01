import requests
import hashlib
import sys


# Request data from the "Have I Been Pwned" API
def request_api_data(query):
    # The URL is formed using the first 5 characters of the SHA1 hash.
    url = "https://api.pwnedpasswords.com/range/" + query

    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}")
    return res


# Get the count of how many times a password hash was leaked
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(":") for line in hashes.text.splitlines())

    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # Hash the password using SHA-1 and convert it to uppercase hexadecimal
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]

    response = request_api_data(first5_char)

    return get_password_leaks_count(response, tail)


def main(path):
    try:
        with open(path, "r") as file:
            content = file.read()
            passwords = [pw.strip() for pw in content.split(",")]
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return

    for password in passwords:
        count = pwned_api_check(password)
        if count:
            print(f'Password "{password}" was found {count} times.')
        else:
            print(f'Password "{password}" was NOT found.')
    return "Check finished!"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 checkmypass.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    sys.exit(main(file_path))

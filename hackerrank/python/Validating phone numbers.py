# https://www.hackerrank.com/challenges/validating-the-phone-number/

def validatePhoneNumber(phone_number):
    import re
    
    return True if re.search(r"^[7-9]\d{9}$", phone_number) else False

if __name__ == "__main__":
    for _ in range(int(input())):
        phone_number = input()

        print("YES" if validatePhoneNumber(phone_number) else "NO")
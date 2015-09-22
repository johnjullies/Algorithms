# https://www.hackerrank.com/challenges/validating-the-phone-number/

def validatePhoneNumber(phone_number):
    import re
    
    match = re.search(r"^[7-9]\d{9}$", phone_number)
    if match:
        return True
    else:
        return False

if __name__ == "__main__":
    for _ in range(int(input())):
        phone_number = input()

        print("YES" if validatePhoneNumber(phone_number) else "NO")
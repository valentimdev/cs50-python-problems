import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    s = s.split(" ")

    if len(s) < 4:
        raise ValueError("Input should have at least 4 components.")

    if "to" not in s:
        raise ValueError("Input should contain 'to'.")

    if ":" not in s[0]:
        s[0] = s[0] + ":00"

    if s[1] == "PM" and ":" not in s[0]:
        s[0] = str(int(s[0]) + 12) + ":00"
    elif s[1] == "PM" and ":" in s[0]:
        h, m = s[0].split(":")
        s[0] = f"{int(h) + 12:02}:{m}"

    if ":" not in s[3]:
        s[3] = s[3] + ":00"

    if s[4] == "PM" and ":" not in s[3]:
        s[3] = str(int(s[3]) + 12) + ":00"
    elif s[4] == "PM" and ":" in s[3]:
        h, m = s[3].split(":")
        s[3] = f"{int(h) + 12:02}:{m}"

    if "12" in s[0] or "24" in s[3]:
        if s[1] == "AM":
            s[0] = "00:00"
        if s[1] == "PM":
            s[0] = "12:00"

    if "12" in s[3] or "24" in s[3]:
        if s[4] == "AM":
            s[3] = "00:00"
        if s[4] == "PM":
            s[3] = "12:00"

    final_string = f"{s[0]} to {s[3]}"

    padrao = r'\b(6[0-9]|[7-9][0-9]|\d{3,})\b'
    verificacao = re.search(padrao, final_string)
    if verificacao:
        raise ValueError("Invalid hour range.")

    return final_string.strip()

if __name__ == "__main__":
    main()

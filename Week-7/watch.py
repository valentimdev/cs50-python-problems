import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        s=s.split('"')
        if len(s)<=1:
            return None
        for sentence in s:
            if "youtube" in sentence:
                new = re.sub(r"^(http.?://)?(www\.)?youtube.com/embed/","https://youtu.be/",sentence)
                return new
    except:
            return None



if __name__ == "__main__":
    main()
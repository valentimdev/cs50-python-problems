from validator_collection import validators, checkers, errors

def main():
    email=input("Whats your email adress?")
    checagem(email)
def checagem(email):
    try:
        email_adress=validators.email(email)
        print('Valid')
    except:
        print('Invalid')
main()
prompt = input("File name: ")

def checagem(prompt):
    prompt=prompt.lower().strip()
    if ".gif" in prompt:
        print("image/gif")
    elif ".pdf" in prompt:
        print("application/pdf")
    elif ".png" in prompt:
        print ("image/png")
    elif ".jpeg" in prompt or ".jpg" in prompt:
        print ("image/jpeg")
    elif ".txt" in prompt:
        print ("text/plain")
    elif ".zip" in prompt:
        print ("application/zip")
    else:
        print("application/octet-stream")

checagem(prompt)

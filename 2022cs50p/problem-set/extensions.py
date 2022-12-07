def a(x):

    if x.endswith(".gif"):
        return "image/gif"
    
    elif x.endswith(".jpg"):
        return "image/jqg"
    
    elif x.endswith(".jpeg"):
        return "image/jpeg"
    
    elif x.endswith(".pdf"):
        return "application/pdf"

    else:
        return "application/octet-stream"

print(a(input("File name: ")))
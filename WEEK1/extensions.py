name = input("File name please: ")
name = name.strip().lower()
name = name[-4:]


match name:
    case '.gif':
        print("image/gif")
    case '.jpg':
        print("image/jpeg")
    case 'jpeg':
        print("image/jpeg")
    case '.png':
        print("image/png")
    case '.pdf':
        print("application/pdf")
    case '.txt':
        print("text/plain")
    case '.zip':
        print("application/zip")
    case _:
        print("application/octet-stream")

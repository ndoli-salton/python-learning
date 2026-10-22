extension = input("File name:")
extension = extension.rsplit(".", 1)[-1].lower()

match extension:
    case ".gif":
        print("image/gif")
    case ".jpg":
        print("image/jpeg")
    case ".jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("text/pdf")
    case "txt":
        print("text/pdf")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
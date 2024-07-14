def main():
    file_name = input("Enter your file name: ").strip().lower()

    file_type = find_file_type(file_name)

    print(file_type)


def find_file_type(name):
    count = name.count(".")

    if count > 0:
        name, ext = name.rsplit(".", 1)
        match ext:
            case "gif":
                return "image/gif"
            case "jpg" | "jpeg":
                return "image/jpeg"
            case "png":
                return "image/png"
            case "pdf":
                return "application/pdf"
            case "txt":
                return "text/plain"
            case "zip":
                return "application/zip"
            case _:
                return "application/octet-stream"
    else:
        return "application/octet-stream"


main()

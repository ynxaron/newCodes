try:
    f = open("new_file.txt", "a")
    try:
        f.write("\nThis is another line here")
    except:
        print("Failed to write to the file")
    else:
        print("Succefully Written On File")
    finally:
        f.close()
except:
    print("Failed to open the file")
else:
    print("Succesfully Opened the File")


x = "he"

if not type(x) is int:
    raise Exception("Sorry, But all variables must be an intiger")


if x < 0:
    raise Exception("Sorry, But all variables must be non-negatives, preferably positive")

try:
    file = open(r"basics/File_Handling/Sample1.txt", 'r')
    content = file.read()
    print(content)
    
except FileNotFoundError:
    print("Specified file is not found. ⚠️")
    
finally:
    if 'file' in locals() and not file.closed:
        file.close()
        print("File closed successfully. ✅")
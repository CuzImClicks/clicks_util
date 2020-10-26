import os 

class File():

    def __init__(self, name, path):

        self.name = name
        self.path = path

    def move(self, new_path):

        try:
            os.replace(self.path, new_path)

        except Exception as e:

            print(e)

    def rename(self, new_name):

        try:
            os.rename(f"{self.path}\{self.name}", f"{self.path}\{new_name}")
            print("success")

        except Exception as e:
            print(e)
            pass
        
        
def rename_raw(path, name, new_name):
    
    try:
        os.rename(f"{path}\{name}", f"{path}\{new_name}")
        print("success")

    except Exception as e:
        print(e)
        pass
        
        
file_test = File("test2.txt", r"C:\Users\bruno\Desktop")

file_test.move(r"C:\Users\bruno\Desktop\Server")
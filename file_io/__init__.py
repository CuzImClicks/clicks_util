
import os 
class File():

    def init(self, name, path):

        self.name = name
        self.path = path

    def write(self, data):

        with open(f"{self.path}{self.name}", "r+") as f:

            f.write(data)
            f.close()

    def move(self, new_path):

        try:
            os.replace(self.path, new_path)

        except Exception as e:

            print(e)

    def rename(self, new_name):

        try:
            os.rename(f"{self.path}{self.name}", f"{self.path}{new_name}")
            print("success")

        except Exception as e:
            print(e)
            pass


def rename_raw(path, name, new_name):

    try:
        os.rename(f"{path}{name}", f"{path}{new_name}")
        print("success")

    except Exception as e:
        print(e)
        pass

def create(name, path):

    try:
        open(f"{path}{name}")

    except Exception as e:
        print(e)


file_test = File("test.txt", r"")

file_test.rename("test2.txt")
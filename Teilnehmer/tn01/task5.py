import os

class Filewalker:
    
    def __init__(self, filepath, filetype):
        self.filepath = filepath
        self.filetype = filetype
    
    def walker(self,start_path, filetype):
        for root, start_path, files in os.walk(start_path, filetype):
            for file in files:
                if file.endswith(filetype):
                    print(os.path.join(root, file))


if __name__ == '__main__':
    a = Filewalker('Trainer/Tag3', '.txt')
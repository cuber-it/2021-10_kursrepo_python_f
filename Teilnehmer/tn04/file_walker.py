class file_walker:
    import os

    def __init__(self):
        pass

    def findfile(self):

        for file in os.listdir("/mydir"):
           if file.endswith(".py"):
               print(os.path.join("/mydir", file))


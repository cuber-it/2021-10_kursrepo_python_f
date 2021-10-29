import os

class Filewalker:

    def __init__(self, startverzeichnis, dateinamenmuster):
        self.startverzeichnis = startverzeichnis
        self.dateinamenmuster = dateinamenmuster
        self.results = []

    def walk(self):
        return self


if __name__ == "__main__":
    fw= Filewalker(r"C:\tmp", "*tmp")
    e=fw.walk()
    print(e)

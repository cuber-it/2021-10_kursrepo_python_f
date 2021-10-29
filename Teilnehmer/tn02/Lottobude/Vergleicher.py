class Vergleicher:
    def compare (self,list_a, list_b):
        set_a=set(list_a)
        set_b=set(list_b)

        self.intersection=set_a.intersection(set_b) #Schnittmenge in a und b
        self.left_only=set_a.difference(set_b) # Differenzmenge (in a und nicht in b)
        self.right_only=set_b.difference(set_a) # Differenzmenge (in b nicht in a)

        return self.left_only, self.intersection, self.right_only

if __name__=="__main__":
    v=compare([1,2,3,4],[3,4,5,6])
    print(v())
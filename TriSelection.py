class TriListe:
    def __init__(self, maListe):
        self.liste=maListe
    def longeurListe(self):
        return len(self.liste)

    def triSelection(self):
        n=self.longeurListe()

        for i in range(n):
            indMin=i
            temp =self.liste[indMin]
            for j in range(i+1, n):
                if(self.liste[j]< self.liste[indMin]):
                    indMin = j

            self.liste[i]=self.liste[indMin]
            self.liste[indMin]=temp
    def get_liste(self):
        return  self.liste

    def triInsertion(self):
        n = self.longeurListe()
        for i in range(1,n):
            cle=self.liste[i]
            j=i-1
            while (j>=0 and cle< self.liste[j]):
                self.liste[j+1]=self.liste[j]
                j=j-1
            self.liste[j+1]=cle
    def triAbulle(self):
        n=self.longeurListe()
        for i in range(n-1):
            for j in range(n-1,i, -1):
                if self.liste[j]<self.liste[j-1]:
                    temp= self.liste[j]
                    self.liste[j] = self.liste[j - 1]
                    self.liste[j-1] = temp
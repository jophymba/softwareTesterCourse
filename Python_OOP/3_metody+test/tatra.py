class NakladniAuto():
    
    nosnost = 3000
    hmotnost_nakladu = 0

    def naloz(self, hmotnost):
        if self.hmotnost_nakladu + hmotnost <= self.nosnost:          
            self.hmotnost_nakladu += hmotnost

    def vyloz(self, hmotnost):
        if hmotnost <= self.hmotnost_nakladu:          
            self.hmotnost_nakladu -= hmotnost

    def vypis_nalozeni(self):
        print(f"V nákladním autě je naloženo {self.hmotnost_nakladu} kg")
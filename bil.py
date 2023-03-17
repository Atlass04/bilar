#det här är en class man kan skapa objekt av
class Bil:

    #constructor körs  först när man skapar objeckt av klassen
    def __init__(self, fabrikat, color, lager,):
        self.fabrikat = fabrikat
        self.color = color
        self.lager = lager
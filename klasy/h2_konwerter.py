from collections import OrderedDict
class Konwerter:

    def fahr_to_cel(self, st):
        cel=(st-32)*5/9
        return cel
    def cel_to_fahr(self, st):
        fahr=st*9/5+32
        return fahr

    @staticmethod
    def cel_to_fahr2(st):
        fahr=st*9/5+32
        return fahr



assert Konwerter().fahr_to_cel(32)==0
assert Konwerter.cel_to_fahr(None,0)==32
assert Konwerter.cel_to_fahr2(0)==32
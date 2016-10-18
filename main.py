from bson.objectid import ObjectId
from pymongo import MongoClient
import falcon

characterPool = {
    "0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
    "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18, "J": 19, "K": 20, "L": 21, "M": 22,
    "N": 23, "O": 25, "P": 26, "Q": 27, "R": 28, "S": 29, "T": 30, "U": 31, "V": 32, "W": 33, "X": 34, "Y": 35, "Z": 36,
    "a": 37, "b": 38, "c": 39, "d": 40, "e": 41, "f": 42, "g": 43, "h": 44, "i": 45, "j": 46, "k": 47, "l": 48, "m": 49,
    "n": 50, "o": 51, "p": 52, "q": 53, "r": 54, "s": 55, "t": 56, "u": 57, "v": 58, "w": 59, "x": 60, "y": 61, "z": 62,
};

client = MongoClient('localhost', 27017)
db = client.nullurl

class RedirectHandler(object):
    def process_request(self, req, res):
        path = req.path.strip('/')
        length = len(path)
        base = len(characterPool)
        acc = 0
        for index,digit in enumerate(path):
            sup = length - 1 - index
            num = characterPool[digit]
            acc += num * (base ** sup)
        id = hex(acc)[2:]
        url = db.urls.find_one({ '_id': ObjectId(id) })
        if url:
            raise falcon.HTTPSeeOther(url['long'])
        else:
            raise falcon.HTTPSeeOther('https://nullorm.github.io')

app = falcon.API(middleware=[RedirectHandler()])

from db import *

class Mahasiswa:
    def __init__(self):
        self.__dbname = "umc"
        self.__collection = "mahasiswa"
        self.db = MongoDB(self.__dbname, self.__collection)
        self.__id=None
        self.__nim=None
        self.__nama=None
        self.__jk=None
        self.__prodi=None

    @property
    def id(self):
        return self.__id

    @property
    def nim(self):
        return self.__nim

    @nim.setter
    def nim(self, value):
        self.__nim = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def jk(self):
        return self.__jk

    @jk.setter
    def jk(self, value):
        self.__jk = value

    @property
    def prodi(self):
        return self.__prodi

    @prodi.setter
    def prodi(self, value):
        self.__prodi = value

    def getAllData(self):
        return [doc for doc in self.db.find()]

    def getByNIM(self, nim):
        data = self.db.find_one({"nim":nim})
        if data:
            self.__nim=data["nim"]
            self.__nama=data["nama"]
            self.__jk=data["jk"]
            self.__prodi=data["prodi"]
        else:
            self.__nim=None
            self.__nama=None
            self.__jk=None
            self.__prodi=None
        return data

    def simpan(self):
        document = [{"nim": self.__nim, 
                     "nama": self.__nama, 
                     "jk": self.__jk, 
                     "prodi": self.__prodi}]
        
        self.db.insert_one(document)

    def updateByNIM(self, nim):
        filter={"nim":nim}
        document = {"$set":{"nim": self.__nim, 
                     "nama": self.__nama, 
                     "jk": self.__jk, 
                     "prodi": self.__prodi}}
        
        return self.db.update_one(filter, document)

    def deleteByNIM(self, nim):
        filter={"nim":nim}
        return self.db.delete_one(filter)


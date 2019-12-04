import hashlib


class Md5_enc():
    def __init__(self, key="cxj"):
        self.key = key
        self.maker = hashlib.md5()
    
    def md5_str(self, message):
        self.maker.update(bytes(self.key, encoding="utf-8"))
        self.maker.update(bytes(message, encoding="utf-8"))
        rel = self.maker.hexdigest()
        self.maker = hashlib.md5()
        return rel
    
    def md5_file(self, filename):
        filehandle= open(filename, 'rb')
        while True:
            tmp_data = filehandle.read(10240)
            if not tmp_data:
                break
            self.maker.update(tmp_data)
        filehandle.close()
        rel = self.maker.hexdigest()
        self.maker = hashlib.md5()
        return rel

if __name__ == '__main__':
    md = Md5_enc()
    # message = '12345667888'
    filename = 'G:\\黄大宝python\\2019\\20190711\\特色业务平台\\fbap.20190711r.t15\\fbap.20190711r.t16.zip'
    # rel = md.md5_str(message)
    rel = md.md5_file(filename)
    print(rel)
import os
import random
import threading


class RandomGetSlice(object):
    def __init__(self, fn, line_max_size=80, spliter='\n'):
        self.fn = fn
        self.line_max_size = line_max_size
        self.spliter = spliter

        self.lock = threading.Lock()
        self.fd = open(fn, "r")
        self.fsize = os.path.getsize(fn)

    def get(self):
        with self.lock:
            position = random.randint(0, self.fsize - (self.line_max_size*2))
            try:
                self.fd.seek(position)
                slice = self.fd.read(self.line_max_size * 2)
            except Exception as e:
                # xlog.warn("RandomGetSlice.get fail, fn:%s e:%r", self.fn, e)
                self.fd.close()
                self.fd = open(self.fn, "r")
                self.fd.seek(position)
                slice = self.fd.read(self.line_max_size * 2)

            if slice is None:
                raise Exception("random read line fail:%s" % slice)

            ns = slice.split(self.spliter)
            if len(ns) < 3:
                raise Exception("random read line fail:%s" % slice)

            return ns[1]

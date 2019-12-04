import os

def mkdirSbin(dpath):
    sbindir = os.path.join(dpath, 'sbin')
    if not os.path.isdir(sbindir):
        os.mkdir(sbindir)
    return sbindir

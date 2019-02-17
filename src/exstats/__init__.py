from os import listdir
from os.path import abspath, getsize, isdir, isfile, islink, join, splitext



VERSION = "0.1.0"

__all__ = [
    ]



def inall(obj):
    __all__.append(obj.__name__)
    return obj



def listfiles(path):
    if not islink(path):
        if isdir(path):
            for subPath in listdir(path):
                subPath = join(path, subPath)
                for fp in listfiles(subPath): yield fp
        elif isfile(path):
            yield path



def getDataForFile(filepath):
    size = getsize(filepath)
    ext = splitext(filepath)[-1]
    if ext: ext = ext[1:]
    if ext == "":
        ext = None
    else:
        ext = ext.lower()
    return ext, size



def getDataForFiles(filepaths):
    data = { }
    for fp in filepaths:
        ext, size = getDataForFile(fp)
        if ext not in data: data[ext] = 0
        data[ext] += size
    return data



def getPaths(givenPaths):
    for gfp in givenPaths:
        for fp in listfiles(gfp):
            yield abspath(fp)



def getData(givenPaths):
    fps = getPaths(givenPaths)
    fps = set(fps)
    return getDataForFiles(fps)

import common
import request
import fileIO

common.start()
userIn = common.waitUserInput()

splitStr = userIn.split()

data =  request.HttpGet(splitStr[0])

if (len(splitStr) != 1) and (len(splitStr) ==2):
    fileIO.write(path = splitStr[1],data = data)

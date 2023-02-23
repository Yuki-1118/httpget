# プログラムのエントリポイント
import common
import request
import config

processConfig = config.config
exitFlag = False

processConfig = common.start()

while not exitFlag:
    userIn = common.waitUserInput()

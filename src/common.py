import config
# argsに格納されている定数はhttpGetをコマンドラインから起動する際に追加で行う処理を指定する起動オプションのリスト
args = ['s','v']

# プログラム起動時に呼び出される
def start():
    print('-'*10 + 'Http Get' + '-'*10)
    return config.config()

# ユーザーからの入力を待機する
def waitUserInput():
    inputText = input()
    return inputText
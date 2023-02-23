
# ファイルに保存する pathには保存するファイルのフルパスを指定
def write(path,data):
    with open(path,'w',encoding='utf-8') as f:
        f.write(data)
    pass
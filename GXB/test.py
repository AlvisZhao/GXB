import happybase
if __name__ == '__main__':
    # thrift默认端口是9090
    host = '192.168.118.134'
    port = 9090
    connection = happybase.Connection(host)
    connection.open()
    table = connection.table("ChinaNews")
    i = 0
    for key, data in table.scan():
        i += 1
        titles = list(data.values())
        values = list(data.values())
        print(bytes.decode(key) + ":")
        for content in values:
            print("    " + bytes.decode(content))
    print("共有："+ str(i) +"条数据")
    connection.close()

fp = open("file/test.txt",'w')  # 打开文件，以写入模式打开 w-->write

# fp.write("hello world")
print("hello world",file=fp)
fp.close()
# -*- coding: utf-8 -*-
# 2018.12/31

cnt = 0
while cnt<100000:
    for i in ['/', '-', '\\', '|']:
        print(i, end = '\r')
        ### \r :  커서를 그 줄 처음으로 다시ㄱㄱ
    cnt += 1

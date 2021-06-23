#!/usr/bin/python3
# coding=utf-8
# Author: shangyidong
# Mail: shangyidong@meituan.com
import xlrd
import json
import pymysql
import uuid
import datetime

# 打开数据库连接，不指定数据库
# db = pymysql.connect("localhost","testuser","test123","TESTDB" )
db = pymysql.connect(host='rm-xxx.mysql.rds.aliyuncs.com',
                     user='xxx',
                     password='xxx',
                     db='xxx',
                     charset='utf8mb4')

# conn.select_db('rhino_service')
# 获取游标
cursor = db.cursor()

# data = xlrd.open_workbook('C:/Users/Shang/Downloads/test.xls')
data = xlrd.open_workbook('C:/Users/Shang/Downloads/test1.xlsx')

table = data.sheets()[0]  # 第一个工作簿
nrows = table.nrows  # 行数
# f = open('/Users/shangyidong/Downloads/test.txt', 'r+')
# f.truncate()
list = []
sqlTemplate = "insert into mcn_video (video_id, video_platform, mcn_account, nickname, video_title, video_type, director_name, planner, operations_manager, publish_time) " \
              "values('{}',{},'{}','{}','{}',{},'{}','{}','{}','{}')"
for i in range(nrows):
    if i == 0:
        continue
    tempObj = {}
    # format_date = datetime.datetime.strptime(table.row_values(i)[0], '%Y/%m/%d').strftime('%Y-%m-%d')
    format_date = table.row_values(i)[0]
    tempObj['publishTime'] = format_date
    tempObj['videoId'] = str(uuid.uuid1())
    tempObj['nickname'] = table.row_values(i)[1]
    tempObj['mcnAccount'] = table.row_values(i)[2]
    # 视频平台 0=抖音 1=快手
    videoPlatform = table.row_values(i)[3]
    if videoPlatform == '抖音':
        tempObj['videoPlatform'] = 0
    elif videoPlatform == '快手':
        tempObj['videoPlatform'] = 1
    tempObj['videoTitle'] = table.row_values(i)[4]
    # 视频类型 0 = 普通视频 1 = 广告视频
    videoType = table.row_values(i)[5]
    if videoType == '普通视频':
        tempObj['videoType'] = 0
    elif videoType == '广告视频':
        tempObj['videoType'] = 1
    # tempObj['videoType'] = table.row_values(i)[5]
    tempObj['directorName'] = table.row_values(i)[6]
    tempObj['planner'] = table.row_values(i)[7]
    tempObj['operationsManager'] = table.row_values(i)[8]
    # tempObj.operationsManager = table.row_values(i)[8]
    sql = sqlTemplate.format(tempObj['videoId'], tempObj['videoPlatform'], tempObj['mcnAccount'], tempObj['nickname'],
                             tempObj['videoTitle'], tempObj['videoType'], tempObj['directorName'], tempObj['planner'],
                             tempObj['operationsManager'], tempObj['publishTime'])
    print(sql)
    execute = cursor.execute(sql)
    print(execute)
    try:
        # 执行sql语句
        execute = cursor.execute(sql)
        print(execute)
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()
    # list.append(tempObj)

print(json.dumps(list, ensure_ascii=False))
cursor.close()
db.close()
# data2 = json.dumps(table.row_values(i))
# print(data2)
# print "'" + bizid + "',"
# f.write("'" + bizid + "'," + "\n")
# print len(bizid)
# print i

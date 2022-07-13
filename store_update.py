from array import array
from ast import copy_location
import csv
from xmlrpc.client import Boolean, boolean
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore import GeoPoint

# 引用firebase私密金鑰
cred = credentials.Certificate('cat-demo1-firebase-adminsdk-r3ki7-c794738a4f.json')
# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)
# 初始化firestore
db = firestore.client()

with open('store.csv', newline='') as csvfile:

  # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
  rows = csv.DictReader(csvfile)
  # 以迴圈輸出指定欄位
  for row in rows:
    print(row)
    op1=(row["adoption"])
    op2=(row["meal"])
    op3=(row["donation"])    
    latitude=row['latitude']
    longitude=row['longitude']
    # 指定寫入資料的位置在'database'中的'store_list'
    doc_ref = db.collection("database").document("store_list")
    # 以update的形式將資料輸入document
    doc_ref.update({row["name"]:{"location":firestore.GeoPoint(float(latitude),float(longitude)),
    "store_info":{"weekday_text":str(row["weekday_text"]),"reserve_mode":str(row["reserve_mode"]),"spending_mode":str(row["spending_mode"])},    
    "store_tag":{"adoption":(boolean(op1==1)),"meal":(boolean(op2==1)),"donation":(boolean(op3==1))},
    "store_area":{"city":str(row["city"]),"district":str(row["district"]),"address":str(row["address"])}}})

from ast import copy_location
import csv
from xmlrpc.client import boolean
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore import GeoPoint

# 引用firebase私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('servicekey.json')
# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)
# 初始化firestore
db = firestore.client()

with open('ntc.csv', newline='') as csvfile:

  # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
  rows = csv.DictReader(csvfile)
  # 以迴圈輸出指定欄位
  for row in rows:
    print(row)
    op1=(row["op1"])
    op2=(row["op2"])
    op3=(row["op3"])
    op4=(row["op4"])
    op5=(row["op5"])
    latitude=row['latitude']
    longitude=row['longitude']
    doc_ref = db.collection("database").document("storelist")
    doc_ref.update({row["name"]:{"lat":float(row["b"]),"log":float(row["a"]),"option1":boolean(op1=="1"),"option2":boolean(op2=="1"),"option3":boolean(op3=="1"),"option4":boolean(op4=="1"),"option5":boolean(op5=="1")}})

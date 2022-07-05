import csv
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

with open('mrtlocation_finish.csv', newline='') as csvfile:

  # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
  rows = csv.DictReader(csvfile)
  mrt_location={}
  # 以迴圈輸出指定欄位
  for row in rows:
    print(row)
    latitude=row['latitude']
    longitude=row['longitude']    
    doc_ref = db.collection("database").document("mrtlist")
    doc_ref.update({row["name"]:{"location":firestore.GeoPoint(float(latitude), float(longitude)),"tag1":str(row["tag1"]),"tag2":str(row["tag2"])}})

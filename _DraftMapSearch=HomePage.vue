<template>
  <Navbar></Navbar>
  <div class="col-12 text-center">
    <button class="btn btn-primary rounded-pill col-12 py-2" type="submit" @click="getCurrent()">Location</button>
  </div>
  <Footer></Footer>
</template>

<script>

import Navbar from "../components/HomeNavbar.vue";
import Footer from "../components/HomeFooter.vue";


export default {
  components: {
    Navbar,
    Footer,
  },
  method:{
    getCurrent() {
      // 先確認使用者裝置能不能抓地點
      if(navigator.geolocation) {
        // 使用者不提供權限，或是發生其它錯誤
        function error() {
          alert('無法取得你的位置');
        }
        // 使用者允許抓目前位置，回傳經緯度
        function success(position) {

          // 將所在地設成比較的點
          let originPosition = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
          // 把要計算的點存成陣列
          const storeData = require('../../store.geojson'); 
          let destinations = [];
          Array.prototype.forEach.call(_this.features, f => {
            destinations.push(new google.maps.LatLng(f.geometry.coordinates[0], f.geometry.coordinates[1]));
          });

          // 所在位置跟各點的距離
          const service = new google.maps.DistanceMatrixService();
          service.getDistanceMatrix({
            origins:[originPosition],//起點
            destinations:destinations,//店家位置
            travalMode: 'WALKING', // 交通方式：BICYCLING(自行車)、DRIVING(開車，預設)、TRANSIT(大眾運輸)、WALKING(走路)
            unitSystem: google.maps.UnitSystem.METRIC, // 單位 METRIC(公里，預設)、IMPERIAL(哩)
            avoidHighways: true, // 是否避開高速公路
            avoidTolls: true // 是否避開收費路線
          }, callback);

          function callback(response, status) {
            console.log(response);
            //把距離寫進json裡
            for(let i = 0, len = _this.features.length; i < len; i++) {
              _this.features[i].properties.distance = response.rows[0].elements[i].distance.value;
              _this.features[i].properties.distance_text = response.rows[0].elements[i].distance.text;
              _this.features[i].properties.distance_time = response.rows[0].elements[i].duration.text;
            }
            // 按距離重排
            _this.features = _this.features.sort((a, b) => {
              return a.properties.distance > b.properties.distance ? 1 : -1;
            });
            console.log(_this.features);
          }
          // 跟使用者拿所在位置的權限
          navigator.geolocation.getCurrentPosition(success, error);
      }
      } 
      else {
      alert('Sorry, 你的裝置不支援地理位置功能。')    
      }
    }
  }
}
</script>
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCQ6C2cE6dpBzxWprqS78ERdTXPSw4dUTM"></script>
<style>
.test {
  height: 500px;
}
</style>

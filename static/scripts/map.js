// retrieving map data
function updateLatLon(lat, lon, title) {
    document.getElementById("lat").value = lat;
    document.getElementById("lon").value = lon;
    document.getElementById("search_input_address").value = title;
}

var map = L.map('setmap').setView([27.709874, 85.32473013712973], 13);
var marker;
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);
map.addControl(new L.Control.Search({
  url: 'https://nominatim.openstreetmap.org/search?format=json&q={s}',
  jsonpParam: 'json_callback',
  propertyName: 'display_name',
  propertyLoc: ['lat', 'lon'],
  // marker: L.marker([0,0],{radius:30}),
  autoCollapse: true,
  autoType: false,
  minLength: 2,
  moveToLocation: function (latlng, title, map) {
      if (marker !== undefined) marker.remove()
      map.panTo(latlng);
      updateLatLon(latlng.lat, latlng.lng,title)
      // $("#search_input_address").val(title) 
      marker = L.marker(latlng).addTo(map)
          .bindPopup(title)
          .openPopup();
  }
}));

map.on("click", async function (e) {
  await $.get(
      `https://nominatim.openstreetmap.org/reverse?lat=${e.latlng.lat}&lon=${e.latlng.lng}`,
      function (data) {
          if (marker !== undefined) marker.remove()
          console.log(data)
          var address_part = data["childNodes"][0]["childNodes"][2]["children"]
            var title = ""
            var _list =["road", "suburb", "city", "country"]
            for(i in address_part){
                if(_list.includes(address_part[i].nodeName)) title += address_part[i]["textContent"] + ", "
            }
            title = title.slice(0, -2)
            if (marker !== undefined) marker.remove()

          map.panTo(e.latlng);
          marker = L.marker(e.latlng).addTo(map)
              .bindPopup(title)
              .openPopup();
          updateLatLon(e.latlng.lat, e.latlng.lng, title)
      }
  );
});


// setting map data
var _lat = 27.709874
var _lon = 85.32473013712973
var _address = "Kathmandu"
var _map = L.map('getmap').setView([_lat, _lon], 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(_map);
L.marker([_lat, _lon]).addTo(_map)
            .bindPopup(title)
            .openPopup();
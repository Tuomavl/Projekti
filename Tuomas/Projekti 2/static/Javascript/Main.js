'use strict';
/* 1. show map using Leaflet library. (L comes from the Leaflet library) */
const map = L.map('map', { tap: false });
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([50 , 10], 4);

const airportMarkers = L.featureGroup().addTo(map);
const list = [
  {name:"Puola",latitude: 52,longitude:21},
  {name:"Unkari",latitude:47,longitude:19},
  {name:"Kroatia",latitude: 45,longitude:16},
  {name:"Itavalta",latitude:48,longitude:17},
  {name:"Tsekki",latitude: 50,longitude:14},
  {name:"Saksa",latitude:52,longitude:13},
  {name:"Tanska",latitude: 56,longitude:13},
  {name:"Alankomaat",latitude:52,longitude:4},
  {name:"Italia",latitude: 42,longitude:12},
  {name:"Ranska",latitude:49,longitude:2},
  {name:"Ruotsi",latitude:60,longitude:18},
  {name:"Kreikka",latitude: 37,longitude:24},
  {name:"Albania",latitude:41,longitude:19},
  {name:"Romania",latitude: 45,longitude:26},
  {name:"Isobritannia",latitude:52,longitude:0}
]


// Get the modal
const modal = document.getElementById("myModal");

// Get the <span> element that closes the modal
const span = document.getElementsByClassName("close")[0];


// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target === modal) {
    modal.style.display = "none";
  }
}


for (let airport of list){
  const marker = L.marker([airport.latitude, airport.longitude]).addTo(map);
  airportMarkers.addLayer(marker);

  marker.openPopup();
  const popupContent = document.createElement('div');
  const h4 = document.createElement('h4');
  popupContent.append(h4);
  h4.innerHTML = airport.name
  const goButton = document.createElement('button');
        goButton.classList.add('button');
        goButton.innerHTML = 'Fly here';
        popupContent.append(goButton);
        marker.bindPopup(popupContent);

  goButton.onclick = function() {
    modal.style.display = "block";
  }
}
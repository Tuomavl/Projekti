'use strict';
/* 1. show map using Leaflet library. (L comes from the Leaflet library) */
const map = L.map('map', { tap: false });
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60, 24], 7);

//Global variable
const apiUrl = 'http://127.0.0.1:5000/loop';
const airportMarkers = L.featureGroup().addTo(map);

// function to fetch data from API
async function getData(apiUrl) {
  const response = await fetch(apiUrl);
  if (!response.ok) throw new Error('Invalid server input!');
  const data = await response.json();
  const data2 = data["data"]
  console.log(data2)

}



// icons
const blueIcon = L.divIcon({ className: 'blue-icon' });
const greenIcon = L.divIcon({ className: 'green-icon' });
// something
const gameData = await getData(url);
console.log(gameData)
for(let airport of gameData.location)
const marker = L.marker([airport.latitude, airport.longitude]).addTo(map);
airportMarkers.addLayer(marker);
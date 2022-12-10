'use strict';
/* 1. show map using Leaflet library. (L comes from the Leaflet library) */
const map = L.map('map', { tap: false });
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60, 24], 7);

async function gameSetup(){
  try {
    const response = await fetch(`http://127.0.0.1:5000/`);
    const data = await response.json();
    console.log(data);

  }catch(error){
    console.log(error);
  }

}
gameSetup();
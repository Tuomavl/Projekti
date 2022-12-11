'use strict';
/* 1. show map using Leaflet library. (L comes from the Leaflet library) */
const map = L.map('map', { tap: false });
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([52 , 15], 4);

//Global variables
const apiUrl = 'http://127.0.0.1:5000/';

//Fetch


//form for playerName
document.querySelector('#player-form').addEventListener('submit', function(evt){
  evt.preventDefault();
  const username = document.querySelector('#player-input').value;


})
//Fetch
const haku = await fetch('http://127.0.0.1:5000/Tarina.html?username='+username)

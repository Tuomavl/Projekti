'use strict';
/* 1. show map using Leaflet library. (L comes from the Leaflet library) */

const map = L.map('map', { tap: false });
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60, 24], 7);

//popup overlay
const Icon = document.getElementById('Icon')
Icon.onclick = function(){
  popup()
}

//form for player name

// function to fetch data from API
async function getData(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error('Invalid server input!');
  const data = await response.json();
  return data;
}
//function to update game status
//function to set up game
//Main function that creates game and calls other functions
async function gamesetup() {
  try{
    const gameData = await getData()
    console.log(gameData)
  } catch(error){
    console.log(error)
  }
}
gamesetup();
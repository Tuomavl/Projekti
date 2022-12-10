'use strict';
/* 1. show map using Leaflet library. (L comes from the Leaflet library) */
const map = L.map('map', { tap: false });
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60, 24], 7);
//Global variables
const apiUrl = 'http://127.0.0.1:5000/';
// form for player name
document.querySelector('#player-form').addEventListener('submit', function (evt) {
  evt.preventDefault();
  const playerName = document.querySelector('#player-input').value;
  gameSetup(`${apiUrl}newgame?player=${playerName}`);
});

//Function to fetch data from api
async function getData(url,message) {
    const response = await fetch(url);
    if (!response.ok) throw new Error(message)
    const data = await response.json();
    return data
}


//function to set up game
async function gameSetup(){
  try {
    const gameData = await getData(`http://127.0.0.1:5000/`);

    console.log(gameData);

  }catch(error){
    console.log(error);
  }

}
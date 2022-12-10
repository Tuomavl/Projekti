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
// form for player name
document.querySelector('#player-form').addEventListener('submit', function (evt) {
  evt.preventDefault();
  const playerName = document.querySelector('#player-input').value;
  gameSetup(`${apiUrl}newgame?player=${playerName}&loc=${startLoc}`);
});


// function to fetch data from API
  const response = await fetch('http://127.0.0.1:5000/newgame/' + playerName + '/' + loc);
  const jsonData = await response.json()
  const id = jsonData['username']


//function to set up game
async function gameSetup(url){
  try {
    const gameData = await getData(url);
    console.log(gameData);
    for (let airport of gameData.){
      const marker = L.marker([airport.latitude,airport.longitude]).addTo(map)
      marker.bindPopup(airport.name)
      marker.openPopUp();
      const popupContent = document.createElement('div');
      const h4 = document.createElement('h4')
      h4.innerHTML = airport.name;
      popupContent.append(h4);
      const gobutton = document.createElement('button')
      gobutton.classList.add('button');
      gobutton.innerHTML = 'Fly here!';
      popupContent.append(gobutton);
      marker.bindPopup(popupContent);

    }
  }catch(error){
    console.log(error);
  }

}
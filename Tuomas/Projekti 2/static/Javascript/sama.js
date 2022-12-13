'use strict';
/* 1. show map using Leaflet library. (L comes from the Leaflet library) */
const map = L.map('map', { tap: false });
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([50 , 10], 4);
const line = L.lineJoin
const apiUrlMurderer = 'http://127.0.0.1:5000/murdererGuess/';
const apiUrlGetMurderer = 'http://127.0.0.1:5000/getmurderer';
const apiUrlTarina = 'http://127.0.0.1:5000/mapview';
const apiUrlWelcomeText = 'http://127.0.0.1:5000/getWelcomeText';
const apiUrlFlyTo = 'http://127.0.0.1:5000//flyTooo/';
const murdererText=document.getElementById('murderer-text');
const murdererSubmit=document.getElementById('murderer-submit');

const polylinePoints = [
    [52, 21], [48, 17], [47,19], [45,26],[37,24], [41,19], [42,12], [49,2], [52,0], [52,4], [49,2], [50,14], [52,13], [52,21], [60,18], [56,13], [52,4], [56,13], [52,13], [50,14], [48,17], [42,12], [41,19], [45,16], [45,26], [47,19], [45,16], [48,17]

  ];

  const polyline = L.polyline(polylinePoints).addTo(map);


const airportMarkers = L.featureGroup().addTo(map);
const list = [
  {name:"Puola",latitude: 52,longitude:21},
  {name:"Unkari",latitude:47,longitude:19},
  {name:"Kroatia",latitude: 45,longitude:16},
  {name:"Itävalta",latitude:48,longitude:17},
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
  {name:"Iso-Britannia",latitude:52,longitude:0}
]

const apiUrlLocations = 'http://127.0.0.1:5000/getsuspectlist';
gameSetup(`${apiUrlLocations}`);

//Tää loggaa selaimen konsoliin murhaajan, joten lopullisessa pois!!
setTimeout(function() { getMurderer(); }, 500);

murdererSubmit.onclick=(event)=>{
    console.log(murdererText.value);
    guessMurderer(murdererText.value)
}

async function getStories(url){
    const gameData = await getData(url);
    const texts = gameData["stories"];
    //for (let i = 0; i < texts.length; i++) {
        //console.log(texts[i])
    //}

}
async function guessMurderer(murderer){
    const murdererRequest = await getData(apiUrlMurderer + murderer)
    if (murdererRequest["data"] === "win") {
        location.href = "victoryEnding.html"
    }else if (murdererRequest["data"] === "loss") {
        location.href = "lossEnding.html"
    }
}

async function fly(maa){
    const gameData = await getData(apiUrlFlyTo + maa)
    //console.log(gameData)
    //console.log(gameData["value"])
    if (gameData["value"]===0){
        console.log("Yepin");
        return gameData["value"];
    }
    else if (gameData["value"]===1){
        console.log("Yepin");
        return [gameData["value"], gameData["welcomeText"]];
    }
    else{
        console.log("Yepin");
        return [gameData["value"], gameData["welcomeText"], gameData["suspect"]];
    }
}


async function getMurderer(){
    const murdererRequest = await getData(apiUrlGetMurderer)
    console.log(murdererRequest["murderer"])
}

async function gameSetup(url){
    const gameData = await getData(url)
    console.log(gameData)
    getStories(apiUrlTarina);
}

async function getData(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error('Invalid server input!');
  const jsonData = await response.json();
  return jsonData;
}



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
        goButton.value = airport.name
        goButton.innerHTML = goButton.value;
        popupContent.append(goButton);
        marker.bindPopup(popupContent);
  const modalcontent = document.createElement('p')
  const moda = document.getElementById('modal-content')
  moda.appendChild(modalcontent)

  goButton.onclick = function() {
    //alert(goButton.value);
    //const flyToValue = gameSetup(apiUrlFlyTo + goButton.value);
    const flyToValue = fly(goButton.value);
    console.log(flyToValue);
    flyToValue.then(function(result) {
        console.log(result);

        if (result[0]==1){
            console.log(result[1])
            moda.innerText="";
            moda.appendChild(modalcontent)
            modal.style.display = "block";
            modalcontent.append(result[1])
        }
        else if (result[0]==2){
            console.log(result[1])
            console.log(result[2])
            moda.innerText="";
            moda.appendChild(modalcontent)
            modal.style.display = "block";
            modalcontent.append(result[1])
            modalcontent.append("Lentokentällä on " + result[2])
        }
        else{
          alert("Et voi lentää tuohon maahan");
        };

    });
  }
}

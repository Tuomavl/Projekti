const apiUrlPeli = 'http://127.0.0.1:5000/startGame';
const apiUrlMurderer = 'http://127.0.0.1:5000/murdererGuess/';
const apiUrlGetMurderer = 'http://127.0.0.1:5000/getmurderer';
const apiUrlTarina = 'http://127.0.0.1:5000/mapview';
const murdererText=document.getElementById('murderer-text');
const murdererSubmit=document.getElementById('murderer-submit');
const modalElement = document.getElementById("modal-content");

gameSetup(`${apiUrlPeli}`);
//Tää loggaa selaimen konsoliin murhaajan, joten lopullisessa pois!!
setTimeout(function() { getMurderer(); }, 500);

murdererSubmit.onclick=(event)=>{
    console.log(murdererText.value);
    guessMurderer(murdererText.value)
}

async function getStories(url){
    const gameData = await getData(url);
    texts = gameData["stories"];

    for (let i = 0; i < texts.length; i++) {
        console.log(texts[i])
    }
}
async function guessMurderer(murderer){
    murdererRequest = await getData(apiUrlMurderer + murderer)
    if (murdererRequest["data"] === "win") {
        location.href = "victoryEnding.html"
    }else if (murdererRequest["data"] === "loss") {
        location.href = "lossEnding.html"
    }
}

async function gameSetup(url){
    const gameData = await getData(url);
    getStories(apiUrlTarina);
    console.log(gameData[res]);

}

async function getData(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error('Invalid server input!');
  const jsonData = await response.json();
  return jsonData;
}


async function getMurderer(){
    murdererRequest = await getData(apiUrlGetMurderer)
    console.log(murdererRequest["murderer"])
}


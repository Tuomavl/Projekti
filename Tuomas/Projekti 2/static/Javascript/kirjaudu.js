const searchy=document.getElementById('player-input');
const searcher=document.getElementById('input-button');
const input = document.getElementById("player-input");

const apiUrlKirjaudu = 'http://127.0.0.1:5000/kirjaudu/';

input.addEventListener("keypress", function(event) {
  if (event.key === "Enter") {
    //search(searchy.value);
      console.log(searchy.value);
      gameSetup(`${apiUrlKirjaudu}`+searchy.value);
  }
});

searcher.onclick=(event)=>{
    console.log(searchy.value);
    gameSetup(`${apiUrlKirjaudu}`+searchy.value);
}

async function gameSetup(url){
    const gameData = await getData(url);
    console.log(gameData["username"]);
};

async function getData(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error('Invalid server input!');
  const jsonData = await response.json();
  return jsonData;
}

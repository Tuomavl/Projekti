const story_start = document.getElementById("story-start");

const apiUrlPeli = 'http://127.0.0.1:5000/startGame';
const apiUrlTarina = 'http://127.0.0.1:5000/tarina';

gameSetup(`${apiUrlTarina}`);

async function gameSetup(url){
    const gameData = await getData(url);
    console.log(gameData["username"]);

    story = "Hei rikosetsivä " + gameData["username"] + "!";

    let yep=document.createElement('p');
    yep.innerText=story;
    story_start.appendChild(yep);
};

async function gameSetup2(url){
    const gameData = await getData(url);
};

async function getData(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error('Invalid server input!');
  const jsonData = await response.json();
  return jsonData;
}

gameSetup2(`${apiUrlPeli}`);

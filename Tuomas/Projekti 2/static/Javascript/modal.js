const modal_text = document.getElementById("modal-content");

const apiUrlTarina = 'http://127.0.0.1:5000/mapview';

gameSetup(`${apiUrlTarina}`);

async function gameSetup(url){
    const gameData = await getData(url);
    console.log(gameData["story"]);

    text =gameData["story"];

    let yep=document.createElement('p');
    yep.innerText=story;
    modal_text.appendChild(yep);
}

async function getData(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error('Invalid server input!');
  const jsonData = await response.json();
  return jsonData;
}

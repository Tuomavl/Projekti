const apiUrlPeli = 'http://127.0.0.1:5000/startGame';

gameSetup(`${apiUrlPeli}`);

async function gameSetup(url){
    const gameData = await getData(url);
    console.log(gameData[res]);
};

async function getData(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error('Invalid server input!');
  const jsonData = await response.json();
  return jsonData;
}

const apiUrlSuspect = 'http://127.0.0.1:5000/getsuspect';
const container = document.getElementById('suspect-container')

getSuspect()


async function getSuspect(){
    sussyRequest = await getData(apiUrlSuspect)
    container.innerText = `Pidätit väärän henkilön. ${sussyRequest["suspect"]} ei ollut murhaaja. Hävisit pelin :(`;
    return sussyRequest["suspect"]
}

async function getData(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error('Invalid server input!');
  const jsonData = await response.json();
  return jsonData;
}
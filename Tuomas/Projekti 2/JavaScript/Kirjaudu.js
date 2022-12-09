const apiUrl = 'http://127.0.0.1:5000/username';

document.querySelector('form').addEventListener('submit', function(evt){
  evt.preventDefault()
  const playerName = document.querySelector('#username').value

})
async function getData(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error('Invalid server input!');
  const playerName = await response.json();
  const result = playerName["playerName"]
  console.log(result)
}
getData(apiUrl)

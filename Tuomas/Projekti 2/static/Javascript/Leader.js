const most_wins = document.getElementById("most-wins");
const most_played = document.getElementById("most-played");
const biggest_winstreak = document.getElementById("biggest-winstreak");

const apiUrlLeaderboard = 'http://127.0.0.1:5000/getLeaderBoard';

gameSetup(`${apiUrlLeaderboard}`);

async function gameSetup(url){
    const gameData = await getData(url);
    console.log(gameData["mostPlayed"]);

    for (i=0; i<gameData["mostPlayed"].length; i++) {
        most_wins_text = i+1 + ". " + gameData["mostWins"][i][1] + ": " + gameData["mostWins"][i][2];
        most_played_text = i+1 + ". " + gameData["mostPlayed"][i][1] + ": " + gameData["mostPlayed"][i][4];
        biggest_winstreak_text = i+1 + ". " + gameData["biggestWinstreak"][i][1] + ": " + gameData["biggestWinstreak"][i][6];

        let most_wins_element = document.createElement('p');
        most_wins_element.innerText = most_wins_text;
        most_wins.appendChild(most_wins_element);

        let most_played_element = document.createElement('p');
        most_played_element.innerText = most_played_text;
        most_played.appendChild(most_played_element);

        let biggest_winstreak_element = document.createElement('p');
        biggest_winstreak_element.innerText = biggest_winstreak_text;
        biggest_winstreak.appendChild(biggest_winstreak_element);
    };
};

async function getData(url) {
  const response = await fetch(url);
  if (!response.ok) throw new Error('Invalid server input!');
  const jsonData = await response.json();
  return jsonData;
}

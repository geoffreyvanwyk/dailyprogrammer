var fs = require('fs'),
    prompt = require('prompt'),

    words = fs.readFileSync('../wordlist.txt').toString().split('\r\n'),
    passwordLength = 7,

    wordsForGame = words.filter(function (word) {
       return word.length === passwordLength;
    });

    password = wordsForGame[randomIndex(0, wordsForGame.length)],
    allCandidates = {},
    selectedCandidates = [],

    guessesPerDifficulty = {
        veryEasy: 3,
        easy: 5,
        average: 7,
        hard: 11,
        veryHard: 13
    };

prepareCandidateLists();
populateCandidateLists();
selectCandidates();

console.log('Guess The Password!');
console.log('You get 4 guesses.');
console.log('Here are the candidates:');

selectedCandidates.forEach(function (candidate, index, candidates) {
    console.log(candidate);
});

var guessCount = 0;
prompt.start();
getGuess();

function getGuess() {
    prompt.get(['guess'], function (err, result) {
        if (err) {
            console.log(err);
        } else if (result.guess === password) {
        console.log('You got it right!');
        } else {
            console.log('Dead wrong!');
            guessCount += 1;
            if (guessCount < 5) {
                getGuess();
            }
        }
    });
}

function prepareCandidateLists() {
    var passChars = password.split('');

    passChars.forEach(function (char, index) {
       allCandidates[(index+1).toString()] = [];
    });

    allCandidates[password.length].push(password);
}

function populateCandidateLists() {
    wordsForGame.forEach(function (word, index, words) {
        var matches = [],
            chars = word.split('');;

        chars.forEach(function (char, index, chars) {
            matches.push(chars[index] === password[index] ? 1 : 0);
        });

        var numberOfMatches = matches.reduce(function (prev, cur) {
            return prev + cur;
        });

        if (numberOfMatches > 0) {
            allCandidates[numberOfMatches.toString()].push(word);
        }
    });
}

function selectCandidates() {
    for (list in allCandidates) {
        if (allCandidates.hasOwnProperty(list)) {
            selectedCandidates.push(allCandidates[list][randomIndex(0, allCandidates[list].length)]);
        }
    }
}

function randomIndex(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}

var fs = require('fs'),

    words = fs.readFileSync('../wordlist.txt').toString().split('\r\n'),
    passwordLength = 7,
    wordsForGame = nCharWords(passwordLength, words),
    password = password(wordsForGame),

    guessesPerDifficulty = {
        veryEasy: 3,
        easy: 5,
        average: 7,
        hard: 11,
        veryHard: 13
    };

console.log(password(WORD_LENGTH, words));

function candidateWords(password, wordsForGame) {
    var candidates = [password],
        passwordChars = password.split('');

    passwordChars.forEach(function (char) {
    });
}

function password(wordsForGame) {
    return wordsForGame[randomIndex(0, wordsForGame.length)];
}

function nCharWords(n, words) {
   var wordsOfNChars = words.filter(function (word) {
       return word.length === n;
   });

   return wordsOfNChars;
}

function randomIndex(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}

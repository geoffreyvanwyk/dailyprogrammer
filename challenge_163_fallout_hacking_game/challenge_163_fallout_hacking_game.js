var fs = require('fs'),
    prompt = require('prompt'),

    words = fs.readFileSync('../wordlist.txt').toString().split('\r\n'),
    passwordLength = 7,
    guessCount = 4,

    wordsForGame = words.filter(function (word) {
       return word.length === passwordLength;
    });

    password = wordsForGame[randomIndex(0, wordsForGame.length)],
    allCandidates = {};

allCandidates = prepareCandidateLists(allCandidates, password);
allCandidates = populateCandidateLists(allCandidates, password);
selectedCandidates = selectCandidates(allCandidates);
selectedCandidates = shuffleCandidates(selectedCandidates);

console.log("Play 'Guess The Password!'");
console.log('You get 4 guesses.');
console.log('Here are the candidates:');

selectedCandidates.forEach(function (candidate, index, candidates) {
    console.log(candidate);
});

prompt.start();
getGuess(password);

function getGuess(password) {
    prompt.get(['guess'], function (err, result) {
        if (err) {
            return console.log(err);
        }
        
        if (result.guess === password) {
            return console.info('You got it right!');
        }

        guessCount -= 1;
        console.log('%d/%d correct. %d guesses left', 
            numberOfMatches(result.guess, password), 
            password.length, 
            guessCount
        );

        if (guessCount > 0) {
            getGuess(password);
        }
    });
}

function prepareCandidateLists(allCandidates, password) {
    var passChars = password.split('');

    passChars.forEach(function (char, index) {
       allCandidates[(index+1).toString()] = [];
    });

    allCandidates[password.length].push(password);

    return allCandidates;
}

function populateCandidateLists(allCandidates, password) {
    wordsForGame.forEach(function (word, index, words) {
        var matches = numberOfMatches(word, password);

        if (matches > 0) {
            allCandidates[matches.toString()].push(word);
        }
    });

    return allCandidates;
}

function numberOfMatches(word, password) {
    var matches = [],
        characters = word.split('');;

    characters.forEach(function (character, index, characters) {
        matches.push(character === password[index] ? 1 : 0);
    });

    return matches.reduce(function (previous, current) {
        return (previous + current);
    });
}

function selectCandidates(allCandidates) {
    var selectedCandidates = [];

    for (list in allCandidates) {
        if (allCandidates.hasOwnProperty(list)) {
            var index = randomIndex(0, allCandidates[list].length);
            selectedCandidates.push(allCandidates[list][index]);
        }
    }

    return selectedCandidates;
}

function shuffleCandidates(selectedCandidates) {
    var shuffledCandidates = [];

    while (selectedCandidates.length > 0) {
        var index = randomIndex(0, selectedCandidates.length);
        shuffledCandidates.push(selectedCandidates.splice(index, 1)[0]);
    }

    return shuffledCandidates;
}

function randomIndex(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}

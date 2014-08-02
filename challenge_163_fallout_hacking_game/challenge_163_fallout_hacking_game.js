var fs = require('fs'),
    prompt = require('prompt'),

    WORDS = fs.readFileSync('../wordlist.txt').toString().split('\r\n'),
    GUESS_FRACTION = 0.75,
    WORDS_PER_DIFFICULTY = {
        '1': 3,
        '2': 6,
        '3': 9,
        '4': 12,
        '5': 15
    };

prompt.start();
setupGame(WORDS, WORDS_PER_DIFFICULTY, GUESS_FRACTION);

function setupGame(words, wordsPerDifficulty, guessFraction) {
    console.log("Play 'Guess The Password!'");
    console.log('Choose your difficulty level (1-5):');

    prompt.get(['difficulty'], function (err, result) {
        if (err) {
            return console.log(err);
        }

        var passwordLength = wordsPerDifficulty[result.difficulty],
            guessCount = Math.floor(guessFraction * passwordLength),

            wordsForGame = words.filter(function (word) {
                return word.length === passwordLength;
            }),
            
            password = wordsForGame[randomIndex(0, wordsForGame.length)],
            allCandidates = {};

        startGame(wordsForGame, password, allCandidates, guessCount);
    });
}

function startGame(wordsForGame, password, allCandidates, guessCount) {
    console.log('You get %d guesses.', guessCount);
    console.log('Here are the candidates:');

    emptyLists = prepareLists(allCandidates, password);
    populatedLists = populateLists(wordsForGame, emptyLists, password);
    selectedCandidates = selectCandidates(populatedLists);
    shuffledCandidates = shuffleCandidates(selectedCandidates);


    shuffledCandidates.forEach(function (candidate, index, candidates) {
        console.log(candidate);
    });

    getGuess(password, guessCount);

}

function getGuess(password, guessCount) {
    prompt.get(['guess'], function (err, result) {
        if (err) {
            return console.log(err);
        }
        
        if (result.guess === password) {
            return console.log('You got it right!');
        }

        guessCount -= 1;
        console.log('%d/%d correct. %d guesses left', 
            numberOfMatches(result.guess, password), 
            password.length, 
            guessCount
        );

        if (guessCount > 0) {
            getGuess(password, guessCount);
        }
    });
}

function prepareLists(allCandidates, password) {
    var passChars = password.split('');

    passChars.forEach(function (char, index) {
        allCandidates[(index+1).toString()] = [];
    });

    return allCandidates;
}

function populateLists(wordsForGame, allCandidates, password) {
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

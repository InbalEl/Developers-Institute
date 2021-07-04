const sentence = 'The movie is not that bad, I like it';
const wordNot = sentence.indexOf('not');
const wordBad = sentence.indexOf('bad');

let newSentence = sentence;

if (wordBad > wordNot) {
    newSentence = sentence.substr(0, wordNot) + 'good' + sentence.substr(wordBad + 3)
}

console.log(newSentence);
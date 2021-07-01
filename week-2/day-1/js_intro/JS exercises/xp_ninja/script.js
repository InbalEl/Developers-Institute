const userInput = prompt(`Please enter a sentence with the word 'Nemo' in it`)
const nemoIndex = userInput.indexOf(`Nemo`)
const msg = nemoIndex == -1 ? `I can't find Nemo :/` : `I found Meno at ${nemoIndex}`
console.log(msg);

console.log(5 >= 1)
console.log(0 === 1)
console.log(4 <= 1)
console.log(1 != 1)
console.log("A" > "B")
console.log("B" < "C")
console.log("a" > "A")
console.log("b" < "A")
console.log(true === false)
console.log(true != true)

let c
let a = 34
let b = 21
a = 2

console.log(a + b)
console.log(c)
console.log(3 + 4 + '5')

const userNumSum = prompt(`Please Enter coma-separated numbers to sum up`)
console.log(eval(userNumSum.replaceAll(',', '+')))

const userNum = Number(prompt('Please enter a number: '))
console.log(`input is ${userNum}`);

let msgBoom = "Bm"

if (userNum < 2) {
    msgBoom = msgBoom.slice(0,1) + "oo" + msgBoom.slice(1)
}

else if (userNum > 2) {
    const nofO = "o".repeat(userNum) 
    console.log(nofO);
    msgBoom = msgBoom.slice(0,1) + 'o'.repeat(userNum) + msgBoom.slice(1)
}

if (userNum % 5 === 0) {
    msgBoom = msgBoom.toUpperCase()
}

if (userNum % 2 === 0) {
    msgBoom += '!'
}


console.log(msgBoom)
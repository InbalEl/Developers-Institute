const x = 5;
const y = 2;

if (x < y) {
    console.log(`y(${y}) is the biggest number`);
} else if (x > y) {
    console.log(`x(${x}) is the biggest number`);
}

const newDog = `Chihuahua`;
console.log(`length = ${newDog.length}`);
console.log(`${newDog.toUpperCase()}`);
console.log(`${newDog.toLowerCase()}`);

if (newDog === 'Chihuahua') {
    console.log(`I love Chihuahuas, it’s my favorite dog breed`);
} else {
    console.log(`I dont care, I prefer cats`);
}


const userNum = Number(prompt('Please enter a number: '));

if (userNum % 2 == 0) {
    console.log(`${userNum} is an even number`);
}
else {
    console.log(`${userNum} is an odd number`);
}

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
const nofUsers = users.length;

if (!users) {
    console.log(`no one is online`);
}
else if (nofUsers === 2) {
    console.log(`${users[0]} and ${users[1]} is online`);
}
else {
    console.log(`${users[0]}, ${users[1]} and ${nofUsers - 2} more are online`);
}

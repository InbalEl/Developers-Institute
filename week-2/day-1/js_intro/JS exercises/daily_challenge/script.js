let fruits = ["banana", "apples", "oranges", "blueberries"];
console.log(fruits);

fruits.splice(fruits.indexOf('banana'), 1);
console.log(fruits);

fruits.sort();
console.log(fruits);

fruits.push('kiwi');
console.log(fruits);

fruits.shift();
console.log(fruits);
fruits.reverse()
console.log(fruits);

console.log(`----------------------------------------`);

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
console.log(moreFruits[1][1][0]);
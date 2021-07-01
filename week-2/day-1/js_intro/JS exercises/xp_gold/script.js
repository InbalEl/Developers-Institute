const me = ["my","favorite","color","is","blue"]
console.log(me.join(" "))

const str1 = "mix"
const str2 = "pod"
const newStr1 = str2.slice(0,2) + str1.slice(2)
const newStr2 = str1.slice(0,2) + str2.slice(2)

// const slicesStrs = `${str2[0,2]} + ${str1[2,]}`
console.log(`${newStr1} ${newStr2}`);

const concatStr = `${str1} ${str2}`
console.log(concatStr);


const num1 = prompt('Please enter the first number: ')
const num2 = prompt('Please enter the second number: ')
const operator = prompt('Please enter the operation desired: ')

alert(`Sum = ${eval(`${num1} ${operator} ${num2}`)}`)
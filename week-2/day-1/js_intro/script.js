const addressNumber = 1
const addressStreet = 'Ben Gurion Blvd'
const country = 'Israel'
const global_address = `${addressNumber} ${addressStreet} St., ${country}`

console.log(global_address)

const birthYear = 1988
const futureYear = 2027

console.log(`I will be ${futureYear-birthYear} in the year ${futureYear}`)

let pets = ['cat',
            'dog',
            'fish',
            'rabbit',
            'cow']

console.log(pets)
console.log(`pets[1] = ${pets[1]}`)

pets.push('horse')
console.log(`pets after adding horse:`)
console.log(pets)

pets.splice(pets.indexOf('rabbit'), 1)
console.log(`pets after removing rabbit:`)
console.log(pets)
console.log(`Arrat legnth is: ${pets.length}`)
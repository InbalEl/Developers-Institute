let articleElem = document.getElementsByTagName('article')[0]
let articlePars = articleElem.querySelectorAll('p')
articleElem.removeChild(articlePars[articlePars.length-1])

let h2 = document.getElementsByTagName('h2')[0]

console.log(h2)

function onH2Click(event) {
    // event.target.style.background = 'lightblue'
    console.log(event.target)
}

h2.addEventListener('onClick', onH2Click)

// let h1 = document.getElementsByTagName('h1')[0]
// h1.style.fontSize = `${Math.random() * 101}px`

// let h3 = document.getElementsByTagName('h3')[0]

// function onH3Click(event) {
//     h3.style.display = 'none'
// }

// h3.addEventListener('onClick', onH3Click)

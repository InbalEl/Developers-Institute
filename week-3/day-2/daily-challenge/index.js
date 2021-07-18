const planetNames = ['Mercury','Venus','Earth','Mars','Jupiter',
                    'Saturn','Uranus','Neptune']
const planetColors = ['gray','yellow','green','red','brown',
                      'purple','lightblue','blue']

let planets = []

planetNames.forEach((value, index) => {
    planets.push({'name': `${value}`, 'color': `${planetColors[index]}`})
})

let planetSection = document.getElementsByClassName('listPlanets')[0]

planets.forEach((planet) => {
    console.log(planet)
    const newPlanetDiv = document.createElement('div')
    newPlanetDiv.style.background = planet['color']
    newPlanetDiv.appendChild(document.createTextNode(planet['name']))
    newPlanetDiv.classList.add('planet')
    
    planetSection.appendChild(newPlanetDiv)
})

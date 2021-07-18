let navDivEl = document.getElementById('navBar')
navDivEl.setAttribute('id', 'socialNetworkNavigation')

let newAnchorEl = document.createElement('a')
newAnchorEl.href = '#'
newAnchorEl.innerHTML = 'Logout'

let newLiEl = document.createElement('li')
newLiEl.appendChild(newAnchorEl)

let listEl = document.getElementById('list')
listEl.appendChild(newLiEl)

console.log(listEl.firstElementChild.firstChild.textContent)
console.log(listEl.lastElementChild.firstChild.textContent)
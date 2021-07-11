let lists = document.getElementsByClassName('list')

lists[0].lastElementChild.firstChild.textContent = 'Richard'

Array.from(lists).forEach((list) => {
    list.firstElementChild.firstChild.textContent = 'Inbal'
    const newLiEl = document.createElement('li')
    newLiEl.textContent = 'Hey Students'
    list.appendChild(newLiEl)
    list.classList.add('student_list')
})

lists[1].children[1].textContent = ''

lists[0].classList.add('university', 'attendance')


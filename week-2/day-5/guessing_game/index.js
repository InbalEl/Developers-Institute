/*----------------------------------------------------------------------------*/
function playTheGame() {
    let userConfirmed = confirm('Would you like to play the guessing game?')

    while (userConfirmed) {

        startRound()
        userConfirmed = confirm('Would you like another round?')
    }

    alert('No problem, goodbye!')
}

/*----------------------------------------------------------------------------*/
function startRound() {
    const userNum = isGoodNum(getUserStrNum())
    if (!isNaN(userNum)) {
        const computerNum = getComputerNum()
        test(userNum, computerNum)
    }
}

/*----------------------------------------------------------------------------*/
function getComputerNum() {
    const compNum = (Math.round(Math.random(0, 10) * 11))
    return compNum
}

/*----------------------------------------------------------------------------*/
function isGoodNum(userNumstr) {
    
    if (!userNumstr || isNaN(userNumstr)) {
        alert('Sorry, not a number')
        return NaN
    } else {
        const userNum = Number(userNumstr)
        if (userNum < 0 || userNum > 10) {
            alert('Sorry, not a good number')
            return NaN
        }
        
        return Number(userNumstr)
    }
}

/*----------------------------------------------------------------------------*/
function getUserStrNum() {
    return prompt('Please enter a number between 0 and 10: ')
}

/*----------------------------------------------------------------------------*/
function test(userNum, computerNum) {
    if (userNum === computerNum) {
        alert('WINNER!')
        
    } else {
        const diff = userNum > computerNum ? "bigger" : "smaller"
        alert(`Your number is ${diff} than the computer's`)
    }
}

/*----------------------------------------------------------------------------*/
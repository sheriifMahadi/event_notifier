
const events = document.getElementById('event')
const countdown = document.getElementById('countdown')

console.log(events.textContent)
const eventDate = Date.parse(events.textContent)

const coundownInterval = setInterval(() => {
    const now = new Date().getTime()
    today = new Date()
    const diff = eventDate - now


    const days = Math.floor(eventDate / (1000 * 60 * 60 * 24) - (now / (1000 * 60 * 60 * 24)))
    const hours = Math.floor((eventDate / (1000 * 60 * 60) - (now / (1000 * 60 * 60))) % 24)
    const minutes = Math.floor((eventDate / (1000 * 60 ) - (now / (1000 * 60))) % 60)
    const seconds = Math.floor((eventDate / (1000) - (now / (1000))) % 60)




    if (diff) {
        countdown.innerHTML = days + ' days, ' + hours + ' hours ' + minutes + ' minutes ' + seconds + ' seconds'

    } 
    else {
        clearInterval(coundownInterval)
        countdown.innerHTML = "Countdown completed"
    }

}, 1000);




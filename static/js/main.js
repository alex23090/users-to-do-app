let message_close = document.getElementsByClassName('alert__close')
let message = document.getElementsByClassName('alert')

if (message){
    message_close.addEventListener('click', (e)=>{
    message.remove()
})
}


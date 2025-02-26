import { isEmail } from "../utils/validators.js";
import {clearSpan} from "./global.js"

const nameContent = document.querySelector('#name')
const emailContent = document.querySelector('#email')
const passwordContent = document.querySelector('#password')
const rePasswordContent = document.querySelector('#re_password')
const btnRegister = document.querySelector('#btn_register')
const spanContent = document.querySelector('#span_message')

emailContent.addEventListener('focus', clearSpan)
btnRegister.addEventListener('click', handlerRegister)

function handlerRegister() {
    const name = nameContent.value
    if (!name) {
        spanContent.innerHTML = 'Empty name field'
        return
    }

    const email = emailContent.value
    if (!isEmail(email)){
        spanContent.innerHTML = 'Invalid E-mail'
        return
    }

    const password = passwordContent.value
    const rePassword = rePasswordContent.value
    if (!password || !rePassword) {
        spanContent.innerHTML = 'Empty password field'
        return
    }
    
    if (password !== rePassword) {
        spanContent.innerHTML = 'Invalid Passwords'
        return
    }

    // fetch('http://localhost:8080/register', {
    //     method: 'POST',
    //     headers: {'Content-Type': 'application/json'},
    //     body: JSON.stringify({name, email, password, rePassword})
    // })
    // .then(response => response.json())
    // then(data => {
    //     if (data.success) {
    //         console.log('entrou')
    //         localStorage.setItem('token', data)
    //         // window.location.href = ''
    //     } else {
    //         spanContent;innerHTML = 'Invalid Login'
    //     }
    // })

    console.log(name, email, password, rePassword)
    nameContent.value = ''
    emailContent.value = ''
    passwordContent.value = ''
    rePasswordContent.value = ''
    clearSpan()
}

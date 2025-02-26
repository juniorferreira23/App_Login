import { isEmail } from "../utils/validators.js";
import {clearSpan} from "./global.js"

const emailContent = document.querySelector('#email')
const passwordContent = document.querySelector('#password')
const btnLogin = document.querySelector('#btn_login')
const spanContent = document.querySelector('#span_message')

emailContent.addEventListener('focus', clearSpan)
btnLogin.addEventListener('click', handlerLogin)


function handlerLogin() {
    const email = emailContent.value
    if (!isEmail(email)){
        spanContent.innerHTML = 'Invalid E-mail'
        return
    }
    const password = passwordContent.value
    if (!password) {
        spanContent.innerHTML = 'Empty password field'
        return
    }

    // fetch('http://localhost:8080/login', {
    //     method: 'POST',
    //     headers: {'Content-Type': 'application/json'},
    //     body: JSON.stringify({email, password})
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

    console.log(email, password)
    emailContent.value = ''
    passwordContent.value = ''
}


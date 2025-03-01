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

async function handlerRegister() {
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

    try{
        const response = await fetch('http://127.0.0.1:8000/register', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                full_name: name,
                username: email,
                password: password,
                re_password: rePassword
            })
        })

        if (!response.ok) {
            throw new Error('Error registering')
        }

        const data = await response.json()
        
        if (data) {
            alert('Registro criado com sucesso')
            window.location.href = 'http://127.0.0.1:3000/index.html'
        }
    } catch (error) {
        console.error('Error:', error)
    }

    nameContent.value = ''
    emailContent.value = ''
    passwordContent.value = ''
    rePasswordContent.value = ''
    clearSpan()
}

import { isEmail } from "../utils/validators.js";
import {clearSpan} from "./global.js"

const emailContent = document.querySelector('#email')
const passwordContent = document.querySelector('#password')
const btnLogin = document.querySelector('#btn_login')
const spanContent = document.querySelector('#span_message')

emailContent.addEventListener('focus', clearSpan)
btnLogin.addEventListener('click', handlerLogin)


async function handlerLogin() {
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

    const formData = new URLSearchParams()
    formData.append('username', email)
    formData.append('password', password)

    try{
        const response = await fetch('http://127.0.0.1:8000/token', {
            method: 'POST',
            headers: {'Content-Type': 'application/x-www-form-urlencoded'},
            body: formData
        })

        if (!response.ok) {
            throw new Error('Error logging in')
        }

        const data = await response.json()
        
        localStorage.setItem('token', data.access_token)

        window.location.href = '/pages/home.html'
    } catch (error) {
        console.error('Error:', error)
    }
    
    console.log(email, password)
    emailContent.value = ''
    passwordContent.value = ''
}


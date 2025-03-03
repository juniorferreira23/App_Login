import { isEmail, isFullName, isPassword } from "../utils/validators.js";
import { clearSpan } from "./global.js"

const nameContent = document.querySelector('#name')
const emailContent = document.querySelector('#email')
const passwordContent = document.querySelector('#password')
const rePasswordContent = document.querySelector('#re_password')
const btnRegister = document.querySelector('#btn_register')
const spanContent = document.querySelector('#span_message')

emailContent.addEventListener('focus', clearSpan)
btnRegister.addEventListener('click', handlerRegister)

async function handlerRegister() {
    const full_name = nameContent.value
    if (!full_name) {
        spanContent.innerHTML = 'Empty name field'
        return
    } 
    let validator = isFullName(full_name)
    if (validator) {
        spanContent.innerHTML = validator
        return
    }

    const email = emailContent.value
    if (!email){
        spanContent.innerHTML = 'Empty e-mail field'
        return
    } else if (!isEmail(email)){
        spanContent.innerHTML = 'Invalid E-mail'
        return
    }

    const password = passwordContent.value
    const rePassword = rePasswordContent.value
    validator = isPassword(password, rePassword)
    if (validator) {
        spanContent.innerHTML = validator
        return
    }

    try{
        const response = await fetch('http://127.0.0.1:8000/register', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                full_name: full_name,
                username: email,
                password: password,
                re_password: rePassword
            })
        })

        const data = await response.json()

        if (!response.ok) {
            throw new Error(data.detail || 'Error registering')
        }
        
        if (data) {
            nameContent.value = ''
            emailContent.value = ''
            passwordContent.value = ''
            rePasswordContent.value = ''
            clearSpan()
            alert('Registro criado com sucesso')
            window.location.href = 'http://127.0.0.1:3000/index.html'
        }
    } catch (error) {
        console.error('Error:', error)
        spanContent.innerHTML = error.message
    }
}

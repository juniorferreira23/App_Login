export function isEmail (email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return regex.test(email)
}

function hasNumber (str) {
    return /\d/.test(str)
}

function hasSpecialCharacters (str) {
    return /[^a-zA-Z0-9\s]/.test(str)
}

function hasCapitalLetter(str) {
    return /[A-Z]/.test(str);
}

function hasLowercaseLetter(str) {
    return /[a-z]/.test(str);
}

export function isFullName (name) {
    if (hasNumber(name)) {
        return 'The full name field cannot contain numbers'
    }
    if (hasSpecialCharacters(name)) {
        return 'The full name field cannot contain special characters'
    }
    const words = name.trim().split(/\s+/)
    if (words.length < 2) {
        return 'The full name field must contain first and last name'
    }
    words.forEach((word) => {
        if (word.length < 4) {
            return 'The full name field must contain at least 4 characters each word'
        }
    })
    return null
}

export function isPassword(password, rePassword = null) {
    if (!password) {
        return 'Empty password field';
    }
    if (rePassword !== null) {
        if (!rePassword) {
            return 'Empty repeat password field';
        }
        if (password !== rePassword) {
            return 'Different passwords';
        }
    }
    if (password.length < 8) {
        return 'The password must have at least 8 digits';
    }
    if (!hasCapitalLetter(password)) {
        return 'Password must contain capital letters';
    }
    if (!hasLowercaseLetter(password)) {
        return 'Password must contain lowercase letters';
    }
    if (!hasNumber(password)) {
        return 'Password must contain numbers';
    }
    if (!hasSpecialCharacters(password)) {
        return 'Password must contain special characters';
    }
    return null;
}
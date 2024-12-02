document.addEventListener('DOMContentLoaded', function() {
    // Login form validation
    const loginForm = document.querySelector('form[action="/login"]');
    if (loginForm) {
        loginForm.addEventListener('submit', function(event) {
            const username = document.querySelector('input[name="username"]');
            const password = document.querySelector('input[name="password"]');

            if (username.value.trim() === '' || password.value.trim() === '') {
                alert('Username and password cannot be empty!');
                event.preventDefault();
            }
        });
    }

    // Registration form validation
    const registerForm = document.querySelector('form[action="/register"]');
    if (registerForm) {
        registerForm.addEventListener('submit', function(event) {
            const username = document.querySelector('input[name="username"]');
            const email = document.querySelector('input[name="email"]');
            const password1 = document.querySelector('input[name="password1"]');
            const password2 = document.querySelector('input[name="password2"]');
            
            if (username.value.trim() === '' || email.value.trim() === '' || password1.value.trim() === '') {
                alert('All fields must be filled out!');
                event.preventDefault();
            }

            if (password1.value !== password2.value) {
                alert('Passwords do not match!');
                event.preventDefault();
            }
        });
    }
});

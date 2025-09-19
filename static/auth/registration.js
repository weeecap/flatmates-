document.addEventListener('DOMContentLoaded', function() {
    setupPasswordToggle('togglePassword1', 'id_password1');
    setupPasswordToggle('togglePassword2', 'id_password2');
    disableSubmitButton('registerForm', 'Создание аккаунта...');
    
    const password1 = document.getElementById('id_password1');
    const strengthBar = document.getElementById('passwordStrengthBar');
    
    if (password1 && strengthBar) {
        password1.addEventListener('input', function() {
            const password = this.value;
            let strength = 0;
            
            if (password.length >= 8) strength += 25;
            if (/[A-Z]/.test(password)) strength += 25;
            if (/[0-9]/.test(password)) strength += 25;
            if (/[^A-Za-z0-9]/.test(password)) strength += 25;
            
            strengthBar.style.width = strength + '%';
            
            if (strength < 50) {
                strengthBar.style.background = '#dc3545';
            } else if (strength < 75) {
                strengthBar.style.background = '#fd7e14';
            } else if (strength < 100) {
                strengthBar.style.background = '#ffc107';
            } else {
                strengthBar.style.background = '#198754';
            }
        });
    }
});
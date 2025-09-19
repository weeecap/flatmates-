function setupPasswordToggle(toggleId, passwordId) {
    const toggle = document.getElementById(toggleId);
    const password = document.getElementById(passwordId);
    
    if (toggle && password) {
        toggle.addEventListener('click', function() {
            const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
            password.setAttribute('type', type);
            this.innerHTML = type === 'password' ? '<i class="bi bi-eye"></i>' : '<i class="bi bi-eye-slash"></i>';
        });
    }
}

function disableSubmitButton(formId, buttonText = 'Отправка...') {
    const form = document.getElementById(formId);
    if (form) {
        form.addEventListener('submit', function() {
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> ${buttonText}`;
            }
        });
    }
}
// Handle Form Submission
const form = document.getElementById('memberForm');
const registrationContent = document.getElementById('registrationContent');
const successMessage = document.getElementById('successMessage');
const submitBtn = document.getElementById('submitBtn');
const btnText = document.getElementById('btnText');
const btnSpinner = document.getElementById('btnSpinner');

form.addEventListener('submit', function (event) {
    event.preventDefault();

    if (!form.checkValidity()) {
        event.stopPropagation();
        form.classList.add('was-validated');
        return;
    }

    // Simulate Loading State
    submitBtn.disabled = true;
    btnText.textContent = "Submitting...";
    btnSpinner.classList.remove('d-none');

    setTimeout(() => {
        registrationContent.style.display = 'none';
        successMessage.style.display = 'block';
        window.scrollTo(0, 0);
    }, 1500);
});



document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById("myForm");
    const stateSelect = document.getElementById('state');
    const lgaSelect = document.getElementById('lga');
    const roleSelect = document.getElementById("role")
    const errorMessage = document.getElementById("error-message");
    const password = document.getElementById("password")
    const confirmPassword = document.getElementById("confirmPassword")





    function toggleFields() {
        const selectedRole = roleSelect.value;

        document.querySelectorAll('.conditional-fields').forEach(field => {
            field.style.display = 'none';
            field.querySelectorAll('input, select').forEach(input => {
                input.disabled = true;
                input.removeAttribute('required');
            });
        });

        if (selectedRole) {
            const visibleFields = document.querySelectorAll(`.conditional-fields[data-role="${selectedRole}"]`);
            visibleFields.forEach(field => {
                field.style.display = 'block';
                field.querySelectorAll('input, select').forEach(input => {
                    input.disabled = false;
                    input.setAttribute('required', '');
                });
            });
        }
    }

    roleSelect.addEventListener('change', toggleFields);
    toggleFields();

    form.addEventListener("submit",async function (event){
        event.preventDefault();

        errorMessage.textContent = "";


        const phoneNumber = document.getElementById("phone").value
        const nigeriaPhoneRegex = /^(?:(?:(?:\+?234|0)[ -]?)(?:(?:70|80|81|90|91)[ -]?\d{8}|(?:701|802|803|804|805|806|807|808|809|810|811|812|813|814|815|816|817|818|819|901|902|903|904|905|906|907|908|909|910|911|912|913|914|915|916|917|918|919)[ -]?\d{7})|(?:0[7-9][01][0-9][ -]?\d{6}))$/;
        if(!(phoneNumber.match(nigeriaPhoneRegex))){
            errorMessage.textContent = "⚠️ Invalid Number"
            return
        }

        if ((password.value).length <= 4){
            errorMessage.textContent = "Password must be greater than 4 characters"
            return
        }

        if (password.value !== confirmPassword.value) {
            errorMessage.textContent = "⚠️ Passwords don't match!";
            return;
        }


        const formData = {
            first_name: document.getElementById('firstname').value.trim(),
            last_name: document.getElementById("lastname").value.trim(),
            phone_number: document.getElementById("phone").value,
            gender: document.getElementById("gender").value,
            dob: document.getElementById("dob").value,
            email_address : document.getElementById("email").value,
            role: roleSelect.value,
            password: document.getElementById("password").value
        }

        switch (roleSelect.value){
            case "Doctor":
            formData.license = document.getElementById("license").value
            formData.specialization = document.getElementById("specialization").value
        }



        try {
            const response = await fetch(`http://127.0.0.1:8000/register`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(formData),
            });

            if (!response.ok) {
                errorMessage.textContent = response.error;
                const errorData = await response.json();
                console.error("Error details:", errorData);
            } else {
                window.location.href = "../Html/LoginPage.html";
            }
        } catch (error) {
            console.error("Network/request error:", error);
            errorMessage.textContent = "⚠️ Registration Failed. Try again.";
        }
    })

});



document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("myForm");
    const errorMessage = document.getElementById("error-message");
    const togglePassword = document.getElementById("togglePassword");
    const passwordInput = document.getElementById("password");




    form.addEventListener("submit", async function (event) {
        event.preventDefault();


        errorMessage.textContent = "";

        const email = document.getElementById("email").value;
        const password = passwordInput.value

        if (email === "" || password === "") {
            errorMessage.textContent = "⚠️ Please fill in all fields!";
            return;
        }


        const formData = {
            email: email,
            password: password
        };
        try {
            const response = await fetch(`http://127.0.0.1:8000/login`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();

            if (!result.ok) {
                errorMessage.style.color = "red";
                errorMessage.textContent = result.error;
            }else{
                errorMessage.style.color = "green";
                errorMessage.textContent = "✅ Login successful!";
                if(result.role.value === "Doctor"){
                    window.location.href ="../Html/StaffDashBoard.html"
                }else if(result.role.value === "Patient"){
                    window.location.href ="../Html/PatientDashBoard.html"
                }else{
                    window.location.href="../Html/AdminDashBoard.html"
                }
            }


        } catch (error) {
            console.error("Error:", error);
            errorMessage.textContent = "⚠️ Failed to connect to the server.";
        }
    });
});

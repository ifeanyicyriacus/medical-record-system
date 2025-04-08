document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("myForm");
    const errorMessage = document.getElementById("error-message");
    const togglePassword = document.getElementById("togglePassword");
    const passwordInput = document.getElementById("password");


    togglePassword.addEventListener("click", function () {
        const currentType = passwordInput.getAttribute("type");

        if (currentType === "password") {
            passwordInput.setAttribute("type", "text");
            togglePassword.textContent = "🙈";
        } else {
            passwordInput.setAttribute("type", "password");
            togglePassword.textContent = "👁️";
        }
    });

    form.addEventListener("submit", async function (event) {
        event.preventDefault();


        errorMessage.textContent = "";

        const name = document.getElementById("email").value;
        const email = document.getElementById("password").value;

        if (name === "" || email === "") {
            errorMessage.textContent = "⚠️ Please fill in all fields!";
            return;
        }


        const formData = {
            name: name,
            email: email
        };
        const roleSelect = document.getElementById("role")

        const endpointMap = {
            Doctor: "/api/register/doctor",
            Admin: "/api/register/admin",
            Patient: "/api/register/patient"
        };

        const endpoint = endpointMap[roleSelect.value]
        try {
            const response = await fetch(`http://localhost:8080${endpoint}`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(formData)
            }).then(response =>{
                if(response.ok){
                    if(roleSelect.value === "Patient"){
                        window.location.href = "../Html/PatientDashBoard.html"
                    }else if (roleSelect.value === "Doctor"){
                        window.location.href = "../Html/StaffDashBoard.html"
                    }else {
                        window.location.href = "../Html/AdminDashBoard.html"
                    }
                }else{
                    errorMessage.textContent = "Login Failed!!!"
                }
            })

            const result = await response.json();
            console.log("Server Response:", result);

            if (!response.ok) {
                errorMessage.textContent = `⚠️ ${result.message || "Login failed!"}`;
                return;
            }

            errorMessage.style.color = "green";
            errorMessage.textContent = "✅ Login successful!";

        } catch (error) {
            console.error("Error:", error);
            errorMessage.textContent = "⚠️ Failed to connect to the server.";
        }
    });
});

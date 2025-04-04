document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("myForm");
    const errorMessage = document.getElementById("error-message");

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

        try {
            const response = await fetch("http://localhost:5000/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(formData)
            });

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

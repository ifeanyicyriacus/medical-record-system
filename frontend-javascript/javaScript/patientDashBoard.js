document.addEventListener("DOMContentLoaded", function () {
    const navButtons = document.querySelectorAll(".sideBar .nav-btn");
    const sections = document.querySelectorAll(".content-section");

    navButtons.forEach(btn => {
        btn.addEventListener("click", function () {
            const id = this.id + "-content";

            sections.forEach(sec => sec.classList.remove("active"));

            document.getElementById(id).classList.add("active");
        });
    });

    const lastCheck = "20°C / 70Kg |160- 170H/g |27 Bml"

    const check = document.getElementById("last-check")
    check.innerHTML = lastCheck
});

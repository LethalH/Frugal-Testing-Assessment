/* ------------------------------
   INDIA STATE → CITY MAPPING
------------------------------ */
const indiaData = {
    "Uttar Pradesh": ["Lucknow", "Noida", "Kanpur", "Varanasi"],
    "Delhi": ["New Delhi", "Dwarka", "Rohini"],
    "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
    "Karnataka": ["Bengaluru", "Mysuru", "Mangalore"]
};

/* ------------------------------
   POPULATE STATE DROPDOWN
------------------------------ */
country.addEventListener("change", function () {
    state.innerHTML = "";
    city.innerHTML = "";

    if (this.value === "India") {
        Object.keys(indiaData).forEach(s => {
            state.innerHTML += `<option value="${s}">${s}</option>`;
        });
    }
});

/* ------------------------------
   POPULATE CITY DROPDOWN
------------------------------ */
state.addEventListener("change", function () {
    city.innerHTML = "";
    indiaData[this.value].forEach(c => {
        city.innerHTML += `<option value="${c}">${c}</option>`;
    });
});

/* ------------------------------
   PASSWORD STRENGTH
------------------------------ */
password.addEventListener("input", function () {
    let pass = password.value;
    let strength = document.getElementById("passStrength");
    let score = 0;

    if (pass.length >= 6) score++;
    if (/[A-Z]/.test(pass)) score++;
    if (/[0-9]/.test(pass)) score++;
    if (/[^A-Za-z0-9]/.test(pass)) score++;

    if (score <= 1) strength.textContent = "Weak";
    else if (score === 2) strength.textContent = "Medium";
    else strength.textContent = "Strong";
});

/* ------------------------------
   VALIDATE FORM
------------------------------ */
function validateForm() {
    let valid = true;

    function error(id, msg) {
        document.getElementById(id + "Error").textContent = msg;
        document.getElementById(id).classList.add("invalid");
        valid = false;
    }

    function ok(id) {
        document.getElementById(id + "Error").textContent = "";
        document.getElementById(id).classList.remove("invalid");
    }

    /* First Name */
    if (!fname.value.trim()) error("fname", "Required");
    else ok("fname");

    /* Last Name */
    if (!lname.value.trim()) error("lname", "Required");
    else ok("lname");

    /* Email */
    let emailVal = email.value.trim();
    let disposable = ["tempmail.com", "mailinator.com", "10minutemail.com"];

    if (!emailVal) error("email", "Required");
    else if (disposable.some(d => emailVal.endsWith(d))) error("email", "Disposable email not allowed");
    else ok("email");

    /* Phone */
    let ph = phone.value.trim();
    let pattern = /^(91|\+91|0)[0-9]{10}$/;

    if (!ph) error("phone", "Required");
    else if (!pattern.test(ph)) error("phone", "Must start with +91, 91, or 0 and 10 digits");
    else ok("phone");

    /* Gender */
    let genderSelected = document.querySelectorAll("input[name='gender']:checked");
    if (genderSelected.length === 0) {
        document.getElementById("genderError").textContent = "Required";
        valid = false;
    } else {
        document.getElementById("genderError").textContent = "";
    }

    /* Country */
    if (!country.value) error("country", "Required");
    else ok("country");

    /* State */
    if (!state.value) error("state", "Required");
    else ok("state");

    /* City */
    if (!city.value) error("city", "Required");
    else ok("city");

    /* Password match */
    if (password.value !== cpassword.value) {
        document.getElementById("passError").textContent = "Passwords do not match";
        cpassword.classList.add("invalid");
        valid = false;
    } else {
        document.getElementById("passError").textContent = "";
        cpassword.classList.remove("invalid");
    }

    /* Terms */
    if (!terms.checked) {
        document.getElementById("termsError").textContent = "Required";
        valid = false;
    } else {
        document.getElementById("termsError").textContent = "";
    }

    submitBtn.disabled = !valid;
    return valid;
}

/* Real Time Validation */
document.addEventListener("input", validateForm);

/* Submit */
submitBtn.addEventListener("click", function () {
    if (validateForm()) {
        topAlert.className = "alert success";
        topAlert.innerHTML = "Registration Successful!<br>Your profile has been submitted successfully.";
        topAlert.style.display = "block";
    }
});

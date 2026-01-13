document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");
  const username = document.querySelector('input[name="username"]');
  const email = document.querySelector('input[name="email"]');
  const password = document.querySelector('input[name="password"]');
  const submitBtn = document.querySelector(".auth-submit");

  // Utility: show error message
  function showError(message) {
    let errorDiv = document.querySelector(".form-error-js");

    if (!errorDiv) {
      errorDiv = document.createElement("div");
      errorDiv.className = "form-error form-error-js";
      form.prepend(errorDiv);
    }

    errorDiv.textContent = message;
  }

  // Utility: clear error
  function clearError() {
    const errorDiv = document.querySelector(".form-error-js");
    if (errorDiv) errorDiv.remove();
  }

  // Email validation
  function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  // Password strength
  function isStrongPassword(password) {
    return password.length >= 6;
  }

  form.addEventListener("submit", function (e) {
    clearError();

    const usernameVal = username.value.trim();
    const emailVal = email.value.trim();
    const passwordVal = password.value.trim();

    if (usernameVal.length < 3) {
      e.preventDefault();
      showError("Username must be at least 3 characters long.");
      return;
    }

    if (!isValidEmail(emailVal)) {
      e.preventDefault();
      showError("Please enter a valid email address.");
      return;
    }

    if (!isStrongPassword(passwordVal)) {
      e.preventDefault();
      showError("Password must be at least 6 characters long.");
      return;
    }

    // Disable button to prevent double submit
    submitBtn.disabled = true;
    submitBtn.textContent = "Creating account...";
  });

  /* ----------------------------
     Optional: Mobile hamburger
  ----------------------------- */
  const hamburger = document.querySelector(".hamburger");
  const navMenu = document.querySelector(".nav-menu");

  if (hamburger && navMenu) {
    hamburger.addEventListener("click", () => {
      navMenu.classList.toggle("active");
      hamburger.classList.toggle("active");
    });
  }
});

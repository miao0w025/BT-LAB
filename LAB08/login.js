document.addEventListener("DOMContentLoaded", function () {
  const loginBtn = document.getElementById("loginBtn");
  const usernameInput = document.getElementById("username");
  const passwordInput = document.getElementById("password");

  loginBtn.addEventListener("click", function (event) {
    event.preventDefault(); 
    const username = usernameInput.value.trim();
    const password = passwordInput.value.trim();

    let oldMsg = document.querySelector(".login-message");
    if (oldMsg) oldMsg.remove();

    const message = document.createElement("p");
    message.classList.add("login-message");

    if (!username || !password) {
      message.textContent = "Vui lòng nhập thông tin";
      message.style.color = "orange";
    } else if (username === "nghi" && password === "123456") {
      message.textContent = "Đăng nhập thành công";
      message.style.color = "green";
    } else {
      message.textContent = "Sai tên đăng nhập hoặc mật khẩu";
      message.style.color = "red";
    }

    document.querySelector(".login-container").appendChild(message);
  });
});

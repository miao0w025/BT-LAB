document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // chặn reload trang

    let username = document.getElementById("username").value.trim();
    let password = document.getElementById("password").value.trim();
    let message = document.getElementById("message");

    if (username === "" || password === "") {
        message.textContent = "⚠️ Vui lòng nhập đầy đủ Username và Password!";
        message.style.color = "red";
    } else {
        message.textContent = "✅ Đăng nhập thành công!";
        message.style.color = "green";
    }
});

// Nút Cancel sẽ xóa nội dung
document.getElementById("cancelBtn").addEventListener("click", function() {
    document.getElementById("username").value = "";
    document.getElementById("password").value = "";
    document.getElementById("remember").checked = false;
    document.getElementById("message").textContent = "";
});

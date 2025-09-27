document.addEventListener("DOMContentLoaded", function () {
  const payBtn = document.getElementById("payBtn");
  const cardInput = document.getElementById("cardNumber");
  const pinInput = document.getElementById("pin");

  payBtn.addEventListener("click", function (event) {
    event.preventDefault();

    // Xóa message cũ
    let oldMsg = document.querySelector(".pay-message");
    if (oldMsg) oldMsg.remove();

    const message = document.createElement("p");
    message.classList.add("pay-message");

    const card = cardInput.value.trim();
    const pin = pinInput.value.trim();

    if (!card || !pin) {
      message.textContent = "Vui lòng nhập thông tin thanh toán";
      message.style.color = "orange";
    } else if (card === "12345678" && pin === "9999") {
      message.textContent = "Thanh toán thành công";
      message.style.color = "green";
    } else {
      message.textContent = "Thanh toán thất bại, vui lòng thử lại";
      message.style.color = "red";
    }

    document.querySelector(".login-container").appendChild(message);
  });
});

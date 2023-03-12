document.addEventListener("DOMContentLoaded", function() {
  function showMessage() {
    let message = "Ваше сообщение отправлено";
    alert(message);
  }

  const button = document.getElementById("submit-button");

  button.addEventListener("click", showMessage);
});

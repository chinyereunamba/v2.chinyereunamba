const body = document.querySelector("body"),
  nav = document.querySelector("nav"),
  navLinks = document.querySelectorAll(".wrapper .button"),
  burger = document.querySelector(".burger");

let buttons = document.querySelectorAll('.wrapper .button')

burger.addEventListener("click", () => {
  nav.classList.toggle("active");
  burger.classList.toggle("close");
});

navLinks.forEach((btn) =>
  btn.addEventListener("click", () => {
    nav.classList.toggle("active");
    burger.classList.toggle("close");
  })
);

buttons.forEach(button => {
  button.addEventListener('click', function () {
    buttons.forEach(btn => btn.classList.remove('active'));
    this.classList.add('active');
    console.log("Active");
  });
});
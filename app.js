const changeColor = document.querySelector("#changeColor");
const cardElement = document.querySelector(".card");
const headingElement = document.querySelector("h1");

function changeColorPage() {
    cardElement.style.backgroundColor = "beige";

    headingElement.textContent = "changed with javascript!";

    console.log("Clicked on the button!");
}

changeColor.addEventListener("click", changeColorPage);

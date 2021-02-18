// Get the modals
var ingredient_modal = document.getElementById("new-ingredient-modal");
var meal_modal = document.getElementById("new-meal-modal");

// When the user clicks on the button, open the modal
function popUpToggle(id) {
    if (id == 'new-ingredient-button'){
        ingredient_modal.style.display = "block";
    }
    else if (id == 'new-meal-button'){
        meal_modal.style.display = "block";
    }
}
// When the user clicks on <span> (x), close the modal
function closeModal() {
    ingredient_modal.style.display = "none";
    meal_modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == ingredient_modal || event.target == meal_modal) {
    ingredient_modal.style.display = "none";
    meal_modal.style.display = "none";
  }
}
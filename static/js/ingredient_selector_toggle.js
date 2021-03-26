var ingredient_selector = document.getElementById("ingredient-selector-content");
var style = getComputedStyle(ingredient_selector).display

function toggelIngredientSelector() {
    // function to hide or display ingredient selector and meal cards based on screen size
    var style = getComputedStyle(ingredient_selector).display
    if (style == 'none'){
        $("#ingredient-selector-content").attr("style", "display: initial !important;");
    }
    else{
        $("#ingredient-selector-content").attr("style", "display: none;");
        $("#meal-card-container").attr("style", "display: block");
    }
    console.log(window.innerWidth)

    if (style == 'none' && window.innerWidth < 900){
        $("#meal-card-container").attr("style", "display: none");
    }
}

$(window).resize(function(){
    // using toggelIngredientSelector function overrides my css rules so adding this to fix
    if($(this).width() >= 900){
        $("#ingredient-selector-content").attr("style", "display: initial;");
    }
});
    
// any functions required for the add meal modal

function addIngredient(){
    console.log("working")
    const ingredient = $('#ingredient-input').val()
    if ($('#selected-ingredients-content').html() == ''){
        $('#selected-ingredients-content').append(ingredient)
    }
    else{
        $('#selected-ingredients-content').append(', '+ ingredient)
    }
}
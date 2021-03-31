function searchIngredientAutoComplete() {
    // to facilitate the autocomplete functionality in the select ingredients section
    var id = id
    var search = $('#select-ingredient').val()
    var data = {
        search: search
    };
    $.ajax({
        url: '/search.json',
        data: data,
        dataType: 'jsonp',
        jsonp: 'callback',
        jsonpCallback: 'searchResultSearchIngredient'
    });
    
}

function searchResultSearchIngredient(data) {
    $( "#select-ingredient" ).autocomplete ({
        source: data,
        appendTo: "#ac-suggestions"
    });
}

// I admit it's a little lazy to make two of these functions for the two diffrent autocomplete fields
// I will work out how to add the necessary arguments to bring this down to one function in the future
function searchIngredientAddMeal() {
    // to facilitate the autocomplete functionality in the add new meal section
    var id = id
    var search = $('#ingredient-input').val()
    var data = {
        search: search
    };
    $.ajax({
        url: '/search.json',
        data: data,
        dataType: 'jsonp',
        jsonp: 'callback',
        jsonpCallback: 'searchResultAddMeal'
    });
    
}

function searchResultAddMeal(data) {
    $( "#ingredient-input" ).autocomplete ({
        source: data,
        appendTo: "#ingredient-input-ac",
        position:  {of:"#ingredient-input-ac",}
    });
}
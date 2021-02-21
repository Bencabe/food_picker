function selectIngredient() {
    const val = $('#select-ingredient').val()
    if ($('#selected_ingredients').html() == ''){
        $('#selected_ingredients').append(val)
    }
    else{
        $('#selected_ingredients').append(', ' + val)
    }
}

function findMeals() {
    $('#meal-card-container').html('')
    const list = $('#selected_ingredients').html()
    $('#selected_ingredients').html('')
    $.ajax({
        url: 'find_meals/',
        data: {
        'ingredients': list
        },
        dataType: 'json',
        success: function (data) {
            console.log(data)
            for (d in data){
                $('#meal-card-container').append('<div class=meal-card> <div id=meal-card-title>' + data[d].fields.name + '</div> <div class=meal-card-content > Star Rating <br>'+ data[d].fields.star_rating  + '</div> <div class=meal-card-content > Time to Cook <br>'+ data[d].fields.minutes  + ' Minutes </div> </div>')
            }
        }
    });
}
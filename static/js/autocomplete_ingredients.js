function searchOpen() {
    var search = $('#select-ingredient').val()
    var data = {
        search: search
    };
    $.ajax({
        url: '/search.json',
        data: data,
        dataType: 'jsonp',
        jsonp: 'callback',
        jsonpCallback: 'searchResult'
    });
}


function searchResult(data) {
    $( "#select-ingredient" ).autocomplete ({
        source: data,
        appendTo: "#ac-suggestions"
        
    });
}
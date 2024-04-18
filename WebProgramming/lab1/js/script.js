const tableData = $('#result-table > tbody'); // тело таблицы

function validate(value, a, b) {
    if (value >= a && value <= b) {
        return true;
    }
    return false;
}

function validateValues(x, y, r) {
    return validate(x, -2, 2) && validate(y, -3, 5) && validate(r, 1, 3);
} 

$(document).ready(function () {
    $.ajax({
        url: 'php/load.php',
        method: 'GET', 
        dataType: 'html', 
        success: function(data) {
            tableData.html(data);
        }, 
        error: function(error) {
            console.log(error);
        }
    });
});

$('#clear-button').click(() => {
    $.ajax({
        url: 'php/clear.php', 
        method: 'GET', 
        dataType: 'html', 
        success: function(data) {
            tableData.html(data);
        }, 
        error: function(error) {
            console.log(error)
        }
    });
});

$('#coordinates-form').on('submit', function(event) {
    event.preventDefault();
    $('.tip').remove();

    // значения типа string
    let x = $('input[name="x"]:checked').val(); 
    let y = $('#Y-text').val();
    let r = $('input[name="r"]:checked').val();
    // console.log(x + ' ' + typeof x);
    // console.log(y + ' ' + typeof y);
    // console.log(r + ' ' + typeof r);
    // console.log(validateValues(x, y, r));

    if (validateValues(x, y, r)) {
        
        $.ajax({
            url: 'php/send.php',
            method: 'GET',
            dataType: 'html',
            data: {'x': x, 'y': y, 'r': r},
            success: function(data) {
                tableData.html(data)
            }, 
            error: function(error) {
                console.log(error)
            }
        });

    } else {
        // console.log(validate(x, -2, 2));
        // console.log(validate(y, -3, 5));
        // console.log(validate(r, 1, 3));

        if (!validate(x, -2, 2)) {
            $('.x-radios').append('<div class="tip">X должен быть от -2 до 2</div>')
        }

        if (!validate(y, -3, 5)) {
            $('.y-text').append('<div class="tip">Y должен быть от -3 до 5</div>')
        }

        if (!validate(r, 1, 3)) {
            $('.r-radios').append('<div class="tip">R должен быть от 1 до 3</div>')
        }
    }
});
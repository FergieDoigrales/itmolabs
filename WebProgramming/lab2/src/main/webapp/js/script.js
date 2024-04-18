const tableData = $('#result-table > tbody'); // тело таблицы
//let xInput = $('input[name="x"]:checked');
let yInput = $('#Y-text');
let rInput = $('#R-text');

function validate(value, a, b) {
    if (value >= a && value <= b) {
        return true;
    }
    return false;
}

function validateValues(x, y, r) {
    return validate(x, -5, 3) && validate(y, -3, 5) && validate(r, 2, 5);
}

function sendRequest(x, y, r, action) {
    $.ajax({
        url: '/lab/controller',
        method: 'POST',
        dataType: 'html',
        data: {'x': x, 'y': y, 'r': r, 'action': action},
        success: function(data) {
            if (action === 'form') {
                window.location.href = 'jsp/result.jsp';
            } else if (action === 'grap') {
                console.log("График")
                // получить данные и отрисовать их на графике и в таблице
                //window.location.href = 'index.jsp';
                console.log(data)
                jsonObject = JSON.parse(data);
                console.log(jsonObject)
                if (jsonObject != null) {
                    let x = jsonObject["x"];
                    let y = jsonObject["y"];
                    let r = jsonObject["r"];
                    let result = jsonObject["result"];
                    let timeExec= jsonObject["time"];
                    console.log(x + ' ' + y + ' ' + r + ' ' + result + ' ' + timeExec)

                    // отрисовка точки на графике
                    let pointString = `<circle id="point" r="4" cx="${((300 / 2 + (x + 0.02) / r * 100))}" cy="${((300 / 2 + (y - 0.02) / r * -100))}" fill="${result ? "green" : "red"}" stroke="white" />`;
                    console.log(pointString)
                    $('svg').html($('svg').html() + pointString);

                    // добавление данных в таблицу
                    let tBodyString = `<tr class="${result ? "table-response-right" : "table-response-wrong"}">
                                    <th>${x}</th>
                                    <th>${y}</th>
                                    <th>${r}</th>
                                    <th>${timeExec}</th>
                                    <th>${result ? "Попал" : "Мимо"}</th> 
                                </tr>`;
                    console.log(tBodyString)
                    tableData.prepend(tBodyString);

                }
            } else if (action === 'clear') {
                window.location.reload();
            }

        },
        error: function(error) {
            console.log(error)
        }
    });
}

$('svg').mousedown(function(event) {

    const r = rInput.val();

    if (validate(r, 2, 5)) {
        const position = $('svg').offset();
        const rowX = event.pageX - position.left;
        const rowY = event.pageY - position.top;
        //console.log('x ' + rowX + ' y ' + rowY);

        const x = (((r / 50) * (262 / 2 - rowX) * -1) / 2 - 0.2 * r).toFixed(2);
        const y = (((r / 50) * (262 / 2 - rowY)) / 2 + 0.2 * r).toFixed(2);
        //console.log('x ' + x + ' y ' + y);

        sendRequest(x, y, r, 'grap');
    } else {
        alert('R должен быть от 2 до 5');
    }
});


$('#coordinates-form').on('submit', function(event) {
    event.preventDefault();
    $('.tip').remove();

    let x = $('input[name="x"]:checked').val();
    let y = yInput.val();
    let r = rInput.val();

    //console.log(x + ' ' + typeof x);
    // console.log(y + ' ' + typeof y);
    // console.log(r + ' ' + typeof r);


    if (validateValues(x, y, r)) {
        console.log('data valid');
        sendRequest(x, y, r, 'form')

    } else {
        // console.log(validate(x, -2, 2));
        // console.log(validate(y, -3, 5));
        // console.log(validate(r, 1, 3));

        if (!validate(x, -5, 3)) {
            $('.x-radios').after('<div class="tip">X должен быть от -5 до 3</div>')
        }

        if (!validate(y, -3, 5)) {
            yInput.after('<div class="tip">Y должен быть от -3 до 5</div>')
        }

        if (!validate(r, 2, 5)) {
            rInput.after('<div class="tip">R должен быть от 2 до 5</div>')
        }
    }
});

$('#clear-button').click((event) => {
    event.preventDefault();
    sendRequest(0,0, 0, 'clear');
    console.log('Удачно очищена таблица');
});
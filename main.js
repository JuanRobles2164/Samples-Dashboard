
$('#fechaRangoSeleccion').daterangepicker();

$(document).ready(function () {
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
});

//var csv is the CSV file with headers
function csvJSON(csv) {

    var lines = csv.split("\n");

    var result = [];

    // NOTE: If your columns contain commas in their values, you'll need
    // to deal with those before doing the next step 
    // (you might convert them to &&& or something, then covert them back later)
    // jsfiddle showing the issue https://jsfiddle.net/
    var headers = lines[0].split(",");

    for (var i = 1; i < lines.length; i++) {

        var obj = {};
        var currentline = lines[i].split(",");

        for (var j = 0; j < headers.length; j++) {
            obj[headers[j]] = currentline[j];
        }

        result.push(obj);

    }

    //return result; //JavaScript object
    return JSON.stringify(result); //JSON
}

function proccessContent(idElemento) {
    let url = "https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv";

    fetch(url)
    .then((response) => response.text())
    .then((response) => csvJSON(response))
    .then((response) => {
        let objetos = JSON.parse(response);
        let labels_x = [];
        let labels_y = [];
        objetos.forEach(element => {
            labels_x.push(element.AAPL_x);
            labels_y.push(element.AAPL_y);
        });
        let data = [{
            x: labels_x,
            y: labels_y,
            type: 'scatter'
        }];
        let layout = {
            height: 400,
            width: 500,
        };
        Plotly.newPlot(idElemento, data, layout);
    });

}

function renderPieChart(){
    let data = [{
        values: [50, 30, 20],
        labels: ['Fase A', 'Fase B', 'Fase C'],
        type: 'pie'
    }];
    let layout = {
        height: 400,
        width: 500,
    };

    Plotly.newPlot('pieChart', data, layout);
}

function renderCurvaCargaChart1(){
    proccessContent('curvaCargaChart');
}

function renderCurvaCargaChart2(){
    proccessContent('curvaCargaChart2');
}

function renderAllCharts(){
    renderPieChart();
    renderCurvaCargaChart1();
    renderCurvaCargaChart2();
}
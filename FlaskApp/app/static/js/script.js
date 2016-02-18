/* this is a js file for index page */

function createChart(seriesOptions, divId) 
{
    $(divId).highcharts('StockChart', {

        rangeSelector: {
            selected: 4
        },

        yAxis: {
            labels: {
                formatter: function () {
                    return (this.value > 0 ? ' + ' : '') + this.value + '%';
                }
            },
            plotLines: [{
                value: 0,
                width: 2,
                color: 'silver'
            }]
        },

        plotOptions: {
            series: {
                compare: 'percent'
            }
        },

        tooltip: {
            pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> ({point.change}%)<br/>',
            valueDecimals: 2
        },

        series: seriesOptions
    });
}

// combine charts together
function combineCharts(divId, stockSymbols, seriesOptions, seriesCounter) 
{
    /**
     * Create the chart when all data is loaded
     * @returns {undefined}
     */
   $.each(stockSymbols, function (i, name) 
   {
        $.getJSON('https://www.highcharts.com/samples/data/jsonp.php?filename=' + name.toLowerCase() + '-c.json&callback=?', function (data) 
        {

            seriesOptions[i] = {
                name: name,
                data: data
            };
            // As we're loading the data asynchronously, we don't know what order it will arrive. So
            // we keep a counter and create the chart when all the data is loaded.
            seriesCounter += 1;
            if (seriesCounter === stockSymbols.length) 
            {
                createChart(seriesOptions, divId);
            }
        });
    });
}

// main function to call charts
$(document).ready(function () {
    var stockSymbolsG = ['MSFT', 'AAPL', 'GOOG'];
    combineCharts("#container", stockSymbolsG, [], 0);
    // add more charts here
});
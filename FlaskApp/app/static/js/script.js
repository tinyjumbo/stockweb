/* this is a js file for index page */
var slideIndex = 1;
function bar_chart(){
	    $('#container1').highcharts({
        data: {
            table: 'datatable'
        },
        chart: {
            type: 'column'
        },
        title: {
            text: 'Tweets count'
        },
		xAxis: {       
    		ordinal: false,
			type: 'datetime'
		},
        yAxis: {
            allowDecimals: false,
            title: {
                text: 'Units'
            }
        },
        tooltip: {
            formatter: function () {
                return '<b>' + this.series.name + '</b><br/>' +
                    this.point.y;
            }
        }
    });
	
}
function tweet_card(){
	
	
}

function plusDivs(n) {
  showDivs(slideIndex += n);
}

function currentDiv(n) {
  showDivs(slideIndex = n);
}

function showDivs(n) {
  var i;
  var x = document.getElementsByClassName("tweet-card");
  if (n > x.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = x.length} ;
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";  
  }
  x[slideIndex-1].style.display = "block";  
}
function line_chart(company){
	$('#container0').highcharts({
        data: {
            table: company+'-table'
        },
        chart: {
            type: 'line'
        },
        title: {
            text: 'Scores calculated'
        },
		xAxis: {       
    		ordinal: false,
			type: 'datetime'
		},
        yAxis: {
            allowDecimals: false,
            title: {
                text: 'Units'
            }
        },
        tooltip: {
            formatter: function () {
                return '<b>' + this.series.name + '</b><br/>' +
                    this.point.y;
            }
        }
    });
}
// main function to call charts
$(document).ready(function () {
	line_chart('google');
	bar_chart();
    
    showDivs(slideIndex);
    $('.tabs nav a').on('click', function() {
        show_content($(this).index());
    });

    show_content(0);

    $('#company-select').searchableOptionList({
		events: {            
            onChange: function(sol,changedElements) {
				var company = sol.getSelection()[0].value;
				line_chart(company);
				
            }
		},
        maxHeight: '100px'
    });

    $( "#from" ).datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 3,
        onClose: function( selectedDate ) {
            $( "#to" ).datepicker( "option", "minDate", selectedDate );
        }
    });
    $( "#to" ).datepicker({
        defaultDate: "+1w",
        changeMonth: true,
        numberOfMonths: 3,
        onClose: function( selectedDate ) {
            $( "#from" ).datepicker( "option", "maxDate", selectedDate );
        }
    });
});
function show_content(index) {
    if(index === 0){
		$("#filter").show();
    }
	else{
		$("#filter").hide();
	}
    // Make the content visible
    $(".tabs .content").hide();
    $("#container"+index).show();

    // Set the tab to selected
    $('.tabs nav a.selected').removeClass('selected');
    $('.tabs nav a:nth-of-type(' + (index + 1) + ')').addClass('selected');
}

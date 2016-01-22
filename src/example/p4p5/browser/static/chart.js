$(document).ready(function() {
    var chart = $('#chart');
    var done = parseInt(chart.attr('done'));
    var inprogress = parseInt(chart.attr('inprogress'));
    var total = done + inprogress;
    if(total == 0) {
        total = 1;
    }
    var done_rate = Math.round(100 * done / total);
    var inprogress_rate = Math.round(100 * inprogress / total);
    chart.append('<div class="done" style="width:'+done_rate+'%">&nbsp;</div>');
    chart.append('<div class="inprogress" style="width:'+inprogress_rate+'%">&nbsp;</div>');
});
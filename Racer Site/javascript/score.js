/**
 * Created by Michael Jes Þórsson on 21-Nov-16.
 * This Script will be used to power the search engine in the score table and other
 */
var $rows = $('#table tr');
$('#tableSearch').keyup(function() {

    var val = '^(?=.*\\b' + $.trim($(this).val()).split(/\s+/).join('\\b)(?=.*\\b') + ').*$',
        reg = RegExp(val, 'i'),
        text;

    $rows.show().filter(function() {
        text = $(this).text().replace(/\s+/g, ' ');
        return !reg.test(text);
    }).hide();
});
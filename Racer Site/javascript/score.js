/**
 * Created by Michael Jes Þórsson on 21-Nov-16.
 * This Script will be used to power the search engine in the score table and other
 */

var score_fetch = function() {
    $.ajax({
        url: "../php/fetchScore.php",
        type: "POST",
        cache: false,
        success: function(html){
            $('#score-table').empty();
            $('#score-table').append(html);
        },
        failure: function (html){
            unexpected_error(html)
        }
    });
};
score_fetch();

$("#score-search").on('keyup', function(){
    if($.trim($("#score-search").val()) == ""){
        $('#score-table').empty();
        $('#score-table').append(score_fetch);
    }else{
        $.ajax({
            url: "../php/lookupScore.php",
            type: "POST",
            cache: false,
            data: {
                user_input: $.trim($("#score-search").val())
            },
            success: function(html){
                $('#score-table').empty();
                $('#score-table').append(html);
            },
            failure: function (html){
                unexpected_error(html)
            }
        });
    }
});

function unexpected_error(caught_error){
    $('#error-text').remove();

    $('.row').after($('' +
        '<div class="col s12 m6">' +
            '<div class="card grey lighten-5">' +
                '<div class="card-content red-text">' +
                    '<span class="card-title">Fatal Error</span>' +
                    '<p>If you are seeing this text it means that something has gone horribly wrong. Please be in contact at vorur.mail@gmail.com and send us the automatically generated error: </p>' +
                    caught_error +
                '</div>' +
            '</div>' +
        '</div>'));
}
// Small script for get JSONP from server.

function search_function(e){
	$('.my-new-list').remove();
$("#search_field").empty();
$.getJSON( "index.cgi?action=search_query&query=" + e + "", function( data ) {
  var items = [];
  $.each( data, function( key, val ) {
    items.push( "<a href=?action=notes&id=" + val[0] + ">" + val[1] + "</a></li>" );
  });
 
  $( "<ul/>", {
    "class": "my-new-list",
    html: items.join( "<br>" )
  }).appendTo( $( "#search_view" ) );
});

}



   function toSubmit(){
        var sok_ord = $('#search_field').val();
        search_function(sok_ord);
        return false;
   }


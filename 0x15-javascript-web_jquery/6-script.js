$("DIV#update_header").click(function(){
	$("DIV.update_header").replaceWith( "<div>" + $( this ).text("New Header") + "</div>" ) ;
});

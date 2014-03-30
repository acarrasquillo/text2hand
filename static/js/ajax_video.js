$("#traslate").on('click', fuction(e){
	$.ajax({
  		type: "POST",
  		url: "/trans",
  		data: { body: "I will eat pizza tomorrow" }
	})
  	.done(function( msg ) {
    	alert( "VIDEO LINK: " + msg );
  	});
});
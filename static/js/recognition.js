var recognition;

if (window.webkitSpeechRecognition) {
  recognition = new webkitSpeechRecognition();
  recognition.continuous = true;
  recognition.interimResults = false;
  recognition.onresult = function(event) {
    var i;
    return $('#transcript').text($('#transcript').text() + ((function() {
      var _i, _ref, _ref1, _results;
      _results = [];
      for (i = _i = _ref = event.resultIndex, _ref1 = event.results.length - 1; _i <= _ref1; i = _i += 1) {
        _results.push(event.results[i][0].transcript);
      }
      return _results;
    })()).join(''));
  };
  $('#startStopButton').on('click', function() {
    if (this.value === 'Start') {
      this.value = 'Stop';
      recognition.lang = 'en-AU';
      return recognition.start();
    } else {
      this.value = 'Start';
      return recognition.stop();
    }
  });
} else {
  alert('Cannot access the speech recognition API.  Are you using Chrome 25+ ?');
}

$("#trans").click(function(e){
      text = $("#transcript").val();
      $.ajax({
          type: "POST",
          url: "/trans",
          data: { body: text }
      })
      .done(function( msg ) {
          $("#video_container").html('<video controls autoplay><source src="./static/' + msg + '"</video>');
          $("#video_share").attr('value', 'static/'+ msg);
      });

});


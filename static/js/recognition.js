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
    if (this.innerText === 'Start') {
      this.innerText = 'Stop';
      recognition.lang = 'en-AU';
      return recognition.start();
    } else {
      this.innerText = 'Start';
      return recognition.stop();
    }
  });
} else {
  alert('Cannot access the speech recognition API.  Are you using Chrome 25+ ?');
}

$('#translate').on('click', function() {
  return $('#prueba').text($("#transcript").val());
});
if window.webkitSpeechRecognition
	recognition = new webkitSpeechRecognition()
	recognition.continuous = true # if false, speech recognition will end when the user stops talking, otherwise it keeps on recording until it is stopped manually
	recognition.interimResults = false # if false, the only results returned by the recognizer are final and will not change

	recognition.onresult = (event) -> $('#transcript').text $('#transcript').text() + (event.results[i][0].transcript for i in [event.resultIndex..event.results.length - 1] by 1).join('')

	$('#startStopButton').on 'click', ->
		if this.innerText == 'Start'
			this.innerText = 'Stop'
			recognition.lang = 'en-AU' # see https://github.com/GoogleChrome/webplatform-samples/blob/master/webspeechdemo/webspeechdemo.html#L138 for other languages
			recognition.start()
		else
			this.innerText = 'Start'
			recognition.stop()
else
	alert 'Cannot access the speech recognition API.  Are you using Chrome 25+ ?'

$('#translate').on 'click', ->
	$('#prueba').text($("#transcript").val())
      

# Sources
# -------
# http://updates.html5rocks.com/2013/01/Voice-Driven-Web-Apps-Introduction-to-the-Web-Speech-API

###
TODOCK:
use div with contenteditable="true"

if webkitSpeechRecognition
	$recordButton = $('#recordButton')
	$transcript = $('#transcript')

	recognising = false

	recognition = new webkitSpeechRecognition()
	recognition.continuous = true
	recognition.interimResults = true
	recognition.lang = 'en-AU'
	recognition.onstart = -> $recordButton.prop 'src', 'images/mic-animate.gif'
	recognition.onend = ->
		$recordButton.prop 'src', 'images/mic.gif'
		recognising = false
	recognition.onresult = (event) ->
		finalTranscript = ''
		interimTranscript = ''
		for i in [event.resultIndex..event.results.length - 1] by 1
			if event.results[i].isFinal
				finalTranscript += event.results[i][0].transcript
			else
				interimTranscript += event.results[i][0].transcript

		$('.interim-transcript').remove()
		$transcript.html "#{$transcript.html()}#{finalTranscript}<span class='interim-transcript'>#{interimTranscript}</span>"

	$recordButton.on 'click', ->
		if recognising
			recognition.stop()
		else
			$recordButton.prop 'src', 'images/mic-slash.gif'
			recognition.start()
			recognising = true
###
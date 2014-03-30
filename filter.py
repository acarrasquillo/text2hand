from string import punctuation

ARTICLES_LIST = [
	'a',
	'an',
	'the',
	'will'
	]

TIME_LIST = [
	'after',
	'always',
	'before',
	'during',
	'lately',
	'never',
	'often',
	'rarely',
	'recently',
	'sometimes',
	'soon',
	'today',
	'tomorrow',
	'usually',
	'yesterday',
]

def getSentences(text):
	text = text.lower()	#Convert text to lower case

	sentences_list = text.split('. ') #create a sentences list

	#characters to exclude 
	exclude = punctuation
	#removing '.' from exlude list to solve the e.g. problem
	exclude = exclude.replace('.','')

	# remove punctuations from text sentences
	
	new_sentences_list = []

	for sentence in sentences_list:
		sentence = ' '.join(filter(None, (word.strip(exclude) for word in sentence.split())))
		#if last element of the sentence is a point remove it
		if sentence[-1]=='.':
			sentence = sentence[:-1] 
		#append sentence to sentence list 
		new_sentences_list.append(sentence)

	return new_sentences_list # return  text string without punctuation

	

def getWords(sentence_array):
	sentences_dict = dict()

	# for each sentence
	for indx,sentence in enumerate(sentence_array):
		
		#list of words to return
		word_list = list()

		#time words in sentence
		timew_list = list()
		
		# for each word in the sentence
		for word in sentence.split(" "):

			# If word isn't in ARTICLES_LIST add it to word_list
			if word not in ARTICLES_LIST:
				#if word is a time word add it to the list
				if word in TIME_LIST:
					timew_list.insert(0,word)
				else:
					word_list.append(word)
				
		#insert time word in front
		for word in timew_list:
			word_list.insert(0,word)
		# insert in dictionary sentence # words	
		sentences_dict[indx] = word_list

	# return sentence dict
	return sentences_dict
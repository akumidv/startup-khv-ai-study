const natural = require('natural')

// const phrase = 'Один не разберет, чем пахнут розы. Другой из горьких трав добудет мед. Кому-то мелочь дашь, навек запомнит. Кому-то жизнь отдашь, а он и не поймет'
const phrase = 'Если вы не можете объяснить это своей бабушке, вы сами этого не понимаете'


let tokenizer = new natural.WordTokenizer();
tokens = tokenizer.tokenize(phrase)
console.log('Токены', tokens);


const stemmer = tokenizer.tokenize(phrase).map(item => natural.PorterStemmerRu.stem(item))
console.log('Стеммы', stemmer)

Exercise for Spacy POS tutorial,

1) You are parsing a news story from cnbc.com. News story is stores in [news_story.txt](https://github.com/codebasics/nlp-tutorials/blob/main/7_pos/news_story.txt) which is available in this same folder on github. You need to,
   1) Extract all NOUN tokens from this story. You will have to read the file in python first to collect all the text and then extract NOUNs in a python list
   2) Extract all numbers (NUM POS type) in a python list
   3) Print a count of all POS tags in this story

[Solution](https://github.com/codebasics/nlp-tutorials/blob/main/7_pos/Exercise/pos_exercise_solution.ipynb)

text = '''Inflation rose again in April, continuing a climb that has pushed consumers to the brink and is threatening the economic expansion, the Bureau of Labor Statistics reported Wednesday.

The consumer price index, a broad-based measure of prices for goods and services, increased 8.3% from a year ago, higher than the Dow Jones estimate for an 8.1% gain. That represented a slight ease from March’s peak but was still close to the highest level since the summer of 1982.

Removing volatile food and energy prices, so-called core CPI still rose 6.2%, against expectations for a 6% gain, clouding hopes that inflation had peaked in March.

The month-over-month gains also were higher than expectations — 0.3% on headline CPI versus the 0.2% estimate and a 0.6% increase for core, against the outlook for a 0.4% gain.

The price gains also meant that workers continued to lose ground. Real wages adjusted for inflation decreased 0.1% on the month despite a nominal increase of 0.3% in average hourly earnings. Over the past year, real earnings have dropped 2.6% even though average hourly earnings are up 5.5%.

Inflation has been the single biggest threat to a recovery that began early in the Covid pandemic and saw the economy in 2021 stage its biggest single-year growth level since 1984. Rising prices at the pump and in grocery stores have been one problem, but inflation has spread beyond those two areas into housing, auto sales and a host of other areas.

Federal Reserve officials have responded to the problem with two interest rate hikes so far this year and pledges of more until inflation comes down to the central bank’s 2% goal. However, Wednesday’s data shows that the Fed has a big job ahead.

Credits: cnbc.com'''
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
names = [name.text for name in doc if name.pos_ == "NOUN"]
nums  = [num.text  for num  in doc if num.pos_  == "NUM"]
counts = doc.count_by(spacy.attrs.POS)
print(names,"\n",nums,"\n",counts)


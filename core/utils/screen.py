from html2image import Html2Image

def run(self, q): 
	try:
		url = q['query']
		file_name = (url+'.png').split(r'http:')[-1].replace('/','')

		self.info(f"screen: Attempting in taking a screenshot of {q['query']}...")
		res = Html2Image(output_path='data/screenshots/')
		res.screenshot(url=url, save_as=file_name)
	except:
		self.error(f"screen: Something went wrong. Please try again.")
		return False
	
	return True

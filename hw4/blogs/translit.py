TRANSLIT = {"а":"a","б":"b","м":"m","п":"p","р":"r","в":"v","с":"s","ы": "y","л":"l", "у":"u", " ":" ","г":"g","т":"t","д":"d", "е":"e","ф":"f","ё":"yo","х":"kh", "ж":"zh","ц":"ts","з":"z","ч":"ch","и":"i","ш":"sh","й":"i","щ":"shch", "к":"k","ъ":"'", "ь":"'","э":"e", "н":"n","ю":"yu","о":"o","я":"ya"}

def transliter(str):
	str_low=str.lower()
	trans_slug=(str_low.translate(str_low.maketrans(TRANSLIT))).capitalize()
	return (trans_slug)
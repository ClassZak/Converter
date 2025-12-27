from mediatype import MediaType

class Media:
	def __init__(self, name:str='', media_format:str='', data:bytes=b'', media_type:MediaType=MediaType.AUDIO):
		self.name = name
		self.media_format = media_format
		self.data = data


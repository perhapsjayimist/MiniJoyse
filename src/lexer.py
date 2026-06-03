class Lexer:
	def __init__(self, text: str):
		self.text = text
		self.pos = 0
		self.tokens = []

	def get_char(self):
		return self.text[self.pos]

	def match_char(self, match: str):
		return self.get_char() == match

	def read_str(self, quot):
		start = self.pos
		self.pos += 1  # skip opening quote

		while self.pos < len(self.text) and not self.match_char(quot):
			self.pos += 1

		value = self.text[start + 1:self.pos]  # exclude quotes
		self.pos += 1  # skip closing quote

		self.tokens.append(("STR", value))

	def read_ident(self):
		start = self.pos

		if not (self.get_char().isalpha() or self.match_char("_")):
			return

		self.pos += 1

		while self.pos < len(self.text):
			if self.get_char().isalnum() or self.match_char("_"):
				self.pos += 1
			else:
				break

		value = self.text[start:self.pos]
		self.tokens.append(("IDENT", value))

	def read_eol(self):
		self.tokens.append(("EOL", None))
		self.pos += 1

	# def read_separator(self):
	# 	self.tokens.append(("SEP", None))
	# 	self.pos += 1

	def read_comment(self):
		while self.pos < len(self.text) and not self.match_char("\n"):
			self.pos += 1

	def process(self) -> list[tuple]:
		while self.pos < len(self.text):
			char = self.get_char()

			if char == "#":
				self.read_comment()
				continue

			elif char == '"':
				self.read_str('"')
				continue
				
			elif char == "'":
				self.read_str("'")
				continue

			elif char == "\n" or char == ";":
				self.read_eol()
				continue

			elif char == " ":
				self.pos += 1
				continue

			elif char.isalpha():
				self.read_ident()
				continue

			else:
				self.pos += 1

		return self.tokens
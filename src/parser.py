class Parser:
	def __init__(self, tokens: list):
		self.tokens = tokens
		self.nodes = []
		self.pos = 0

	def get_token(self):
		return self.tokens[self.pos]

	def advance(self):
		self.pos += 1

	def skip_eol(self):
		while self.pos < len(self.tokens) and self.get_token()[0] == "EOL":
			self.advance()

	def parse_call(self):
		name = self.get_token()[1]
		self.advance()

		args = []

		while self.pos < len(self.tokens):
			tok_type, tok_value = self.get_token()

			if tok_type == "EOL":
				break

			args.append(tok_value)
			self.advance()

		return {
			"type": "call",
			"name": name,
			"args": args
		}

	def process(self) -> list:
		while self.pos < len(self.tokens):
			self.skip_eol()

			if self.pos >= len(self.tokens):
				break

			token = self.get_token()

			if token[0] == "IDENT":
				node = self.parse_call()
				self.nodes.append(node)
				continue

			self.advance()

		return self.nodes
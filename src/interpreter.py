class Interpreter:
	def __init__(self, nodes, env, keywords):
		self.nodes = nodes
		self.env = env
		self.keywords = keywords

	def run(self):
		for node in self.nodes:
			self.execute_call(node)

	def execute_call(self, node):
		name = node["name"]
		args = node["args"]

		if name in self.env:
			self.env[name](*args)
		else:
			print(f"Unknown function: {name}")
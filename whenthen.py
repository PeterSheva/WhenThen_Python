
def whenthen(functiontion):
	class WhenThen:
		def __init__(self, functiontion):
			self.function = functiontion
			self._when = []
			self._then = []

		def __call__(self, *args, **kwargs):
			if(len(self._when) != len(self._then)):
				raise NoWhenException()
			for idx, function in enumerate(self._when):
				if function(*args, **kwargs):
					return self._then[idx](*args, **kwargs)
			return self.function(*args, **kwargs)

		def when(self, functiontion):
			if(len(self._when) != len(self._then)):
				raise NoWhenException()
			else:
				self._when.append(functiontion)
			return self

		def then(self, functiontion):
			if(len(self._when) - len(self._then) != 1):
				raise NoThenException()
			else:
				self._then.append(functiontion)
			return self
	return WhenThen(functiontion)

@whenthen
def fract(x):
    return x * fract(x - 1)

@fract.when
def fract(x):
    return x == 0

@fract.then
def fract(x):
    return 1

@fract.when
def fract(x):
    return x > 5

@fract.then
def fract(x):
    return x * (x - 1) * (x - 2) * (x - 3) * (x - 4) * fract(x - 5)

if __name__ == "__main__":
    print(fract(0))
    print(fract(1))
    print(fract(5))

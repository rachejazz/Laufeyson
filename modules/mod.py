import core as u

def mod_run(self, util):
	real = getattr(u, util)
	real.run(self)
	self.info("Module mod worked!")
	path = 'hey'


from .commands.wocker import Wocker
from .commands.image import Image

def entry():
	Wocker.wocker( obj = {} )

if __name__ == "__main__":
	entry()

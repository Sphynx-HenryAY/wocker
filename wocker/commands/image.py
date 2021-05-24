import click
from .wocker import Wocker

class Image:

	@Wocker.wocker.group()
	@click.pass_context
	def image( ctx ):
		print( f"Image.image: {ctx}" )

	@image.command()
	@click.pass_context
	def pull( ctx ):
		print( f"Image.ls: {ctx}" )

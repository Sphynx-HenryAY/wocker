import click

class Wocker:

	@click.group()
	@click.pass_context
	def wocker( ctx ):
		print( f"Wocker.wocker: {ctx}" )

#!/usr/bin/env python
import click

@click.command()
def hello():
    click.echo('HEllo world')
    
    
if __name__=='__main__':
    hello()
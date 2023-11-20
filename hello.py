#!/usr/bin/env python
"""This a cli """

import click
from mylib.myadd import add

@click.command()
@click.option('--value1', help="1st number to add")
@click.option('--value2', help="2nd number to add")

def calculate(value1, value2):
    result = add(value1, value2)
    click.echo(click.style(f'Adding numbers: {value1}, {value2}', fg='red'))
    click.echo(click.style(f'Result: {result}', fg='red'))
    
if __name__ == '__main__':
    #pylint: disable=no-value-for-parameter
    calculate()

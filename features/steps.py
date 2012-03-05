from lettuce import *
from nose.tools import *

from defaultdict2 import defaultdict2

@step('I have an increment-by-one defaultdict2')
def increment_by_one_defaultdict2(step):
    world.d = defaultdict2(lambda k: k + 1)

@step('I assign the value (\d+) to the key (\d+)')
def assignment(step, value, key):
    key, value = int(key), int(value)

    world.d[key] = value

@step(u'It should contain the key (\d+)')
def membership(step, key):
    key = int(key)

    assert_true(key in world.d)

@step(u'It does not contain the key (\d+)')
def non_membership(step, key):
    key = int(key)

    assert_false(key in world.d)

@step(u'I should be able to retrieve the value (\d+) for the key (\d+)')
def subscript(step, value, key):
    key, value = int(key), int(value)

    assert_equals(value, world.d[key])

@step(u'Insert some values')
def insert_some_values(step):
    for row in step.hashes:
        key, value = int(row["key"]), int(row["value"])
        world.d[key] = value

@step(u'It should look like (.+)')
def look_like(step, code):
    expected = eval(code)
    assert_equals(expected, world.d)

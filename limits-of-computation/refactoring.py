# when refactoring, we'd like to know if the changed code
# has the same output as the initial code

def fns_are_equivalent(f, g):
  pass


def halts(f):
  def inner():
    f()
    return 0
  def inner2():
    return 0
  return fns_are_equivalent(inner, inner2)

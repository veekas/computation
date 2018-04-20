# compiler trying to generalize a rule for determining if a function
# always returns a constant

def returns_constant(f):
  pass

def halts(f):
  def inner():
    f()
    return 0
  return returns_constant(inner)

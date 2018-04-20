# Church numerals -> identity -> add -> multiply
ZERO = lambda f: lambda x: x
# ONE = lambda f: lambda x: f(x)
# IDENTITY = lambda n: (lambda f: lambda x: n(f)(x))
ADD1 = lambda n: (lambda f: lambda x: f(n(f)(x)))
ADD = lambda n: lambda m: n(ADD1)(m)
MULT = lambda n: lambda m: n(lambda acc: ADD(m)(acc))(ZERO)

SUB1 = (
  lambda n:
  lambda f:
  lambda x: n (lambda g: lambda h: h(g(f)))
              (lambda u: x)
              (lambda u: u)
)

NULL = lambda x: x
TRUE = lambda t: lambda f: t(NULL)
FALSE = lambda t: lambda f: f(NULL)
IF = lambda cond: lambda t: lambda f: cond(t)(f)
IS_ZERO = lambda n: n(lambda x: FALSE)(TRUE)

ONE = ADD1(ZERO)
SIX = ADD1(ADD1(ADD1(ADD1(ADD1(ONE)))))

print(
  (
    lambda myself: (
      lambda n: (
        IF(
          IS_ZERO(n)
        )(
          lambda _: ONE
        )(
          lambda _: MULT(n)( myself(myself)(SUB1(n)) )
        )
      )
    )
  )(
    lambda myself: (
      lambda n: (
        IF(
          IS_ZERO(n)
        )(
          lambda _: ONE,
        )(
          lambda _: MULT(n)(myself(myself)(SUB1(n)))
        )
      )
    )
  )
  (SIX)
  # the following line just converts the lambda function to a python number
  (lambda x: x + 1)(0)
)

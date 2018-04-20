IF = lambda cond: lambda t_func: lambda f_func: t_func(None) if cond else f_func(None)
IS_ZERO = lambda x: x == 0
ONE = 1
MULT = lambda x: lambda y: x * y
SUB1 = lambda x: x - 1

print(
  (
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
  (6)
)

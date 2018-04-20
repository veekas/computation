print(
  (
    lambda myself: (
      lambda n: (
        (
          lambda cond: lambda t: lambda f: cond(t)(f)
        )(
          (
            lambda n: n(
              lambda x: (
                lambda t: lambda f: f(lambda x: x)
              )
            )
            (lambda t: lambda f: t(lambda x: x))
          )
          (n)
        )(
          lambda _: (
            lambda n: (
              lambda f: lambda x: f(n(f)(x))
            )
          )
          (lambda f: lambda x: x)
        )(
          lambda _: (
            lambda n: lambda m: n(
              lambda acc: (
                  lambda n: lambda m: n(
                    lambda n: lambda f: lambda x: f(n(f)(x))
                  )
                  (m)
              )
              (m)
              (acc)
            )
            (lambda f: lambda x: x)
          )
          (n)
          (
            myself(
              myself
            )(
              (
                lambda n:
                lambda f:
                lambda x: n(lambda g: lambda h: h(g(f)))
                (lambda u: x)
                (lambda u: u)
              )
              (n)
            )
          )
        )
      )
    )
  )(
    lambda myself: (
      lambda n: (
        (
          lambda cond: lambda t: lambda f: cond(t)(f)
        )(
            lambda n: n(
              lambda x: (
                lambda t: lambda f: f(lambda x: x)
              )
            )
            (lambda t: lambda f: t(lambda x: x))
          )
          (n)
        (
          lambda _: (
              lambda n: (
                  lambda f: lambda x: f(n(f)(x))
              )
          )
          (lambda f: lambda x: x)
        )(
          lambda _: (
            lambda n: lambda m: n(
              lambda acc: (
                lambda n: lambda m: n(
                  lambda n: lambda f: lambda x: f(n(f)(x))
                )
                (m)
              )
              (m)
              (acc)
            )
            (lambda f: lambda x: x)
          )
          (n)
          (
            myself(
              myself
            )(
              (
                lambda n:
                lambda f:
                lambda x: n(lambda g: lambda h: h(g(f)))
                (lambda u: x)
                (lambda u: u)
              )
              (n)
            )
          )
        )
      )
    )
  )((
      (
        lambda n: lambda f: lambda x: f(n(f)(x))
      )(
        (
          lambda n: lambda f: lambda x: f(n(f)(x))
        )(
          (
            lambda n: lambda f: lambda x: f(n(f)(x))
          )(
            (
              lambda n: lambda f: lambda x: f(n(f)(x))
            )(
              (
                lambda n: lambda f: lambda x: f(n(f)(x))
              )(
                (
                  lambda n: lambda f: lambda x: f(n(f)(x))
                )(
                  (lambda f: lambda x: x)
                )
              )
            )
          )
        )
      )
  ))
  # the following line just converts the lambda function to a python number
  (lambda x: x + 1)(0)
)

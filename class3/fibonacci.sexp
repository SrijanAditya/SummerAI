(brilisp
    (define ((print int) (n int)))
    
    (define ((fib int) (k int))
        (set (x int) (const 0))
        (set (y int) (const 1))

        (set (res1 bool) (eq k x))
        (br res1 zero other1)

        (label zero)
        (ret x)

        (label other1)        
        (set (res2 bool) (eq k y))
        (br res2 one other2)

        (label one)
        (ret y)

        (label other2)
        (set (b int) (const 1))
        (set (c int) (const 2))
        (set (d int) (sub k b))
        (set (e int) (sub k c))
        (set (tmp1 int) (call fib d))
        (set (tmp2 int) (call fib e))
        (set (out int) (add tmp1 tmp2))
        (ret out))
        
    (define ((main int))
        (set (f int) (const 5))
        (set (g int) (call fib f))
        (set (tmp int) (call print g))
        (ret tmp)))

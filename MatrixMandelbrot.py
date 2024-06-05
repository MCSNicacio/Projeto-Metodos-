def MatrixMandelbrot(n_i, N):

    x_in = np.linspace(-2, 2, N)
    y_in = np.linspace(-2, 2, N)
    [a, b] = np.meshgrid(x_in, y_in * 1j)
    z = a+b
    c =a+b
    div_array = np.zeros([N,N])
   
    for p in range(n_i):
        div_ind = np.abs(z) < 2
        div_array[div_ind] = div_array[div_ind]+1
        z= z**2 + c
    print(div_array)

MatrixMandelbrot(20,10)

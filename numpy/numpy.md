- # Numpy
	- ## Importing
		- `import numpy as np`
	- ## numpy.linalg
		- `from numpy.linalg import inv, qr`
		- It has a standard set of matrix decompositions and things like inverse and determinant.
		-
		  | Function | Description |
		  |---|---|
		  | `diag` | Return the diagonal (or off-diagonal) elements of a square matrix as a 1D array, or convert a 1D array into a square matrix with zeros on the off-diagonal |
		  | `dot` | Matrix multiplication |
		  | `trace` | Compute the sum of the diagonal elements |
		  | `det` | Compute the matrix determinant |
		  | `eig` | Compute the eigenvalues and eigenvectors of a square matrix |
		  | `inv` | Compute the inverse of a square matrix |
		  | `pinv` | Compute the Moore-Penrose pseudoinverse of a matrix |
		  | `qr` | Compute the QR decomposition |
		  | `svd` | Compute the singular value decomposition (SVD) |
		  | `solve` | Solve the linear system Ax = b for x, where A is a square matrix |
		  | `lstsq` | Compute the least-squares solution to Ax = b |
	- ## Array
		- ### Array Generation Functions
			- Array Generation
			  | Function | Description |
			  |---|---|
			  | `array()` | Convert input data (list, tuple, array, or other sequencetype) to an ndarray |
			  | `asarray()` | Convert input to ndarray, but do not copy if the input is already an ndarray |
			  | `arange()` | Like the built-in range but returns an ndarray instead of a list |
			  | `ones()` | produce an array of all 1s with the given shape and data type |
			  | `ones_like()` | takes another array and produces a ones array of the same shape and data type |
			  | `zeros()`, `zeros_like()` | Like ones and ones_like but producing arrays of 0s instead |
			  | `empty()`, `empty_like()` | Create new arrays by allocating new memory, but do not populate with any values |
			  | `full()` | Produce an array of the given shape and data type with all values set to the indicated "fill value" |
			  | `full_like()` | takes another array and produces a filled array of the same shape and data type |
			  | `eye`, `identity` | Create a square N × N identity matrix (1s on the diagonal and 0s elsewhere) |
				-
				  ```code
				  data = np.array([[1, 2, 3],
				                   [4, 5, 6],
				                   [7, 8, 9]])
				  ```
		- ### Aggregation, Statistical, Mathematical functions
			- Some functions take an optional axis argument that computes the statistic over the given axis.
				- `axis=1` means "compute across the columns"
				- `axis=0` means "compute  down the rows."
			- `np.sum(ndarray)`
				- print("column sums:", data.sum(axis=0))
				- print("row sums:", data.sum(axis=1))
			- `np.argmin(ndarray)` for the index of the smallest value.
			- `np.min(ndarray)`
			- `np.argmax(ndarray)` for the index of the largest value.
			- `np.max(ndarray)`
			- `np.mean(ndarray)`
			- `np.std(ndarray)` standard deviation
			- `np.var(ndarray)` for standard variance (square of deviation)
			- Accumulation functions
			- `cumsum` return an array of the same size but with the partial aggregates computed along the indicated axis according to each lower dimensional slice
				-
				  ```code
				  arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
				  
				  arr.cumsum(axis=0)
				  ```
			- `cumprod` Cumulative product of elements starting from 1
		- ### Set operations and Unique Values
			- `np.unique(ndarray)` returns a new array with unique and sorted values.
				- equivalent of doing `sorted(set(List))` in standard python.
			- Set Opts
			- `intersect1d(x, y)`Compute the sorted, common elements in x and y.
			- `union1d(x, y)`Compute the sorted union of elements
			- `in1d(x, y)`Compute a Boolean array indicating whether each element of x is contained in y
			- `setdiff1d(x, y)` Set difference, elements in x that are not in y
			- `setxor1d(x, y)` Set symmetric differences; elements that are in either of the arrays, but not
			  both  
		- ### Scalar arithmetic and comparisons
			- Numeric
			  ```code
			  arr3d = np.array([[[1,2], [3,4]],
			                    [[5,6], [7,8]],
			                    [[9,10],[11,12]]])
			                    
			  arr3d[0] = 42
			  ```
			- String
			  ```code
			  names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
			  
			  names == "Bob"
			  ```
		- ### Indexing
			- `array[start:end:steps]` for one dimension
			- `array[dim1, dim2,.......dimN]` for multiple dimension
				-
				  ```code
				  arr3d = np.array([[[1,2], [3,4]],
				                    [[5,6], [7,8]],
				                    [[9,10],[11,12]]])
				                    
				  arr3d[0:2, 1:, ::-1]
				  ```
			- To select a subset of the rows in a particular order, you can simply pass a list or ndarray of integers specifying the desired order. Using negative indices selects rows from the end.
				-
				  ```code
				  my_arr = np.array([[0., 0., 0., 0.],
				                      [1., 1., 1., 1.],
				                      [2., 2., 2., 2.],
				                      [3., 3., 3., 3.],
				                      [4., 4., 4., 4.],
				                      [5., 5., 5., 5.],
				                      [6., 6., 6., 6.],
				                      [7., 7., 7., 7.]])
				                      
				  my_arr[[4, 3, 0, 6]]
				  ```
		- ### dtype
			- `integers = np.array([1, 2, 3], dtype=np.int32)`
			- `floats = np.array([1, 2, 3], dtype=np.float64)`
	- ## Broadcasting
		- Broadcasting allows NumPy to perform arithmetic between arrays with compatible shapes without explicitly replicating the smaller array.
		- Boolean Indexing
			-
			  ```code
			  names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe", "Will"])
			  data2 = np.array([[1, 3], [2, 4], [5, 7], [6, 8], [9, 11], [10, 12], [13, 15], [14, 16]])
			  
			  data2[names == "Bob"]
			  ```
			- selecting values greater than 10
			  ```code
			  indices = data2 > 10
			  
			  data2[indices]
			  ```
	- ## Conditional Logic
		- `np.where(condition, arr1, arr2)` a vectorized version of the ternary expression x if condition else y
			-
			  ```code
			  xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
			  yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
			  cond = np.array([True, False, True, True, False])
			  
			  result = np.where(cond, xarr, yarr)
			  ```
		- The second and third arguments to numpy.where don’t need to be arrays; one or both of them can be scalars.
		-
		  ```code
		  my_arr = np.array([1, 5, 2, 9, 10, -1, 0, -2, -5])
		  np.where(my_arr > 0, 2, 0)
		  ```
	- ## File I/O
		- Reading from Binary:
		- `np.load(filename)`load data to and from disk in some text or binary formats with file extension .npy.
		- `np.save(filename, array)` arrays are saved by default in an uncompressed raw binary format with file extension .npy.
		- `numpy.savez(filename, arr1, arr2, arrN)` save multiple arrays in an uncompressed archive.
			- When loading an .npz file, you get back a dictionary-like object that loads the individual arrays lazily:
			  ```code
			  arch = np.load("array_archive.npz")
			  arch["b"]
			  ```
		- `np.savez_compressed(filename, a=arr1, b=arr2)` If your data compresses well.
		- Reading other file formats:
		- `np.loadtxt(filename)` to read files, best when the file has consistent columns and no missing values.
			- Parameters:
				* `filename`: File name or path link to the CSV file.
				* `delimiter` (optional): Delimiter to consider while creating array of values from text default is whitespace.
				* `encoding` (optional): Encoding used to decode the input file.
				* `dtype` (optional): Data type of the resulting array

			- `.loadtxt(filePath, delimiter=",")` for csv
		- `np.genfromtxt(filename)` used to handle datasets with missing values or varied data types. It's perfect for more complex CSV files that require handling.
			- Paramaters:
				* filename: File name or path to the CSV file.
				* delimiter (optional): Used consider while creating array of values from text default is any consecutive white spaces act as a delimiter.
				* missing_values (optional): Set of strings to use incase of a missing value.
				* dtype (optional): Data type of the resulting array.

	- ## Matrices
		- `T` Arrays have the transpose method and the special T attribute
			-
			  ```code
			  transposing = np.arange(16).reshape(4, 4)
			  
			  transposing, transposing.T
			  ```
		- Multiplying
			- Multiplying two two-dimensional arrays with `*` is an element-wise product, while matrix multiplications require either using the `dot` function or the `@` infix operator.
			- A matrix product between a two-dimensional array and a suitably sized one-dimensional array results in a one-dimensional array:
		- `np.dot(x, y)` or `x.dot(y)` when computing the inner matrix product
			-
			  ```code
			  transposing = np.arange(16).reshape(4, 4)
			  
			  np.dot(transposing, transposing.T)
			  ```
		- The `@` infix operator is another way to do matrix multiplication
			-
			  ```code
			  transposing = np.arange(16).reshape(4, 4)
			  transposing @ transposing.swapaxes(0,1)
			  ```
		- `swapaxes()` similarly returns a view on the data without making a copy
			-
			  ```code
			  transposing = np.arange(16).reshape(4, 4)
			  
			  transposing.swapaxes(0,1)
			  ```
	- ## Methods
		- `my_arr.ndim` to see dimensions
		- `my_arr.shape` shape gives us the shape of the array (dimensions, columns, rows)
		- `my_arr.dtype` The data type is stored in a special dtype metadata object
		- `arr.reshape()` to convert an array from one shape to another without copying any data.
			-
			  ```code
			  reshaping = np.array([1,2,3,4,5,6,7,8])
			  
			  reshaping.reshape(2,4)
			  ```
	- ## Random
		- `numpy.random`has functions for effciently generating whole arrays of sample values from many kinds of probability distributions.
		- `numpy.random.standard_normal(size)` to get a 4 × 4 array of samples from the standard normal distribution.
		- Python’s built-in random module, by contrast, samples only one value at a time
		- Functions like `numpy.random.standard_normal` use the `numpy.random` module's default random number generator, but your code can be configured to use an explicit generator
		- ### Methods
			-
			  | Method | Description |
			  |---|---|
			  | `permutation` | Return a random permutation of a sequence, or return a permuted range |
			  | `shuffle` | Randomly permute a sequence in place |
			  | `uniform` | Draw samples from a uniform distribution |
			  | `integers` | Draw random integers from a given low-to-high range |
			  | `standard_normal` | Draw samples from a normal distribution with mean 0 and standard deviation 1 |
			  | `binomial` | Draw samples from a binomial distribution |
			  | `normal` | Draw samples from a normal (Gaussian) distribution |
			  | `beta` | Draw samples from a beta distribution |
			  | `chisquare` | Draw samples from a chi-square distribution |
			  | `gamma` | Draw samples from a gamma distribution |
			  | `uniform` | Draw samples from a uniform [0, 1) distribution |
	- ## Universal Functions
		- a function that performs element-wise operations on data in ndarrays.
		- `numpy.sqrt(array)` returns the square of all elements in the array.
		- ### Unary Functions
			-
			  | Function | Description |
			  |---|---|
			  | abs, fabs | Compute the absolute value element-wise for integer, foating-point, or complex values |
			  | sqrt | Compute the square root of each element (equivalent to arr ** 0.5 ) |
			  | square | Compute the square of each element (equivalent to arr ** 2) |
			  | exp | Compute the exponent ex of each element |
			  | sign | Compute the sign of each element: 1 (positive), 0 (zero), or – 1 (negative) |
			  | ceil | Compute the ceiling of each element (i.e., the smallest integer greater than or equal to that number) |
			  | floor | Compute the floor of each element (i.e., the largest integer less than or equal to each element) |
			  | rint | Round elements to the nearest integer, preserving the dtype |
			  | modf | Return fractional and integral parts of array as separate arrays |
			  | isnan | Return Boolean array indicating whether each value is NaN (Not a Number) |
			  | isfinite, isinf | Return Boolean array indicating whether each element is finite (non- inf , non- NaN ) or infnite, respectively |
			  | logical_not | Compute truth value of not x element-wise (equivalent to~arr ) |
			-
			  | log, log10, log2, log1p | Natural logarithm (base e), log base 10, log base 2, and log(1 + x), respectively |
			  |---|---|
			  | cos, cosh, sin, sinh, tan,tanh | Regular and hyperbolic trigonometric functions |
			  | arccos, arccosh, arcsin, arcsinh, arctan, arctanh | Inverse trigonometric functions |
		- ### Binary Functions
		-
		  | Function | Description |
		  |---|---|
		  | add | Add corresponding elements in arrays |
		  | subtract | Subtract elements in second array from first array |
		  | multiply | Multiply array elements |
		  | divide, floor_divide | Divide or floor divide (truncating the remainder) |
		  | power | Raise elements in first array to powers indicated in second array |
		  | maximum, fmax | Element-wise maximum; fmax ignores NaN |
		  | minimum, fmin | Element-wise minimum; fmin ignores NaN |
		  | mod | Element-wise modulus (remainder of division) |
		  | copysign | Copy sign of values in second argument to values in first argument |
		  | greater, less, equal, not_equal | |
		  | greater_equal, less_equal | |
		  | logical_and | Compute element-wise truth value of AND ( & ) logical operation |
		  | logical_or | Compute element-wise truth value of OR logical operation |
		  | logical_xor | Compute element-wise truth value of XOR ( ^ ) logical operation |
	- ## Vectorization
		- Replacing explicit loops with array expressions is referred to by some people as vectorization.
		-
		  <p><code>numpy.meshgrid</code> function takes two <b>one-dimensional</b> arrays and produces two <b>two-dimensional</b> matrices corresponding to all pairs of (x, y) in the two arrays</p>
			- Making the grid
			  ```code
			  data = np.arange(-5, 5, 0.1)
			  
			  xs, ys = np.meshgrid(data, data)
			  xs, ys
			  ```
			- Plotting
			  ```code
			  plt.title("My first Plot") # function of matplotlip.pyplot as plt
			  plt.plot(xs, ys, "go-", label="y")
			  plt.show()
			  ```

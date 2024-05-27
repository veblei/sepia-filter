# Profiling report

## Questions

A few questions below to help understand the kind of information we can get from profiling outputs.
 We are not asking for lots of detail, just 1-2 sentences each.

### Question 1

> Which profiler produced the most useful output, and why?

The output from line-profiler was more useful visually because it was easier to understand
and it produced detailed statistics for every line of code in the functions. For cProfile it
was difficult to interpret the output, especially when compared to line-profiler.

### Question 2

> Pick one profiler output (e.g. `cprofile numpy_color2sepia`).
  Based on this profile, where should we focus effort on improving performance?

> **Hint:** two things to consider when picking an optimization:

> - how much time is spent in the step? (reducing a step that takes 1% of the time all the way to 0 can only improve performance by 1%)
> - are there other ways to do it? (simple steps may already be optimal. Complex steps often have many implementations with different performance)

selected profile: `line-profiler numpy_color2gray`

Most amount of time in this function, and most other functions, is spent on adding the new
rgb-values to the image. I don't know if there are more efficient ways to add the new values,
but if we want to improve the performance of the function, this step is where the most time
is spent and therefore where we can gain the most time aswell.

## Profile output

Paste the outputs of `python3 -m instapy.profiling` below:

<details>
<summary>cProfile output</summary>

Begin cProfile
Profiling python color2gray with cprofile:
         2764815 function calls in 7.906 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    7.648    2.549    7.906    2.635 /Users/VebjornLeihne/Studier-git/IN4110/vebjorol-repo/assignment3/instapy/python_filters.py:7(python_color2gray)
  2764800    0.258    0.000    0.258    0.000 {method 'append' of 'list' objects}
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 /Users/VebjornLeihne/opt/anaconda3/envs/IN4110/lib/python3.10/site-packages/numpy/core/multiarray.py:80(empty_like)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling numpy color2gray with cprofile:
         18 function calls in 0.016 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.016    0.005    0.016    0.005 /Users/VebjornLeihne/Studier-git/IN4110/vebjorol-repo/assignment3/instapy/numpy_filters.py:7(numpy_color2gray)
        3    0.000    0.000    0.000    0.000 {method 'astype' of 'numpy.ndarray' objects}
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 /Users/VebjornLeihne/opt/anaconda3/envs/IN4110/lib/python3.10/site-packages/numpy/core/multiarray.py:80(empty_like)


Profiling numba color2gray with cprofile:
         15 function calls in 0.018 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.018    0.006    0.018    0.006 /Users/VebjornLeihne/Studier-git/IN4110/vebjorol-repo/assignment3/instapy/numba_filters.py:6(numba_color2gray)
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 /Users/VebjornLeihne/opt/anaconda3/envs/IN4110/lib/python3.10/site-packages/numpy/core/multiarray.py:80(empty_like)


Profiling cython color2gray with cprofile:
         18 function calls (15 primitive calls) in 0.018 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      6/3    0.018    0.003    0.018    0.006 instapy/cython_filters.pyx:6(cython_color2gray)
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 /Users/VebjornLeihne/opt/anaconda3/envs/IN4110/lib/python3.10/site-packages/numpy/core/multiarray.py:80(empty_like)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Profiling python color2sepia with cprofile:
         2764815 function calls in 20.756 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3   20.489    6.830   20.756    6.919 /Users/VebjornLeihne/Studier-git/IN4110/vebjorol-repo/assignment3/instapy/python_filters.py:30(python_color2sepia)
  2764800    0.267    0.000    0.267    0.000 {method 'append' of 'list' objects}
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 /Users/VebjornLeihne/opt/anaconda3/envs/IN4110/lib/python3.10/site-packages/numpy/core/multiarray.py:80(empty_like)


Profiling numpy color2sepia with cprofile:
         18 function calls in 0.040 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        3    0.040    0.013    0.040    0.013 /Users/VebjornLeihne/Studier-git/IN4110/vebjorol-repo/assignment3/instapy/numpy_filters.py:25(numpy_color2sepia)
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.array}
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 /Users/VebjornLeihne/opt/anaconda3/envs/IN4110/lib/python3.10/site-packages/numpy/core/multiarray.py:80(empty_like)


Profiling numba color2sepia with cprofile:
         21 function calls (18 primitive calls) in 0.036 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      6/3    0.036    0.006    0.036    0.012 /Users/VebjornLeihne/Studier-git/IN4110/vebjorol-repo/assignment3/instapy/numba_filters.py:23(numba_color2sepia)
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 /Users/VebjornLeihne/opt/anaconda3/envs/IN4110/lib/python3.10/site-packages/numba/core/serialize.py:29(_numba_unpickle)
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 /Users/VebjornLeihne/opt/anaconda3/envs/IN4110/lib/python3.10/site-packages/numpy/core/multiarray.py:80(empty_like)


Profiling cython color2sepia with cprofile:
         18 function calls (15 primitive calls) in 0.041 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
      6/3    0.041    0.007    0.041    0.014 instapy/cython_filters.pyx:23(cython_color2sepia)
        3    0.000    0.000    0.000    0.000 <__array_function__ internals>:177(empty_like)
        3    0.000    0.000    0.000    0.000 {built-in method numpy.core._multiarray_umath.implement_array_function}
        3    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        3    0.000    0.000    0.000    0.000 /Users/VebjornLeihne/opt/anaconda3/envs/IN4110/lib/python3.10/site-packages/numpy/core/multiarray.py:80(empty_like)


End cProfile

</details>

<details>
<summary>line_profiler output</summary>

Begin line_profiler
Profiling python color2gray with line_profiler:
Timer unit: 1e-06 s

Total time: 14.298 s
File: /Users/VebjornLeihne/Studier-git/IN4110/vebjorol-repo/assignment3/instapy/python_filters.py
Function: python_color2gray at line 7

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     7                                           def python_color2gray(image: np.array) -> np.array:
     8                                               """Convert rgb pixel array to grayscale
     9                                           
    10                                               Args:
    11                                                   image (np.array)
    12                                               Returns:
    13                                                   np.array: gray_image
    14                                               """
    15         3         68.0     22.7      0.0      gray_image = np.empty_like(image)
    16                                               # iterate through the pixels, and apply the grayscale transform
    17         3          4.0      1.3      0.0      i = 0
    18      1443       1403.0      1.0      0.0      for nd in image:
    19      1440        867.0      0.6      0.0          j = 0
    20    923040     691244.0      0.7      4.8          for row in nd:
    21    921600     603404.0      0.7      4.2              rgb = []
    22   3686400    3144828.0      0.9     22.0              for item in row:
    23   2764800    2069343.0      0.7     14.5                  rgb.append(item)
    24    921600    7068812.0      7.7     49.4              gray_image[i,j] = (rgb[0]*0.21 + rgb[1]*0.72 + rgb[2]*0.07)
    25    921600     716907.0      0.8      5.0              j += 1
    26      1440       1099.0      0.8      0.0          i += 1
    27         3          3.0      1.0      0.0      return gray_image

Profiling numpy color2gray with line_profiler:
Timer unit: 1e-06 s

Total time: 0.018786 s
File: /Users/VebjornLeihne/Studier-git/IN4110/vebjorol-repo/assignment3/instapy/numpy_filters.py
Function: numpy_color2gray at line 7

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     7                                           def numpy_color2gray(image: np.array) -> np.array:
     8                                               """Convert rgb pixel array to grayscale
     9                                           
    10                                               Args:
    11                                                   image (np.array)
    12                                               Returns:
    13                                                   np.array: gray_image
    14                                               """
    15         3         37.0     12.3      0.2      gray_image = np.empty_like(image)
    16                                               # Hint: use numpy slicing in order to have fast vectorized code
    17         3       1827.0    609.0      9.7      r, g, b = image[:,:,[0]], image[:,:,[1]], image[:,:,[2]]
    18         3      16287.0   5429.0     86.7      gray_image[:,:] = (r*0.21 + g*0.72 + b*0.07)
    19                                               # Return image (make sure it's the right type!)
    20         3        630.0    210.0      3.4      gray_image = gray_image.astype("uint8")
    21         3          5.0      1.7      0.0      return gray_image

Profiling numba color2gray with line_profiler:
Timer unit: 1e-06 s

Total time: 0 s
File: /Users/VebjornLeihne/Studier-git/IN4110/vebjorol-repo/assignment3/instapy/numba_filters.py
Function: numba_color2gray at line 6

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           @jit(forceobj=True)
     7                                           def numba_color2gray(image: np.array) -> np.array:
     8                                               """Convert rgb pixel array to grayscale
     9                                           
    10                                               Args:
    11                                                   image (np.array)
    12                                               Returns:
    13                                                   np.array: gray_image
    14                                               """
    15                                               gray_image = np.empty_like(image)
    16                                               # iterate through the pixels, and apply the grayscale transform
    17                                               r, g, b = image[:,:,[0]], image[:,:,[1]], image[:,:,[2]]
    18                                               gray_image[:,:] = (r*0.21 + g*0.72 + b*0.07)
    19                                               gray_image = gray_image.astype("uint8")
    20                                               return gray_image

Profiling cython color2gray with line_profiler:
Timer unit: 1e-06 s

Total time: 0.020334 s
File: instapy/cython_filters.pyx
Function: cython_color2gray at line 6

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     6                                           cpdef cython_color2gray(image):

Profiling python color2sepia with line_profiler:
Timer unit: 1e-06 s

Total time: 44.9656 s
File: /Users/VebjornLeihne/Studier-git/IN4110/vebjorol-repo/assignment3/instapy/python_filters.py
Function: python_color2sepia at line 30

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    30                                           def python_color2sepia(image: np.array) -> np.array:
    31                                               """Convert rgb pixel array to sepia
    32                                           
    33                                               Args:
    34                                                   image (np.array)
    35                                               Returns:
    36                                                   np.array: sepia_image
    37                                               """
    38         3         39.0     13.0      0.0      sepia_image = np.empty_like(image)
    39                                               # Iterate through the pixels
    40                                               # applying the sepia matrix
    41         3          4.0      1.3      0.0      sepia_matrix = [
    42         3          4.0      1.3      0.0          [0.393, 0.769, 0.189],
    43         3          3.0      1.0      0.0          [0.349, 0.686, 0.168],
    44         3          3.0      1.0      0.0          [0.272, 0.534, 0.131]
    45                                               ]
    46         3          3.0      1.0      0.0      i = 0
    47      1443       2158.0      1.5      0.0      for nd in image:
    48      1440       1440.0      1.0      0.0          j = 0
    49    923040    1120988.0      1.2      2.5          for row in nd:
    50    921600     995162.0      1.1      2.2              rgb = []
    51   3686400    4853495.0      1.3     10.8              for item in row:
    52   2764800    3317302.0      1.2      7.4                  rgb.append(item)
    53   3686400    4219635.0      1.1      9.4              for h in range(3):
    54   2764800   21728187.0      7.9     48.3                  val =  (rgb[0]*sepia_matrix[h][0] + rgb[1]*sepia_matrix[h][1] + rgb[2]*sepia_matrix[h][2])
    55   2764800    3204989.0      1.2      7.1                  if val > 255:
    56    135222     172257.0      1.3      0.4                      val = 255
    57   2764800    4284493.0      1.5      9.5                  sepia_image[i,j,h] = val
    58    921600    1063663.0      1.2      2.4              j += 1
    59      1440       1729.0      1.2      0.0          i += 1
    60                                               # Return image
    61                                               # don't forget to make sure it's the right type!
    62         3          3.0      1.0      0.0      return sepia_image

Profiling numpy color2sepia with line_profiler:
Timer unit: 1e-06 s

Total time: 0.040305 s
File: /Users/VebjornLeihne/Studier-git/IN4110/vebjorol-repo/assignment3/instapy/numpy_filters.py
Function: numpy_color2sepia at line 25

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    25                                           def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    26                                               """Convert rgb pixel array to sepia
    27                                           
    28                                               Args:
    29                                                   image (np.array)
    30                                                   k (float): amount of sepia filter to apply (optional)
    31                                           
    32                                               The amount of sepia is given as a fraction, k=0 yields no sepia while
    33                                               k=1 yields full sepia.
    34                                           
    35                                               (note: implementing 'k' is a bonus task,
    36                                               you may ignore it for Task 9)
    37                                           
    38                                               Returns:
    39                                                   np.array: sepia_image
    40                                               """
    41         3         11.0      3.7      0.0      if not 0 <= k <= 1:
    42                                                   # validate k (optional)
    43                                                   raise ValueError(f"k must be between [0-1], got {k=}")
    44                                           
    45         3         43.0     14.3      0.1      sepia_image = np.empty_like(image)
    46                                           
    47                                               # define sepia matrix (optional: with `k` tuning parameter for bonus task 13)
    48         6         36.0      6.0      0.1      sepia_matrix = np.array([
    49         3          4.0      1.3      0.0          [0.393, 0.769, 0.189],
    50         3          3.0      1.0      0.0          [0.349, 0.686, 0.168],
    51         3          3.0      1.0      0.0          [0.272, 0.534, 0.131]
    52                                               ])
    53                                           
    54                                               # HINT: For version without adaptive sepia filter, use the same matrix as in the pure python implementation
    55                                               # use Einstein sum to apply pixel transform matrix
    56                                               # Apply the matrix filter
    57         3         22.0      7.3      0.1      r, g, b = image[:,:,0], image[:,:,1], image[:,:,2]
    58        12         36.0      3.0      0.1      for i in range(3):
    59         9      31050.0   3450.0     77.0          val = (r*sepia_matrix[i,0] + g*sepia_matrix[i,1] + b*sepia_matrix[i,2])
    60         9       6358.0    706.4     15.8          val[val > 255] = 255
    61         9       2735.0    303.9      6.8          sepia_image[:,:,i] = val
    62                                           
    63                                               # Check which entries have a value greater than 255 and set it to 255 since we can not display values bigger than 255
    64                                               # Return image (make sure it's the right type!)
    65         3          4.0      1.3      0.0      return sepia_image

Profiling numba color2sepia with line_profiler:
Timer unit: 1e-06 s

Total time: 0 s
File: /Users/VebjornLeihne/Studier-git/IN4110/vebjorol-repo/assignment3/instapy/numba_filters.py
Function: numba_color2sepia at line 23

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    23                                           @jit(forceobj=True)
    24                                           def numba_color2sepia(image: np.array) -> np.array:
    25                                               """Convert rgb pixel array to sepia
    26                                           
    27                                               Args:
    28                                                   image (np.array)
    29                                               Returns:
    30                                                   np.array: sepia_image
    31                                               """
    32                                               sepia_image = np.empty_like(image)
    33                                               # Iterate through the pixels
    34                                               # applying the sepia matrix
    35                                           
    36                                               sepia_matrix = np.array([
    37                                                   [0.393, 0.769, 0.189],
    38                                                   [0.349, 0.686, 0.168],
    39                                                   [0.272, 0.534, 0.131]
    40                                               ])
    41                                           
    42                                               r, g, b = image[:,:,0], image[:,:,1], image[:,:,2]
    43                                               for i in range(3):
    44                                                   val = (r*sepia_matrix[i,0] + g*sepia_matrix[i,1] + b*sepia_matrix[i,2])
    45                                                   val[val > 255] = 255
    46                                                   sepia_image[:,:,i] = val
    47                                           
    48                                               # Return image
    49                                               # don't forget to make sure it's the right type!
    50                                               return sepia_image

Profiling cython color2sepia with line_profiler:
Timer unit: 1e-06 s

Total time: 0.041722 s
File: instapy/cython_filters.pyx
Function: cython_color2sepia at line 23

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    23                                           cpdef cython_color2sepia(image):

End line_profiler

</details>

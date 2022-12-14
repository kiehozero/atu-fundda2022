# Assessment: Fundamentals of Data Analysis, Autumn 2022

This repository serves as my assessment for the Fundamentals of Data Analysis module, a constituent module of the Higher Diploma in Data Analytics at the Atlantic Technological University, Ireland. As part of the course, we were given tasks each week with a single deadline at the end of term; all of the notebooks associated with these tasks are tores in the [Practicals](practicals) sub-folder.

I have stored any notebooks or PDF files that we received as part of the course in the [Materials](materials) section of this repository, just so I had this information to hand while I was working through it, and also so that I could easily reference any of the lecturer's remarks. Some of these are heavily annotated by myself, while others are less so; in any case, these are equivalent to any margin scribbles I would have done in a book-based module.

When I was completing exercises, I would mark incomplete files with an INC suffix to remind myself of the amount of work outstanding. I then renamed them once I was finished with an exercise; the obvious effect this has is that the completed files will have very few commits on them as they are new submissions to GitHub. If you go through the history of the repo as a whole, you will see these files appear through the submission history. This is probably a way of marking completed and in-progress files that I won't be using going forward!

Special thanks to my friend Richard Bilsborough who has studied undergraduate economics and answered a ton of my questions on entropy and logarithms. He provided the NIST article that is referenced in the second exercise.

## Using Jupyter Notebooks

All of the exercises are completed using [Jupyter Notebook](https://jupyter.org/), a free package that comes pre-installed with Anaconda. Launched from Anaconda Navigator or using the _jupyter notebook_ command in your preferred CLI, Notebook is a browser-based tool that allows for quick setup and easy annotation of code with text and images outside of the code itself. This allows for more thorough explanations than traditional IDEs offer.

***

## Exercises

### **Ex. 1 - Information**

**Task**: Adapt the code in Ian's initial tutorials to generate a 1000 character-long string with weights based on the previous two characters.

**Comments**: I couldn't get this to work as I expected, so I have included my workings knowing that it doesn't currently function correctly.

**References**:

W3Schools (2022) "Python - Nested Dictionaries". Available at [W3Schools](https://www.w3schools.com/python/python_dictionaries_nested.asp) (Accessed 28th December, 2022).
\
W3Schools (2022) "Python - Slice Strings". Available at [W3Schools](https://www.w3schools.com/python/gloss_python_string_slice.asp) (Accessed 28th December, 2022).

### **Ex. 2 - Logarithms**

**Task**: Explain why the log of zero is undefined.

**References**:

Aziz, Khalil Ahmed (2020) "Learn How to Write Markdown and LaTeX in The Jupyter Notebook". Available at [Towards Data Science (Medium)](https://towardsdatascience.com/write-markdown-latex-in-the-jupyter-notebook-10985edb91fd) (Accessed 26th November, 2022).
\
Fast and Easy Maths (2022) "Why we cannot find log 0?". Available at [YouTube](https://www.vedantu.com/maths/value-of-log-0) (Accessed 26th November, 2022).
\
Kelly, Steve (2012) "Logarithms, Explained". Available at [TED-Ed on Youtube](https://www.youtube.com/watch?v=zzu2POfYv0Y) (Accessed 26th November, 2022).
\
National Institute of Standards and Technology (2017) "A Tutorial introduction to the ideas behind Normalized cross-entropy and the information-theoretic idea of Entropy". Available at [NIST](https://www.nist.gov/system/files/documents/2017/11/30/nce.pdf) (Accessed 26th November, 2022).
\
Pierce, R. (2022) "_e_ (Euler's Number)". Available at [MathsIsFun](https://www.mathsisfun.com/numbers/e-eulers-number.html) (Accessed 2nd January, 2023).
\git add
RapidTables (2022) "Logarithm of Zero". Available at [RapidTables](https://www.rapidtables.com/math/algebra/logarithm/Logarithm_of_0.html) (Accessed 26th November, 2022).
\
StackExchange (2012) "Why are logarithms not defined for 0 or negatives?". Available at [StackExchange Mathematics](https://math.stackexchange.com/questions/116622/why-are-logarithms-not-defined-for-0-and-negatives) (Accessed 26th November, 2022).
\
Vedantu (2022) "Log of Zero". Available at [Vedantu](https://www.vedantu.com/maths/value-of-log-0) (Accessed 26th November, 2022).
\
W3Schools (2022) "Python math.log() Method". Available at [W3Schools](https://www.w3schools.com/python/ref_math_log.asp) (Accessed 26th November, 2022).
\
Wikipedia (2022, last edit) "Logarithm: Graph of the Logarithm Function". Available at [Wikipedia](https://en.wikipedia.org/wiki/Logarithm#Graph_of_the_logarithm_function) (Accessed 26th November, 2022).

### Ex. 3a - Combinations**

**Task**: It is somewhat interesting that (5x4x3x2x1) perfectly divides (10x9x8x7x6), there is no remainder. If we only wanted exactly four heads as opposed to five, the equivalent calculation would be (10x9x8x7)/(4x3x2x1). Does that evenly divide too? What is the formula in general? Does it always come out as a positive whole number?

**References**:

CueMath (2022) "n Choose k Formula". Available at [CueMath](https://www.cuemath.com/n-choose-k-formula/) (Accessed 15th November, 2022).
\
GeeksForGeeks (2022) "Python - math.comb() method". Available at [GeeksForGeeks](https://www.geeksforgeeks.org/python-math-comb-method/) (Accessed 15th November, 2022).
\
Gregersen, E. (2016) "Factorial". Available at [Encyclop??dia Britannica](https://www.britannica.com/science/factorial) (Accessed 21st December, 2022).
\
Math Documentation (2022) "math - Mathematical Functions: Number-theoretic and representation functions". Available at [Python.org](https://docs.python.org/3/library/math.html#number-theoretic-and-representation-functions) (Accessed 20th December, 2022).
\
Ratemi, W.M. (2015) "The Mathematical Secrets of Pascal's Triangle". Available at [YouTube](https://www.youtube.com/watch?v=XMriWTvPXHI) (Accessed 20th December, 2022).
\
Story of Mathematics (2022) "Combinations - Explanation and Examples". Available at [SOM](https://www.storyofmathematics.com/combinations/) (Accessed 15th November, 2022).
\
Thamrongpairoj, K.S. (2019) "What is _n_ choose _k_? formula, examples, Pascal's triangles". Available at [YouTube](https://www.youtube.com/watch?v=dvLMIfHleM8) (Accessed 26th November, 2022).
\
W3Schools (2022) "Python math.log() Method". Available at [W3Schools](https://www.w3schools.com/python/ref_math_log.asp) (Accessed 26th November, 2022).
\
Wikipedia (2022, last edit) "Binomial Coefficient". Available at [Wikipedia](https://en.wikipedia.org/wiki/Binomial_coefficient) (Accessed 26th November, 2022).

### **Ex. 3b - Pascal's Triangle**

**Task**: Note that there are the same number of way to get 4 tails as there are to get 4 heads. Explain why this is.

**References**:

CueMath (2022) "Pascal's Triangle". Available at [CueMath](https://www.cuemath.com/algebra/pascals-triangle/) (Accessed 20th December, 2022).
\
Ratemi, W.M. (2015) "The Mathematical Secrets of Pascal's Triangle". Available at [YouTube](https://www.youtube.com/watch?v=XMriWTvPXHI) (Accessed 20th December, 2022).
\
W3Schools (2022) "Python math.log() Method". Available at [W3Schools](https://www.w3schools.com/python/ref_math_log.asp) (Accessed 26th November, 2022).

### **Ex. 4 - Distributions**

**Task**: Plot bar charts of histograms of any three different distributions listed at this [link](https://numpy.org/doc/stable/reference/random/generator.html#distributions).

**References**:

Bobbitt, Z. (2020) "An Introduction to the Multinomial Distribution". Available at [Statology.org](https://www.statology.org/multinomial-distribution/) (Accessed 9th November, 2022).
\
Bobbitt, Z. (2021) "An Introduction to the Triangular Distribution". Available at [Statology.org](https://www.statology.org/triangular-distribution/) (Accessed 8th November, 2022).
\
Frost, J. (2017) "Degrees of Freedom in Statistics". Available at [Statistics by Jim](https://statisticsbyjim.com/hypothesis-testing/degrees-freedom-statistics/) (Accessed 15th November, 2022).
\
MatPlotLib Documentation (2022) "matplotlib.pyplot.subplot". Available at [MatPlotLib.org](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html) (Accessed 15th November, 2022).
\
NumPy Documentation (2022) "numpy.random.Generator.chisquare". Available at [NumPy.org](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.chisquare.html) (Accessed 15th November, 2022).
\
NumPy Documentation (2022) "numpy.random.Generator.multinomial". Available at [NumPy.org](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.multinomial.html) (Accessed 9th November, 2022).
\
NumPy Documentation (2022) "numpy.random.Generator.triangular". Available at [NumPy.org](https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.triangular.html) (Accessed 3rd November, 2022).
\
Russano, E. (2022) "Multinoulli and Multinomial Distributions with Examples in Python". Available at [euanrussano.com](https://www.euanrussano.com/post/probability/multinoulli_multinomial/) (Accessed 9th November, 2022).
\
Spardha (2021) "Your Guide to Discrete Probability Distributions and Their Applications in R". Available at [Analytics Vidhya (Medium)](https://medium.com/analytics-vidhya/7-types-of-discrete-probability-distributions-and-their-applications-in-r-ba5e2e263bd5) (Accessed 3rd November, 2022).
\
Turney, S. (2022) "Chi-Square (????) Distributions | Definition & Examples". Available at [Scribbr](https://www.scribbr.com/statistics/chi-square-distributions/) (Accessed 15th November, 2022).
\
Wikipedia (2022, last edit) "Chi-Squared Distribution". Available at [Wikipedia](https://en.wikipedia.org/wiki/Chi-squared_distribution) (Accessed 15th November, 2022).
\
Wikipedia (2022, last edit) "Degrees of Freedom (Statistics)". Available at [Wikipedia](https://simple.wikipedia.org/wiki/Degrees_of_freedom_(statistics)) (Accessed 15th November, 2022).
\
Wikipedia (2022, last edit) "Triangular Distribution". Available at [Wikipedia](https://en.wikipedia.org/wiki/Triangular_distribution) (Accessed 9th November, 2022).
\
Zangre, A. (2019) "Discrete vs. Continuous Data - What's the Difference?", [G2.com](https://www.g2.com/articles/discrete-vs-continuous-data) (Accessed 3rd November, 2022).

### **Ex. 5a - Cognitive Bias**

**Task**: Give three real-world examples of different types of cognitive bias.

**References**:

Deleniv, S., Ariely, D. and Peters, K. (2021) "Natural is Better: How the Appeal to Nature Fallacy Derails Public Health". Available online at [Behavioural Scientist](https://behavioralscientist.org/natural-is-better-how-the-naturalistic-fallacy-derails-public-health/) (Accessed 3rd November, 2022).
\
Ellenberg, J. (2016) _How Not To Be Wrong: The Power of Mathematical Thinking_. Excerpt available online at the Penguin Press [Medium account](https://medium.com/@penguinpress/an-excerpt-from-how-not-to-be-wrong-by-jordan-ellenberg-664e708cfc3d) (Accessed 3rd November, 2022).
\
RT??.ie (2018) "Winning Streak". Available at [Raidi?? Teilif??s ??ireann](https://www.rte.ie/tv/programmes/932584-winning-streak/) (Accessed 3rd November, 2022).
\
Wikipedia (2022, last edit). "Survivorship Bias". Available at [Wikipedia](https://en.wikipedia.org/wiki/Survivorship_bias) (Accessed 3rd November, 2022).

### **Ex. 5b - Bessel's Correction**

**Task**: Show that the difference between the standard deviation calculations is greatest for small sample sizes.

**References**:

Hall, B. (2020) "The Reasoning Behind Bessel's Correction". Available at [Towards Data Science (Medium)](https://towardsdatascience.com/the-reasoning-behind-bessels-correction-n-1-eeea25ec9bc9) (Accessed 11th December, 2022).
\
Hello Leo (2021) "Normal Distribution - Why divide by (n-1)?". Available at [YouTube](https://www.youtube.com/watch?v=YkXSjFY2mHM) (Accessed 11th December, 2022).
\
Khan Academy (2012) "Review and Intuition: Why we divide by n-1 for the unbiased sample". Available at [YouTube](https://www.youtube.com/watch?v=KkaU2ur3Ymw) (Accessed 14th November, 2022).
\
GeeksForGeeks (2018) "numpy.mean() in Python". Available at [GeeksForGeeks](https://www.geeksforgeeks.org/numpy-mean-in-python/) (Accessed 10th December, 2022).

### **Ex. 6a - Morley's Box Plots**

**Task**: Create box plots on a single set of axes for all five experiments in the Morley data set.

**References**:

GeeksForGeeks (2022) "Split Pandas Dataframe by Column Value". Available at [GeeksForGeeks](https://www.geeksforgeeks.org/split-pandas-dataframe-by-column-value/) (Accessed 16th December, 2022).
\
StackOverflow (2012) "Using a loop in Python to name variables". Available at [StackOverflow](https://stackoverflow.com/questions/13603215/using-a-loop-in-python-to-name-variables) (Accessed 17th December, 2022).

### **Ex. 6b - Fisher's Iris Box Plots**

**Task**: Create box plots for all of the numerical variables in Fisher's Iris data set.

**References**:

GeeksForGeeks (2022) "Box Plot in Python using Matplotlib". Available at [GeeksForGeeks](https://www.geeksforgeeks.org/box-plot-in-python-using-matplotlib/) (Accessed 17th December, 2022).

### **Ex. 6c - Proportionality**

**Task**: Adapt the above code and plots so that the overall plot is inversely propertional and the individual groups are directly proportional.

**References**:

BBC Bitesize (2022) "Direct and Inverse Proportion". Available at [BBC Bitesize](https://www.bbc.co.uk/bitesize/guides/zqd6srd/revision/3) (Accessed 16th December, 2022).
\
NumPy Documentation (2020) "numpy.ndarray.flatten() function". Available at [NumPy.org](https://www.geeksforgeeks.org/numpy-ndarray-flatten-function-python/) (Accessed 22nd December, 2022).
\
CueMath (2022) "Direct Proportion". Available at [CueMath](https://www.cuemath.com/commercial-math/direct-proportion/) (Accessed 16th December, 2022).

### **Ex. 7a - Replacing Characters Using Regular Expressions**

**Task**: Write a Python function to remove all non-alphanumeric characters from a string.

**References**:

W3Schools (2022) "Python RegEx". Available at [W3Schools](https://www.w3schools.com/python/python_regex.asp#sub) (Accessed 18th December, 2022).
\
Wikipedia (2022, last edit) "F??? A??? ???". Available at [Wikipedia](https://en.wikipedia.org/wiki/F%E2%99%AF_A%E2%99%AF_%E2%88%9E) (Accessed 18th December, 2022).

### **Ex. 7b - Editing Datasets Using Regular Expressions**

**Task**: Adapt the above code to capitalise the first letter of the iris species, using regular expressions.

**References**:

GeeksForGeeks (2022) "Python String Title Method". Available at [GeeksForGeeks](https://www.geeksforgeeks.org/title-in-python/) (Accessed 20th December, 2022).
\
StackOverflow (2009) "Given a URL to a text file, what is the simplest way to read the contents of the text file?" Available at [StackOverflow](https://stackoverflow.com/a/1393367) (Accessed 19th December, 2022).
\
StackOverflow (2017) "Split a string by the position of the character". Available at [StackOverflow](https://stackoverflow.com/questions/46766530/python-split-a-string-by-the-position-of-a-character) (Accessed 20th December, 2022).
\
W3Schools (2022) "Python RegEx: The search() function". Available at [W3Schools](https://www.w3schools.com/python/python_regex.asp) (Accessed 20th December, 2022).

***

## Normal Distribution

**Task**: Create a notebook about the normal distribution. Define and explain the main concepts. Pitch the notebook at your classmates. Use visuals like plots to explain concepts.

**Bugs and Oddities**:
\
1 - I was trying to plot lots of subplots on a single graph in explaining the shape of different distributions. In doing so I utterly ruined the view for a while, but luckily the link below to their documentation provided a quick reset.
\
2 - I attempted to recreate the code used to create the normal distribution PDFs on Wikipedia. I didn't want to take the exact code, but rather amend the condensed version Ian provided in an earlier notebook. It took me way too long to realise that the make_gauss function the original user created divided everything by 1. I'd earlier gone down a rabbit hole of trying to strategically place sqrt() functions from NumPy inside the density function, rather than in the list, of course with no success.
\
3 - In the course of writing an explanation for the density function and in plotting an equivalent of the Wikipedia PDF plots, I noticed a difference in the LaTeX equation used there, and in what was provided in the course material. With some quick testing I realised that they produced the same results, so I have indicated where I have sourced the density calculation from each time it occurs. The exact commit where I tested these and removed them from the code is [here](https://github.com/kiehozero/atu-fundda2022/commit/c1e9d430c07479705157b2786a083f518c8aa4c1).

**References**:

Ace Tutors (2021) "Normal Distribution Explained with Examples". Available at [YouTube](https://www.youtube.com/watch?v=xI9ZHGOSaCg) (Accessed 31st December, 2022).
\
Andersson, E. (2022) "Digits of Pi". Available at [Eve Andersson](http://www.eveandersson.com/pi/digits/) (Accessed 2nd January, 2023).
\
Anonymous (1998) "Normal Distribution". Available at [Encyclop??dia Britannica](https://www.britannica.com/topic/normal-distribution) (Accessed 20th December, 2022).
\
Bhandari, P. (2020) "Normal Distribution: Examples, Formulas and Uses". Available at [Scribbr](https://www.scribbr.com/statistics/normal-distribution/) (Accessed 27th November, 2022).
\
Chen, J. (2022) "Normal Distribution: What It Is, Properties, Uses and Formula". Available at [Investopedia](https://www.investopedia.com/terms/n/normaldistribution.asp) (Accessed 15th November, 2022).
\
GeeksforGeeks (2020) "numpy.random.standard_t() in Python". Available at [GeeksForGeeks](https://www.geeksforgeeks.org/numpy-random-standard_t-in-python/) (Accessed 1st January, 2023).
\
Frost, J. (2018) "Normal Distribution in Statistics". Available at [Statistics by Jim](https://statisticsbyjim.com/basics/normal-distribution/) (Accessed 21st December, 2022).
\
Matplotlib Documentation (2022) "matplot.pyplot.rcdefaults()". Available at [Matplotlib](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.rcdefaults.html) (Accessed 1st January, 2023).
\
National Institute of Standards and Technology (2003) "Section 1.3.6.6.1 Normal Distribution". Available at [NIST/SEMATECH Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/eda/section3/eda3661.htm) (Accessed 23rd December, 2022).
\
NumPy Documentation (2022) "Constants". Available at [NumPy](https://numpy.org/doc/stable/reference/constants.html) (Accessed 2nd January, 2023).
\
NumPy Documentation (2022) "numpy.linspace". Available at [NumPy](https://numpy.org/doc/stable/reference/generated/numpy.exp.html) (Accessed 2nd January, 2023).
\
NumPy Documentation (2022) "numpy.exp". Available at [NumPy](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) (Accessed 2nd January, 2023).
\
NumPy Documentation (2022) "numpy.random.normal". Available at [NumPy](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html) (Accessed 15th November, 2022).
\
NumPy Documentation (2022) "numpy.random.logistic". Available at [NumPy](https://numpy.org/doc/stable/reference/random/generated/numpy.random.logistic.html) (Accessed 1st January, 2023).
\
NumPy Documentation (2022) "numpy.random.standard_cauchy". Available at [NumPy](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_cauchy.html) (Accessed 1st January, 2023).
\
NumPy Documentation (2022) "numpy.random.standard_t". Available at [NumPy](https://numpy.org/doc/stable/reference/random/generated/numpy.random.standard_t.html) (Accessed 1st January, 2023).
\
NumPy Documentation (2022) "numpy.random.uniform". Available at [NumPy](https://numpy.org/doc/stable/reference/random/generated/numpy.random.uniform.html) (Accessed 3rd January, 2023).
\
SciPy Documentation (2002) "scipy.stats.norm". Available at [SciPy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html) (Accessed 22nd December, 2022).
\
Starmer, J. (2017) "The Normal Distribution, Clearly Explained". Available at [StatQuest (YouTube)](https://www.youtube.com/watch?v=rzFX5NWojp0) (Accessed 20th December, 2022).
\
Starmer, J. (2018) "The Central Limit Theorem, Clearly Explained". Available at [StatQuest (YouTube)](https://www.youtube.com/watch?v=YAlJCEDH2uY) (Accessed 28th December, 2022).
\
Weisstein, E.W. (2020) "Normal Distribution." Available at [Wolfram MathWorld](https://mathworld.wolfram.com/NormalDistribution.html) (Accessed 22nd December, 2022).
\
Wikipedia (2022, last edit) "Cauchy Distribution". Available at [Wikipedia](https://en.wikipedia.org/wiki/Cauchy_distribution) (Accessed 1st January, 2023).
\
Wikipedia (2022, last edit) "Logistic Distribution". Available at [Wikipedia](https://en.wikipedia.org/wiki/Logistic_distribution) (Accessed 1st January, 2023).
\
Wikipedia (2022, last edit) "Normal Distribution". Available at [Wikipedia](https://en.wikipedia.org/wiki/Normal_distribution) (Accessed 15th November, 2022).
\
Wikipedia (2016) "A selection of Normal Distribution Probability Distribution Functions". Available at [Wikipedia](https://commons.wikimedia.org/wiki/File:Normal_Distribution_PDF.svg) (Accessed 31st December, 2022).
\
Wikipedia (2022, last edit) "Student's _t_ Distribution". Available at [Wikipedia](https://en.wikipedia.org/wiki/https://en.wikipedia.org/wiki/Student%27s_t-distribution) (Accessed 1st January, 2023).

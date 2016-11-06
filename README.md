## Southern Arkansas University / MCIS6273 / Data Mining / Fall 2016

## This Course

Over the semester we will explore the many facets of data mining, from data munging (aka data preparation) to classification and regression.  The goal of this repository is to provide a place for the critical materials, code and notes for the course.

| Book | Description | Location |
|------|-------------|----------|
| Zaki, Mohammed J., and Wagner Meira Jr. Data mining and analysis: fundamental concepts and algorithms. Cambridge University Press, 2014. ISBN-13: 978-0521766333 | | |
| Han, Jiawei, Jian Pei, and Micheline Kamber. Data mining: concepts and techniques. Elsevier, 2011. ISBN-13: 2901558604895 | | |
| Segaran, Toby. Programming collective intelligence: building smart web 2.0 applications. O'Reilly Inc., 2007. ISBN-13: 978-0596529321 | | |
| Conway, Drew, and John White. Machine learning for hackers. " O'Reilly Media, Inc.", 2012. ISBN: 1449303714 | | |
| Grus, Joel. Data Science from Scratch: First Principles with Python. " O'Reilly Media, Inc.", 2015. ISBN: 9781491901427 | | |
| Downey, Allen. Think Python. " O'Reilly Media, Inc.", 2012. ISBN-13: 978-1449330729 | | |
| McKinney, Wes. Python for data analysis: Data wrangling with Pandas, NumPy, and IPython. " O'Reilly Media, Inc.", 2012. ISBN-13: 9781449319793 | | |
| Russell, Matthew A. Mining the Social Web: Data Mining Facebook, Twitter, LinkedIn, Google+, GitHub, and More. " O'Reilly Media, Inc.", 2013. ISBN-13: 978-1461427186 | | |




# Data Mining
Data mining is fundamentally the process of extracting something _useful_ from one or more data sets that is otherwise _a prior_ not fully understood.  The _useful_ part of data mining can often be attributed to asking good questions at the beginning &ndash; randomly exploring data can  yield very little, and  can further produce results that are senseless at worst and misleading at best.  We will take the approach that there is indeed something _interesting_ about the data, and that there are some _hypotheses_ that can be explored through that data - hopefully methodically, but at the very least guided and not entirely random.


--> make a diagram

## Begin with the Data

## Ask some questions, explore a hypothesis

## Begin an inquiry

## Explore, Visualize, Analyze

## Rinse, interpret, repeat

the data -> the question/hypthesis -> the technique


## Python
Most of the examples in this course will be in Python.  Why Python?  There are many opinions you can read all over the web about what makes Python great (or not), but here are my reasons for choosing Python for this course:

1. **Python is a very accessible language.**  Skilled programmers will have little trouble picking up Python very quickly and new programmers will not be scared out of their wits of it upon first sight.
2. **There are multiple entry points to Python.**  Following on the point above, if all you want to do is use Python for scripting, you can have your first script done in a few minutes.  If, instead, you want to develop an object-oriented, enterprise grade web application, the language has many tools for achieving that.  If instead, you want to do something in between ... say like in this course, you are free to do that too, without much hassle.
3. **The community is friendly.** You can [check this out]() and determine for yourself whether you think this is so.
4. **Tool support for data mining and data science in general are excellent.** From [Pandas]() to [SciPy]() and [matplotlib]() you'll have most, if not all of what you need to acquire, analyze and visualize your data with high quality, well-documented libraries. There are many communities contributing great tools to the data mining/data science stack in Python ...
5. **


| Resource | Notes |
|----------|-------|
|[Think Python](http://www.greenteapress.com/thinkpython/thinkpython.html) (Allen B. Downey, 2012) | A very nice open [as in free](https://github.com/AllenDowney/ThinkPython) introductory text to the Python language. |
| | |


## Other tools ...


# Data, and **Open Data**
There are an unknown number of great data sources out there in the _dataverse_, from the one's inside companies you have (or will) work on to the plethora of open data sources from around the web.  We're going to tap in to an insignificant number of such data sources (fewer than half a dozen)

## TOPICS COVERED


### CLUSTERING

|  | TOPICS | READINGS | EXPLORATIONS |  |
|:------------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------:|-------------|---|
| CLUSTERING 1 | Introduction to cluster analysis and motivations, Types of data – scaled, binary, categorical, ordinal, Introduction to core clustering algorithms, Partitioning: k-means, k-mediods, Hierarchical: Agglomerative methods, ROCK | readings | A nice Python exploration of K-Means (by Thomas Breuel) [GH](https://github.com/tmbdev/teaching-mmir/blob/master/30-kmeans.ipynb) [NBV](https://nbviewer.jupyter.org/github/tmbdev/teaching-mmir/blob/master/30-kmeans.ipynb) | --  |
| CLUSTERING 2 | Density-based: DBSCAN, Model-based: Expectation-Maximization, Application – survey of clustering in SciPy Application – building a recommendation system in Python | readings | -- |  -- |
|  |  |  |  |  |
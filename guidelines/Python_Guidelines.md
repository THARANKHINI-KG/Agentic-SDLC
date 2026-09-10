# **Python Programming Standards and Guidelines** 

## **About this Document** 

### **Introduction and Purpose** 

The purpose of this document is to provide the coding standards, guidelines and Best Practices to be followed for Python Programming. 

### **Intended Audience** 

This document is intended for Python programmers and Reviewers who develop and review Python code and deploy them in Production environment. 

## **INTRODUCTION** 

This document describes the coding standards, naming conventions and guidelines to be followed when designing and implementing framework/ scripts using Python programming. These coding standards and guidelines will assure the consistency and maintainability of the code. 

## **PYTHON IDENTIFIER AND NAMING STANDARDS** 

An identifier in Python is a name that is used to identify a variable, function, class, module or other object. 

### **File Name** 

- File name should be in lower case 

- File name can have underscore to improve readability of the file name 

- The file name should be meaningful and should end with “.py” 

### Examples: 

Valid Names( samplefn.py, testfilen_series.py ) 

Non-Valid Names ( Samplefn.py, Xyzv.py, No887.py, testfilenmCheck.py ) 

### **Mandatory Rules for naming an identifier** 

- An identifier must start with a letter ( A-Z, a-z) or an underscore (_) or numbers 

- An identifier first character should be a letter or underscore, not numbers or special characters 

- Identifier names are case sensitive in Python 

- Keywords(True, False, break, continue etc.) cannot be used as identifiers 

### Examples: 

Valid identifier ( Emp_tcs, _salary, var1, role_ ) Non-valid identifier ( Emp@tcs, 2ndcar, $var1 ) 

Method name should not match with variable name 

**Conventions used while naming an identifier** 

|**Types**|**Description**|**Example**|
|---|---|---|
|Class names|CapWords/ CamelCase<br>convention|Class Student, class MyClass|
|Private|Single leading score|_private_variable|
|Specific meaning to<br>interpreter, Mangles names to<br>avoid name clashes with name<br>defined by subclasses|Two leading underscores|__private_variable|
|Language- defined special<br>name|Ends with two trailing<br>underscores|special_variable__|



__double_leading_underscore: Double underscore will mangle (“mangling” is the modification of the variables/ function names by the compiler/ interpreter with some rules) the attribute names of a class to avoid conflicts of attribute names between classes. 

The mangling rule of Python is adding the “_ClassName” as a prefix to the attribute names that are declared with double underscore. 

That is, if a method is named “__method” in a class, the name will be mangled in “_ClassName__method” form. 

### **Reserved Words** 

The following are the list of reserved words in Python. These words may not be used as any identifier name. (Python version 3.9.7) 

|`False`|`await`|`else`|`import`|`pass`|
|---|---|---|---|---|
|`None`|`break`|`except`|`in`|`raise`|
|`True`|`class`|`finally`|`is`|`return`|
|`and`|`continue`|`for`|`lambda`|`try`|
|`as`|`def`|`from`|`nonlocal`|`while`|
|`assert`|`del`|`global`|`not`|`with`|
|`async`|`elif`|`if`|`or`|`yield`|



The keywords mentioned in the above table, may vary based on the version of python. The list of keywords in the current version can be seen by typing the following in prompt. 

```
>>> import keyword
>>>print(keyword.kwlist)
```

For more detail refer 

```
>>> help("keyword")
```

## **SYNTAX** 

### **Spacing** 

Spaces are the preferred indentation method. 

Tabs or 4 spaces should be used solely to remain consistent with code that is already indented with tabs. Python 3 disallows mixing the use of tabs and spaces for indentation. 

Python 2 code indented with a mixture of tabs and spaces should be converted to using spaces exclusively. 

When invoking the Python 2 command line interpreter with the -t option, it issues warnings about code that illegally mixes tabs and spaces. When using –tt option, these warnings become errors. These options are highly recommended. 

### **Whitespace in Expressions and Statements** 

Avoid extraneous whitespace in the following situations: 

- Immediately inside parentheses, brackets or braces: 

```
# Correct:
spam(ham[1], {eggs: 2})
# Wrong:
spam( ham[ 1 ], { eggs: 2 } )
```

- Between a trailing comma and a following close parenthesis: 

```
# Correct:
foo = (0,)
# Wrong:
bar = (0, )
```

● Immediately before a comma, semicolon, or colon: `# Correct: if x == 4: print x, y; x, y = y, x # Wrong: if x == 4 : print x , y ; x , y = y , x` 

- However, in a slice the colon acts like a binary operator, and should have equal amounts on either side (treating it as the operator with the lowest priority). In an extended slice, both colons must have the same amount of spacing applied. 

Exception: when a slice parameter is omitted, the space is omitted: 

```
# Correct:
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
```

```
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]
# Wrong:
ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]
```

● Immediately before the open parenthesis that starts the argument list of a function call: `# Correct: spam(1) # Wrong: spam (1)` 

● Immediately before the open parenthesis that starts an indexing or slicing: `# Correct: dct['key'] = lst[index] # Wrong: dct ['key'] = lst [index]` 

● More than one space around an assignment (or other) operator to align it with another: `# Correct: x = 1 y = 2 long_variable = 3 # Wrong: x = 1 y = 2 long_variable = 3` 

- Avoid trailing whitespace anywhere. Because it's usually invisible, it can be confusing: e.g. a backslash followed by a space and a newline does not count as a line continuation marker. Some editors don't preserve it and many projects (like CPython itself) have pre-commit hooks that reject it. 

- Always surround these binary operators with a single space on either side: assignment (=), augmented assignment (+=, -= etc.), comparisons (==, <, >, !=, <>, <=, >=, in, not in, is, is not), Booleans (and, or, not). 

- If operators with different priorities are used, consider adding whitespace around the operators with the lowest priority(ies). Use your own judgment; however, never use more than one space, and always have the same amount of whitespace on both sides of a binary operator: 

### **Colon** 

Colon “ : “ using for Function, Loops, Conditions, Class defining as like curly braces in other programming language. 

Function defining by using colon 

`def addition(): a` … 

`b` … `def subtraction(): a` … `b` … 

Condition defining using colon 

`If (a == b ) : A` … `b` … `elif (` … `. ) : CC` … `DD` … 

Class defining using colon 

```
Class subject:
```

### **Indentation** 

- Use four (4) spaces to indent the code 

- Never use tabs or mix of tabs and spaces 

- Fixing line length (80 Columns) prevents lots of nesting and very long functions 

- It is suggested to have Indents of 4 spaces at minimum, though 8 spaces are ideal 

### **Line Length** 

It is recommended to have less than 80 characters in a line. If it does not fit within 80 characters, then it is an indication that some of the work should be encapsulated as a separate function. 

## **COMMENT STANDARDS** 

- Add comments to improve the readability. Comments that contradict the code are worse than no comments. Whenever there is a change in code, have a priority to update the comments 

- Comments should be complete sentences. If a comment is a phrase or sentence, its first word should be capitalized, unless it is an identifier that begins with a lower case letter 

- If a comment is short, the period at the end can be omitted. Block comments generally consist of one or more paragraphs built out of complete sentences and each sentence should end with a period 

- Use two spaces after a sentence-ending period 

- Document the changes to the framework/ scripts in the modification history. A modification history should contain the following: 

Name of the associate who changed the code: 

Date of change: 

Version: Changed function/ event: Change description: 

### **Block Comments** 

- Each line of a block comment starts with a # and a single space (unless it is indented text inside the comment) 

- These comments apply to some (or all) code that follows them and are indented to the same level as that code 

- Paragraphs inside a block comment are separated by a line containing a single # 

   - `# Increment my y value by one y = y + 1` 

### **Inline Comments** 

- An inline comment is a comment on the same line as a statement. These comments must be separated by at least two spaces from the statement and should start with a # and a single space 

- Avoid using inline comments in statements 

- Inline comments are unnecessary and in fact distracting if they state the obvious 

   - `y = y + 1 # Increment y` 

### **Documentation Strings** 

Conventions for writing good documentation strings (i.e. "docstrings"): 

Docstrings must be there for all public modules, functions, classes, and methods. Docstrings are not necessary for non-public methods, but a comment must be there to describe the method. This comment should appear after the def line. 

The """ that ends a multiline docstring should be on a line by itself, e.g.: 

```
"""Return a foobang
```

```
Optional plotz says to frobnicate the bizbaz first.
"""
```

For one liner docstrings, keep the closing """ on the same line. 

```
"""Return a foobang Optional plotz says to frobnicate the bizbaz first. """
```

```
class MinMaxScaler (TransformerMixin, BaseEstimator):
    """Transform features by scaling each feature to a given range.
    The transformation is given by::
        X_std = (X-X.min(axis=0)) / (X.max(axis=0) X.min(axis=0))
        X scaled = X_std * (max - min) + min
    where min, max = feature_range.
    Parameters
    -----------
    feature_range: tuple (min, max), default=(0, 1)
        Desired range of transformed data.
    Attributes
    -----------
    min_ : ndarray of shape (n_features,)
        Per feature adjustment for minimum. Equivalent to ``mi -  X.min(axis=0) *
```

```
self.scale_``
    Examples
    ---------
    >>> from sklearn.preprocessing import MinMaxScaler
    >>> data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
    >>> scaler = MinMaxScaler()
    >>> print(scaler.fit(data))
    MinMaxScaler()
    >>>>> print (scaler.data_max_)
    [ 1. 18.]
    >>> print (scaler.transform(data))
    [[0. 0. ]
    [0.25 0.25]
    [0.5 0.5]
    [1. 1. ]]
    >>> print(scaler.transform([[2, 2]]))
    [[1.5 0.]]
    See also
    --------
    minmax_scale: Equivalent function without the estimator API.
    """
    def _init_(self, feature_range=(0, 1), *, copy=True):
        self.feature_range = feature_range
        self.copy copy = copy
```

Documentation Strings with Sphinx: 

There are several different docstring formats, that can be used to enable Sphinx’s autodoc extension, for automatically generating documentation. 

A typical Sphinx docstring has the following format: 

```
"""[Summary]
:param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
:type [ParamName]: [ParamType] (, optional)
...
:raises [ErrorType]: [ErrorDescription]
...
:return: [ReturnDescription]
:rtype: [ReturnType]
"""
```

Pair of :param: and :type: directive options must be used for each parameter that is to be documented :raises: option - Used to describe the errors that are raised by the code :return: and :rtype: options – Used to describe values returned by code . 

Example: 

```
class SimpleBleDevice(object):
"""This is a conceptual class representation of a simple BLE device (GATT Server). It
is essentially an extended combination of the :class: `bluepy.btle.Peripheral` and
class:`bluepy.btle.ScanEntry` classes
```

```
:param client: A handle to the :class:`simpleble.SimpleBleClient` client object that
detected the device
:type client: class:`simpleble.SimpleBleClient`
:param addr: Device MAC address, defaults to None
:type addr: str, optional
:param addrType: Device address type -one of ADDR_TYPE_PUBLIC or ADDR_TYPE_RANDOM,
defaults to ADDR_TYPE_PUBLIC
:type addrType: str, optional
:param iface: Bluetooth interface number (0=/dev/hcio) used for the connection,
defaults to 0
:type iface: int, optional
:param data: A list of tuples (adtype, description, value) containing the AD type
code, human-readable description and value for all available advertising data items,
defaults to None
:type data: list, optional
:param rssi: Received Signal Strength Indication for the last received broadcast from
the device. This is an integer value measured in dB, where 0 dB is the maximum
(theoretical) signal strength, and more negative numbers indicate a weaker signal,
defaults to 0
:type rssi: int, optional
:param connectable: `True` if the device supports connections, and `False` otherwise
(typically used for advertising 'beacons')., defaults to False`
:type connectable: bool, optional
:param updateCount: Integer count of the number of advertising packets received from
the device so far, defaults to 0
:type updateCount: int, optional
"""
def __init_(self, client, addr=None, addrType=None, iface=0, data=None, rssi=0,
connectable=False, updateCount=0):
"""Constructor method
"""
super()._init_(deviceAddr=None, addrType=addrType, iface=iface)
self.addr = addr
self.addrType addrType
self.iface = iface
self.rssi = rssi
self.connectable = connectable
self.updateCount = updateCount
self.data = data
self._connected = False
self._services = []
self._characteristics = []
self._client = client
def getServices (self, uuids=None):
    """Returns a list of class:`bluepy.bite.Service` objects representing the
services offered by the device. This will perform Bluetooth service discovery if this
has not already been done; otherwise it will return a cached List of services
immediately..
```

```
    :param uuids: A List of string service UUIDs to be discovered, defaults to None
```

```
    :type uuids: list, optional
    :return: A list of the discovered : class:`bluepy.blte.Service` objects, which
match the provided ``uuids``
    :rtype: list On Python 3.x, this returns a dictionary view object, not a List
    """
    self._services = []
    if(uuids is not None):
    for uuid in uuids:
        try:
            service = self.getServiceByUUID(uuid)
            self.services.append(service)
        except BTLEException:
            pass
    else:
        self._services super().getServices()
    return self._services
```

## **IMPORTS** 

The imports are used only for packages and modules. The imports allow the reusability mechanism for sharing the code across modules. 

The imports can be defined as follows: 

import pack_or_module : – for importing modules and packages 

from pack_or_module import Z :- where pack_or_module is the package or module and z is the module name without prefix 

from pack_or_module import x as z :- if two modules named x are to be imported or x is long name 

- Imports must be on separate lines: 

```
# Correct:
import os
import sys
# Wrong:
import sys, os
# Correct:
from subprocess import Popen, PIPE
```

- Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants. 

- Imports should be grouped in the following order: 

   1. Standard library imports. 

   2. Related third party imports. 

   3. Local application/library specific imports. 

You should put a blank line between each group of imports. 

- Absolute imports are recommended, as they are usually more readable and tend to be better behaved (or at least give better error messages) if the import system is incorrectly configured (such as when a directory inside a package ends up on sys.path): 

```
import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example
```

However, explicit relative imports are an acceptable alternative to absolute imports, especially when dealing with complex package layouts where using absolute imports would be unnecessarily verbose: 

```
from . import sibling
from .sibling import example
```

- Standard library code should avoid complex package layouts and always use absolute imports. 

- When importing a class from a class-containing module, it's usually okay to spell this: 

```
from myclass import MyClass
from foo.bar.yourclass import YourClass
```

If this spelling causes local name clashes, then spell them explicitly: 

```
import myclass
import foo.bar.yourclass
```

and use "myclass.MyClass" and "foo.bar.yourclass.YourClass". 

- Wildcard imports (from <module> import *) should be avoided, as they make it unclear which names are present in the namespace, confusing both readers and many automated tools. There is one defensible use case for a wildcard import, which is to republish an internal interface as part of a public API (for example, overwriting a pure Python implementation of an interface with the definitions from an optional accelerator module and exactly which definitions will be overwritten isn't known in advance). 

- When republishing names this way, the guidelines below regarding public and internal interfaces still apply. 

Example: 

To import package, urllib2 is used for reading the data from urls and it can be written as 

```
import urllib2
```

(Packages: - The code base can be divided into clean and efficient modules using Python packages. The packages can be reused for sharing the code between different Python programs. Like a directory contains sub directories and files, a Python package can contain sub packages and modules) To import the module, use the full path name of the module. The advantage of specifying full path name avoids conflicts in module names and makes it easier to find the modules. It makes harder to deploy code, as there is a need to replicate package hierarchy. 

Imports should be as follows: 

```
import sound.filters.equalizer (reference code with complete name)
from sound.filters import equalizer (reference code with just module
name and is preferred)
```

## **NESTED/ LOCAL/ INNER CLASSES AND FUNCTIONS** 

Nested/ Local/ Inner classes and functions are acceptable. A class can be defined inside of a method, function or a class. A function can be defined inside a method or a function. Nested functions have read-only access to variables defined in enclosing scopes. The advantage is that they allow definition of utility classes and functions that are only used for a very limited scope. The disadvantages are nested or local classes cannot be pickled. 

Example of inner class: 

```
class Ivnbo:
def __init__(apna):
apna.name = 'Tsaml'
apna.head = apna.Head()
class Sird:
def boll(apna):
return 'talking...'
if __name__ == '__main__':
tsaml = Ivnbo()
print tsaml.name
print tsaml.sird.boll()
```

## **GLOBAL VARIABLES** 

Variables that are declared at module level are called global variables. Avoid use of global variables. The advantage of using global variable is that they are occasionally useful. The disadvantage is that it has potential to change the module behaviour during the import, because assignments to module-level variables are done when the module is imported. In favour of class variables, avoid the global variables. 

Some exceptions are as follows: 

- default options for scripts 

- module level constants. For example: PI = 3.14159 

It is sometimes useful for globals to cache values needed or returned by functions. If needed, globals 

should be made internal to the module and accessed through public module level functions. 

## **LIST COMPREHENSIONS** 

Use List comprehensions for simple cases. It can be used to construct lists in a very natural way like a mathematician is used to do 

For example: 

```
S= [x**2 for x in range(10)]
v= [2**i for i in range(13)]
```

Each portion must fit on one line: mapping expression, for clause, filter expression Multiple for clauses or filter expressions are not permitted, it is recommended to use loops in such cases. 

## **GENERATORS** 

The advantage is that it results in simple code. The state of the local variables and control flow are preserved for each call. A generator uses less memory than the function call that creates an entire list of values at once. 

Use “Yields” rather than return. 

The below Fibonacci series is an example of generator. 

```
def fib(max):
a, b = 0, 1
while a < max:
yield a
a, b = b, a + b
```

## **LAMBDA FUNCTIONS** 

Lambda functions are like lambda calculus, which is the backbone of functional programming. These functions defines anonymous functions in an expression as opposed to statement and often used to define callbacks or operators for higher-order functions like map() and filter(). 

The advantage is that they are convenient. The disadvantage is that it is difficult to read and debug than local functions. The lack of names means stack traces are more difficult to understand. Expressiveness is limited as the function may only contain an expression. 

If the code inside the lambda function is any longer than 60–80 characters, it's probably better to define it as a regular (nested) function. 

For common operations, instead of Lambda, use the functions available in the operator module. For example, for multiplication prefer operator.mul to lambda x,y: x * y. 

The below example illustrates the lambda function. 

```
double = lambda y: y * 2
print(double(5))
```

## **DEFAULT ITERATORS AND OPERATORS** 

These are used only with types that support them like files, lists and dictionaries. The Container types like lists and dictionaries, define default iterators and membership test operators ("in" and "not in"). The advantage is that these are simple and efficient. Without extra method calls, they express the operation directly. A function that uses default operators is generic. 

The type of object cannot be identified by reading the method names (e.g. has_key() means a dictionary). This is also an advantage. 

The built-in types(like list, dictionary and sets) also defines iterator methods. Better use these methods for methods that return lists, but ensure that the containers are not mutated, while iterating over it. 

```
Yes: for key in adict: ...
if key not in adict: ...
if obj in alist: ...
for line in afile: ...
```

`for k, v in dict.iteritems():` … `No: for key in adict.keys(): ... if not adict.has_key(key): ... for line in afile.readlines(): ...` 

## **EXCEPTIONS** 

Exceptions are events that can modify the flow of control through a program and must be used cautiously. 

Exceptions must follow certain conditions. 

1. Raise Exceptions as below: 

raise MyException('Error Message') or raise MyException 

Don’t use the two argument form (raise MyException, 'Error Message') or deprecated string based exception (raise 'Error message') 

2. Modules or packages should define their own domain specific base exception class, which should inherit from the built-in Exception class. The base Exception for a module should be called Error 

```
class Error(Exception):
pass
```

3. Never use catch-all except: statements, or catch Exception or StandardError, unless you are in the outermost block in your thread (and printing an error message) or re-raising the exception.The except: will really catch everything including sys.exit() calls, misspelled names, unit test failures, Ctrl+C interrupts and all kinds of other exceptions that the developer may simply don't want to catch 

4. It is recommended to have minimum code in a try/ except block. If the try block is larger, there is a high probability to get an unexpected exception by a line of code (which the developer didn’t expect to raise an exception), and the real error is hidden 

5. Use the finally clause to execute code whether or not an exception is raised in the try block. This is widely used for clean-up activities like closing a file 

6. For capturing an exception, instead of comma use “as” . For example: 

```
try:
raise Error
except Error as error:
pass
```

## **DEFAULT ARGUMENT VALUES** 

Default arguments are acceptable in most cases. 

These values for variables can be specified at the end of a function's parameter list, e.g. def dau(a,b=0) If dau is called with only one argument, then b is set to zero. If dau is called with two arguments, then b has the value of the second argument. 

It is acceptable to use with the following caveat: 

Do not use mutable objects as default values in the function or method definition. 

```
Yes: def bau(a, b=None):
if b is None:
b = []
No: def bau(a, b=[]):
...
No: def bau(a, b=time.time()): # The time the module was loaded???
...
No: def bau(a, b=FLAGS.my_thing): # sys.argv has not yet been parsed...
...
```

## **ZEN OF PYTHON** 

Also known as PEP 20, the guiding principles for python design. 

```
>>> import this
```

The Zen of Python, by Tim Peters Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules, although practicality beats purity. Errors should never pass silently, unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one and preferably only one obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea, let's do more of those! 

## **IDIOMS** 

Al programming idiom is a way to write code. 

Unpacking: If the length of a list or tuple is known, the names can be assigned to its elements with unpacking. 

Example: enumerate() will provide a tuple of two elements for each item in list 

```
for index, item in enumerate(mylist): # do something with index and item
x, y = y, x # Swapping the variables
x,(y,z) = 8,(7,9) #nested unpacking
```

In Python 3, a new method of unpacking defined as below 

```
x, *rest = [1, 2, 3]
# x = 1, rest = [2, 3]
x, *middle, d = [1, 2, 3, 4]
# x = 1, middle = [2, 3], d = 4
```

Create an ignored variable(throwaway variable): 

```
filename = 'filtst.txt'
basename, __, ext = filename.rpartition('.')
```

Though many Python style guides recommend to use the single underscore “_” for this variable, as “_” is generally used as an alias for the gettext() function and also at the interactive prompt to hold the value of the last operation, using a “__” will eliminate the risk of accidentally interfering with these other use cases. 

Create a length-N list of the same value 

This can be obtained with the Python list * operator: 

```
four_neons = [“neon”] * 4
```

Create a length-N list of lists 

```
four_lists = [[] for __ in xrange(4)]
```

Create a string from a list 

```
letters = ['w', 'a', 'r', 'n']
word = ''.join(letters)
```

Searching for an item in a collection 

```
s = set(['s', 'p', 'a', 'm'])
l = ['s', 'p', 'a', 'm']
def lookup_set(s):
return 's' in s
def lookup_list(l):
return 's' in l
```

## **CONVENTIONS** 

**Check if variable equals a constant:** 

Don’t need to explicitly compare a value to True or None or 0. The variable can be just added to the if statement. 

```
Bad:
if tstr == True:
print 'True!'
if tstr == None:
print 'tstr is None!'
Good:
# check just the value
if tstr:
print 'tstr is truth!'
```

```
# or check for the opposite
if not tstr:
print 'tstr is false!'
# or, as None is considered as false, explicitly check for it
if tstr is None:
print 'tstr is None!'
```

### **Access a Dictionary Element:** 

Don’t use the dict.has_key() method. Instead, pass a default argument to dict.get() or use x in d syntax. 

```
Bad:
d = {'pytho': 'elmnt'}
if d.has_key('pytho'):
print d['pytho'] # prints 'elmnt'
else:
print 'default_value'
Good:
d = {'pytho': 'elmnt'}
print d.get('pytho', 'default_value') # prints 'elmnt'
print d.get('tstdf', 'default_value') # prints 'default_value'
# Or:
if 'pytho' in d:
print d['pytho']
```

### **Short Ways to Manipulate Lists:** 

List comprehensions provide a powerful and concise way to work with lists. The map() and filter() functions also can perform operations on lists using more concise and different syntax. 

```
Bad:
# Filter elements greater than 4
x = [1, 4, 5]
y = []
for j in x:
if j > 4:
y.append(j)
Good:
x = [1, 4, 5]
y = [i for i in x if i > 4]
# Or:
y = filter(lambda x: x > 4, x)
Bad:
# Add three to all list members.
x = [1, 4, 5]
for j in range(len(x)):
x[j] += 3
Good:
x = [1, 4, 5]
x = [i + 3 for i in x]
# Or:
x = map(lambda i: i + 3, x)
```

Use enumerate() keep a count of your place in the list. 

```
x = [1, 5, 6]
for j, item in enumerate(x):
print j, item
# prints the below
# 0 1
# 1 5
# 2 6
```

The enumerate function provides better readability and it is also better optimized for iterators. 

### **Read From a File:** 

Use the “with open” syntax to read from files. This will automatically close files for you. 

```
Bad:
t = open('ftst.txt')
x = t.read()
print x
t.close()
Good:
with open('ftst.txt') as t:
for line in t:
print line
```

Better to use the with statement as it ensures that the file is closed always, even if an exception is raised inside the “with” block. 

### **Line Continuations:** 

When a logical line of code is longer than the accepted limit, split it over multiple physical lines. If the last character of the line is a backslash, the Python interpreter will join the consecutive lines. Though it is helpful, it is better to avoid this as a white space added to the end of the line, after the backslash, will break the code and may have unexpected results. 

A better solution is to use parentheses around your elements. Left with an unclosed parenthesis on an end-of-line the Python interpreter will join the next line until the parentheses are closed. The curly and square braces are also executed in the same way. 

```
Bad:
```

```
my_large_big_string = """For a long time I used to write very long sentences, \
when I had realized that, it was very difficult to update after that all are done and \
it took a very long time."""
```

```
from one.last.module.inside.a.module import a_need_function, another_need_function, \
yet_another_need_function
```

```
Good:
```

```
my_very_big_string = (
```

   - `" For a long time I used to write very long sentences,"` 

   - `" when I had realized that, it was very difficult to update, after that "` 

- `" all are done and it took a very long time."` 

- `)` 

```
from one.last.module.inside.a.module import (
a_need_function, another_need_function, yet_another_need_function)
```

But having to split a long logical line is an indication that you are trying to do too many things at the same time, and ofcourse the readability of the code also will be affected. 

## **POWER FEATURES** 

It is recommended to avoid these features. 

Python is extremely flexible language and gives you many fancy features such as metaclasses, access to bytecode, on-the-fly compilation, dynamic inheritance, object reparenting, import hacks, reflection, modification of system internals etc. 

The advantage is that these are powerful language features which can make code very compact. The disadvantage is that it is tempting to use these features when they're not absolutely necessary. It's harder to read, understand and debug code that's using these features. It doesn't seem that way at first (to the original author), but when revisiting the code, it tends to be more difficult than code that is longer but straight forward. 

Python bytecode helps to understand how Python execute your code. The dis module comes handy at disassembling bytecode. 

### **Metaclasses** 

By default, classes are constructed using type(). The class body is executed in a new namespace and the class name is bound locally to the result 

of type(name, bases, namespace). 

The class creation process can be customized by passing the metaclass keyword argument in the class definition line, or by inheriting from an existing class that included such an argument. In the following example, both MyClass and MySubclass are instances of Meta: 

```
class Meta(type):
```

```
pass
class MyClass(metaclass=Meta):
pass
class MySubclass(MyClass):
pass
```

When a class definition is executed, the following steps occur: 

- MRO entries are resolved; 

- the appropriate metaclass is determined; 

- the class namespace is prepared; 

- the class body is executed; 

- the class object is created 

### **Uses for metaclasses** 

The potential uses for metaclasses are boundless. Some ideas that have been explored include enum, logging, interface checking, automatic delegation, automatic property creation, proxies, frameworks, and automatic resource locking/synchronization. 

### **Determining the appropriate metaclass** 

The appropriate metaclass for a class definition is determined as follows: 

- if no bases and no explicit metaclass are given, then type() is used; 

- if an explicit metaclass is given and it is not an instance of type(), then it is used directly as the metaclass; 

- if an instance of type() is given as the explicit metaclass, or bases are defined, then the most derived metaclass is used. 

The most derived metaclass is selected from the explicitly specified metaclass (if any) and the metaclasses (i.e. type(cls)) of all specified base classes. The most derived metaclass is one which is a subtype of all of these candidate metaclasses. If none of the candidate metaclasses meets that criterion, then the class definition will fail with TypeError. 

## **DEPRECATED LANGUAGE FEATURES** 

It is recommended to: 

- Use string methods instead of the string module wherever possible 

- Use function call syntax instead of apply 

- Use list comprehensions and for loops instead of filter and map when the function argument have an inline lambda 

- Use for loops instead of reduce 

Current versions of Python provide alternative constructs that people find generally preferable. 

```
Good:
```

```
words = foo.split(':')
[x[1] for x in my_list if x[2] == 5]
map(math.sqrt, data) # Ok. No inlined lambda expression.
fn(*args, **kwargs)
Bad:
words = string.split(foo, ':')
map(lambda x: x[1], filter(lambda x: x[2] == 5, my_list))
apply(fn, args, kwargs)
```

## **THREADING** 

Do not rely on the atomicity of built-in types. 

While Python's built-in data types such as dictionaries appear to have atomic operations. There are corner cases where they aren't atomic (e.g. if __hash__or__eq__are implemented as Python methods) and their atomicity should not be relied upon. Also you should not rely on atomic variable assignment 

(since this in turn depends on dictionaries). 

Use the Queue module's Queue data type as the preferred way to communicate data between threads. Otherwise, use the threading module and its locking primitives. Learn about the proper use of condition variables so you can use threading.Condition instead of using lower-level locks. 

Example: (Threading) (https://www.saltycrane.com/blog/2008/09/simplistic-python-thread-example/) 

```
import time
from threading import Thread
def myfunc(i):
print "sleeping 5 sec from thread %d" % i
time.sleep(5)
print "finished sleeping from thread %d" % i
for i in range(10):
t = Thread(target=myfunc, args=(i,))
t.start()
```

## **TRUE AND FALSE EVALUATIONS** 

Use the "implicit" false if it is possible. Python evaluates certain values as false when in a Boolean context. A quick rule of thumb is that all empty values are considered false so 0, None, [], {}, ''; all evaluate as false in a Boolean context. 

The advantage is Conditions using Python Booleans are easier to read and less error-prone. In most cases, they're also faster. 

The disadvantage is that it may look strange to C/C++ developers. Use the "implicit" false if at all possible, e.g., if foo:rather than if foo != []. Below are few caveats that the developersshould know: Never use == or != to compare singletons like None. Use is or is not. 

Beware of writing if x: when you really mean if x is not None e.g., when testing whether a variable or argument that defaults to None was set to some other value. The other value might be a value that's false in a Boolean context. 

Never compare a Boolean variable to False using ==. Use if not x: instead. If there is a need to distinguish False from None then chain the expressions, such as if not x and x is not None:. 

For sequences (strings, lists, tuples), use the fact that empty sequences are false, so if not seq: or if seq: is preferable to if len(seq): or if not len(seq): 

When handling integers, implicit false may involve more risk than benefit (like accidentally handling 

None as 0). The developer may compare a value which is known to be an integer (and is not the result of len()) against the integer 0. 

```
Good:
if not users:
print 'no users'
if foo == 0:
self.handle_zero()
if i % 10 == 0:
self.handle_multiple_of_ten()
Bad:
```

```
if len(users) == 0:
print 'no users'
if foo is not None and not foo:
self.handle_zero()
if not i % 10:
self.handle_multiple_of_ten()
```

## **FUNCTION ARGUMENTS** 

Set of instruction: Function always start with def keyword 

### Default arguments: 

A default value can be given for an argument by using assigning operator(=) 

Example: 

```
def hello_world(xx, msg = ‘Hi’):
print(msg + “ “ +str(xx))
person1 = ‘Ram’
hello_world (person1)
Output: “Hi Ram”
```

### Keyword arguments: 

A function can be called with some values, which directly assign to their position based on order of priority. 

Example: 

```
def hello_world(name, msg):
print('Hi ‘ + name+ ‘ ‘+msg)
person1 = ‘Ram’
Message = ‘Good Morning’
hello_world ( person, message)
Output: Hi Ram Good Morning
```

Arbitrary arguments: 

In few scenarios, when the exact number of arguments are not known, the arbitrary arguments help to assign the value. 

Example: 

```
def hello_world(*args):
for arg in args:
print(‘Hello ‘ + “ “+str(arg))
hello_world(‘Ram’, ‘Sony’, ‘Axay’)
Output:
Hello Ram
Hello Sony
Hello Axay
```

## **PYTHON CODE ENCRYPTION TECHNIQUE** 

Cython is an optimizing static compiler for both the Python programming language and the extended Cython programming language (based on Pyrex). It makes writing C extensions for Python as easy as Python itself. The code can be encrypted inside python files to avoid any IP code/ business or technical solution approach getting exposed to all. 

Cython gives the combined power of Python and C to let the developer 

- write Python code that calls back and forth from and to C or C++ code natively at any point 

- easily tune readable Python code into plain C performance by adding static type declarations, also in Python syntax 

- use combined source code level debugging to find bugs in Python, Cython and C code 

- interact efficiently with large data sets, e.g. using multi-dimensional NumPy arrays 

- quickly build applications within the large, mature and widely used CPython ecosystem 

- integrate natively with existing code and data from legacy, low-level or high-performance libraries and applications 


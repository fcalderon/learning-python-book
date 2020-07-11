
# Chapter 4 - Introducing Python Object Types

- "Things to do stuff" -
"things" operations
"stuff" objects


- Python programs can be decomposed into modules, statements, expressions and
objects

- Programs are composed of modules
- Modules contain statements
- Statements contain expressions
- Expressions create and process objects


## On Python is "dynamically typed" but also "strongly typed"

This means that although Python manages types for you, you can only perform
valid operations on types. For example, lists operations can only be applied to
list type objects, and string operations can only be performed on string type
objects.

In Lutz's words:

> Python is ***dynamically typed***, a model that *keeps track of types for you
automatically* instead of requiring declaration code, but it is also
***strongly typed***, a constraint that means you can perform on an object *only
operations that are valid for its type*

--new-word: **whet** a thing that stimulates appetite or desire.

## On Type-Specific methods

"str".find("str") = substring
"str".replace("str", "another-str") = replace

Strings are immutable so any method on a string simply returns a new string.

--question: Why are strings typically immutable in programming languages?
--answer: From this link: https://stackoverflow.com/questions/93091/why-cant-strings-be-mutable-in-java-and-net. They are good for concurrency, they are less bug prone, they are simple.

## On Type-Specific Operations (pg 112)

The author claims that lists are more powerful in Python because they don't
have a fixed type. I wished Lutz explained his definition of powerful here
because I can't think of any scenario in which I'd find a list with no defined
types more powerful than a list with types. As a matter of fact, not even the
other way around. Both have its pros and cons in terms of typing.

The point about lists not being fixed in size is definitely useful to
developers.

## On Comprehension

### List Comprehension

This is a lovely feature that seems convenient and time saving. I'm still
getting familiar with the syntax, but it looks like the following example:

```Python

# a simple list of objects
fruit_objects = [{'name': 'apple', 'color': 'red'},
                 {'name': 'orange', 'color': 'orange'},
                 {'name': 'grape', 'color': 'purple'}
]

# list comprehension in action

fruit_names = [fruit['name'] for fruit in fruit_objects]

assert fruit_names == ['apple', 'orange', 'grape']

```

List comprehension is very similar to `map` in other languages.

For example, in JavaScript, the same can be accomplished:

```JavaScript
const fruitObjects = [{name: 'apple', color: 'red'},
                 {name: 'orange', color: 'orange'},
                 {name: 'grape', color: 'purple'}];

const fruitNames = fruitObjects.map(fruit => fruit.name);

assert(fruitNames, ['apple', 'orange', 'grape']);
```

Note that Python also has a `map` function:

```Python

# list comprehension in action

fruit_names = list(map(lambda fruit: fruit['name'], fruit_objects))

assert fruit_names == ['apple', 'orange', 'grape']

```

### Other applications to Comprehension

Comprehension syntax can also be used in other data types. For example, you
can create sets:

```Python
fruit_objects = [{'name': 'apple', 'color': 'red'},
                 {'name': 'apple', 'color': 'green'},
                 {'name': 'grape', 'color': 'purple'},
                 {'name': 'grape', 'color': 'green'},
]

assert {'apple', 'grape'} == {fruit['name'] for fruit in fruit_objects}

```

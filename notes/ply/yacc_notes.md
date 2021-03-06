# yacc notations

[extremely nice tutorial](http://www.dabeaz.com/ply/ply.html)

## an example

see `yacc_demo.py`

Note: The use of negative indices have a special meaning in yacc---specially p[-1] does not have the same value as p\[3\] in this example. Please see the section on "Embedded Actions" for further details.

## Combining Grammar Rule Functions

```python
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(t):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]
```

👇

```python
def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
```

## empty productions

```python
def p_empty(p):
    'empty :'
    pass

def p_optitem(p):
    'optitem : item'
    '        | empty'
    ...
```

Note: You can write empty rules anywhere *by simply specifying an empty right hand side*. However, I personally find that writing an "empty" rule and using "empty" to denote an empty production is **easier to read and more clearly states your intentions.**

## Dealing with ambigious Grammars

An typical ambigious example:

```
expression : expression PLUS expression
           | expression MINUS expression
           | expression TIMES expression
           | expression DIVIDE expression
           | LPAREN expression RPAREN
           | NUMBER
```

```python
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)
```

通过上面的语句，

1. `+`, `-`, `*`, `/` 均为 left associative
2. `+`, `-` 同一优先级，`*`, `/` 同一优先级
3. `*`, `/` 优先级高于 `+`, `-`

还是无法处理 `3 + 4 * -5` 的情况，或者有些时候我们并不希望结合律呢？

```python
precedence = (
	('nonassoc', 'LESSTHAN', 'GREATERTHAN'),  # Nonassociative operators
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),            # Unary minus operator
)

def p_expr_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]
```
## Syntax Error Handling

### Recovery and resynchronization with error rules

The most well-behaved approach for handling syntax errors is to write grammar rules that include the error token.



### Panic mode recovery

An alternative error recovery scheme is to enter a *panic mode recovery* in which tokens are *discarded* to a point where the parser might be able to *recover in some sensible manner*.

Panic mode recovery is implemented entirely in the `p_error()` func.

```python
# eg 1
def p_error(p):
    print("Whoa. You are seriously hosed.")
    if not p:
        print("End of File!")
        return

    # Read ahead looking for a closing '}'
    while True:
        tok = parser.token()             # Get the next token
        if not tok or tok.type == 'RBRACE': 
            break
    parser.restart()

# eg 2
def p_error(p):
    if p:
        print("Syntax error at token", p.type)
        # Just discard the token and tell the parser it's okay.
        parser.errok()
    else:
        print("Syntax error at EOF")
```


## Line Number and Position Tracking
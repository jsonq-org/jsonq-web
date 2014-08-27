{
	"name": "Queries"
}

The JSONQ query is where all the magic happens. Below, you'll find descriptions of all the parts of
a JSONQ query. They should all seem familiar in function if not in name to something you are used
to.

# The Basics

These are the basic clauses you will need to construct a simple, valid query.

## from

The `from` clause describes what resources to search. It can be single-valued or multi-valued (for
the join case).

### single store
	{
		"from": "Products"
		...
	}
### multiple stores
	{
		"from": ["Products", "Customers"]
		...
	}

Joins will be covered in more detail later. For now, we'll stick to the single-store case.

## as

The `as` clause allows you to specify a variable with which to reference the store. In the case of a
join, the order of variable definitions here must match the order of store definitions in the
`from` clause

### single store
	{
		"from": "Products"
		"as": "p"
		...
	}

In this case, you will be able to refer to items in the `Products` store using the variable `p` in
your query's `where` or `select` clauses.

### multiple stores
	{
		"from": ["Products", "Customers"]
		"as": ["p", "c"]
		...
	}

With the multiple-store case, you will be able to refer to items in the `Products` store using 
the variable `p`and items in the `Customers` store with the variable `c`

## where

The `where` clause allows you to restrict your query. Without `where`, queries would be pretty
useless. `where` is an object which contains either a simple clause or a group of clauses.

### simple clause

The simple clause is an expression which evaluates to either `true` or `false`. This expression is
run against the objects in a store to determine matches.

In a C-like programming language, a clause would look like:

    p.unitsInStock > 5

In JSONQ, this becomes:

	{
		"from": "Products"
		"as": "p"
		"where": {
			"lhs": "p.unitsInStock",
			"op": ">"
			"rhs": 5,
		},
		...
	}

Let's break this down:

 - **lhs** stands for 'left-hand side'. This is the portion of the clause to the left of the
   operator.
 - **rhs** stands for 'right-hand side'. This is the portion of the clause to the right of the
   operator.
 - **op** is the operator to apply. This tells the JSONQ engine how to evaluate the left-hand side
   against the right-hand side. The valid values for `op` are described at the end of this section.

Pretty simple, right? Now, let's move on to groupings.

### groupings

Sometimes, a clause just doesn't cut it. What if you want to know what products have a high price
and low quantity? Well, you'll need a grouping to combine clauses.

The C-like equivalent of a grouping would be something like:

	p.unitsInStock < 3 && p.unitPrice > 100

In JSONQ, this becomes:

	{
		"from": "Products"
		"as": "p"
		"where": {
			"op": "AND",
			"value": [
				{
					"lhs": "p.unitsInStock",
					"op": "<"
					"rhs": 3,
				},
				{
					"lhs": "p.unitPrice",
					"op": ">"
					"rhs": 100.00,
				}]
		},
		...
	}

As you can see, a Grouping is defined by the operation and a set of expressions. You can have any number
of clauses *or* groupings inside a grouping.

The order of expressions inside a grouping matters. Each expression will be evaluated in the order
it is positioned inside the `value` array. If the expression is a grouping, it is evaluated in a
depth-first manner.

### valid operators

For clauses, the valid operators are: **>**, **>=**, **=**,  **<=**, and **<**. These should
be familiar to you. In order, they mean: greater-than, greater-than or equals, equals, less-than or
equals, and less-than.

Note that for strings, the equals operator is an exact match. For pattern matching, you should use
the operator **=~**. This will indicate to the engine that the expression contains regular
expressions.

For groupings, the valid operators are:

 - **AND**: all clauses must evaluate to `true`
 - **OR**: at least one clause must evaluate to `true`



clause:

attribute 
operator
value

group:

grouping (op)
elements

intersection: [...]
union: [...]
and: [...]
or: [...]

a

	( a && b ) || c
	
	(&(unitsInStock>0)(unitPrice>3))

--

where

 - Grouping
  - op, value
  - has operator (AND, OR)
  - contains n>=1 Clauses (only >=2 makes sense)

 - Clause
  - key, value, op
  - simple inequality (GT, GE, EQ, LE, LT)
  - regex?
  - key is field reference (using selection var name)

select

 - string or array
  - string is either:
      - selection var (i.e. - p) 
      - field reference (i.e. - p.name)
      - operator (i.e. - min(p.price), max(p.price), avg(p.price))
  - array is array of strings for limited object (i.e. - p.name, p.city, p.state) - cannot
		  contain an operator!

order

 - field name, sort order
 - single value or array

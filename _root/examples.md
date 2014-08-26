{
	"title": "examples"
}

# JSONQ examples

The following example demonstrates a simple aggregation.

## Data

	[ 2, 2, 3, 5, 5 ]

## Request

	{
		"distinct": {
			"from": "args[0]",
			"as": "n",
			"select": "count(n)"
		}
	}

# Result

	{
		"results": [ 2, 3, 5 ]
	}

{
	"title": "JSONQ"
}

# What is JSONQ?

JSONQ is a JSON-based specification for data access and storage. All operations are, fundamentally,
able to be represented as [JSON][] documents. By using JSON messages to represent data operations,
JSONQ provides a flexible base layer for building asynchronous language bindings.

# Language Bindings

JSONQ is a language-agnostic specification. If your language of choice can handle JSON, it can be
used with JSONQ-compliant data sources. Writing JSON queries is not going to save you any time,
however, so language bindings are expected to be used to fully leverage JSONQ.

Some examples of possible bindings are provided below. This is the JSONQ query being demonstrated:

	{
		"from": "Products",
		"as": "p",
		"group": {
			"by": "p.category",
			"into": "cat"
		},
		"select": {
			"category": "cat.key",
			"products": "cat"
		}
	}

## Javascript

	var products = jsonq.getStore("Products");
	products
		.as("p")
		.group( "p.category", "cat" )
		.select(
			{
				"category": "cat.key",
				"products": "cat"
			},
			function(results) {
				for (var i = 0; i<results.length; i++) {
					var r = results[i];
					console.log(
						"There are " + r.products.length +
						" products in category '" + r.category+"'" );
				}
			}

		)

 [JSON]: http://www.json.org "JSON"


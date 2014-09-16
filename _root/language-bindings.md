{
	"title": "language bindings"
}

# Language Bindings

JSON/q is a language-agnostic specification. If your language of choice can handle JSON, it can be
used with JSON/q-compliant data sources. Writing JSON queries is not going to save you any time,
however, so language bindings are expected to be used to fully leverage JSON/q.

Using language bindings, you can leverage JSON/q on whatever platform you choose: Android, iOS,
Windows Phone, web, NodeJS, J2EE. Language bindings provide APIs in a language-appropriate
style, making integration with JSON/q second-nature.

Some examples of possible bindings are provided below. This is the JSON/q query being demonstrated:

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
		.group("p.category", "cat")
		.select(
			{ "category": "cat.key",
			  "products": "cat" },
			function(results) {
				for (var i=0; i<results.length; i++) {
					var r = results[i];
					console.log(
						"There are " + r.products.length +
						" products in category '" + r.category+"'" );
				}
			}

		)

 [JSON]: http://www.json.org "JSON"


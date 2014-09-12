{
	"title": "JSONQ"
}

# What is JSONQ?

JSONQ is a JSON-based specification for data access and storage. All operations are, fundamentally,
able to be represented as [JSON][] documents. By using JSON messages to represent data operations,
JSONQ provides a flexible base layer for building asynchronous language bindings.


# Project Goals

The JSONQ project is designed to make developers' lives easier by providing a unified language for
accessing and querying data.

### Open Specification

We aim to provide a detailed and open specification for JSONQ. This will enable anyone to build
JSONq-compliance into their product whether it is a database, SDK, or web service. This openness will
also allow us to easily gather and incorporate feedback from everyone using JSONQ.

### Ubiquitous Promotion

The more places a technology exists, the more useful it is. We aim to promote JSONQ across the
software development world to have it supported in major browsers, databases, and webservices.

# Capabilities

We envision a world without language barriers when dealing with data sources. Why should developers
have to treat MySQL any differently than PostgreSQL? Or MongoDB?

What about Facebook? Twitter? Wikipedia? Fundamentally, these services provide data. Why, then, must
we treat them differently than traditional databases?

JSONQ aims to unify the way you talk about **any** data source, allowing you to easily incorporate
Facebook data into your business app, join across MySQL and Wikipedia, or join device SMS messages
with your in-app messaging.

# Language Bindings

JSONQ is a language-agnostic specification. If your language of choice can handle JSON, it can be
used with JSONQ-compliant data sources. Writing JSON queries is not going to save you any time,
however, so language bindings are expected to be used to fully leverage JSONQ.

Using language bindings, you can leverage JSONQ on whatever platform you choose: Android, iOS,
Windows Phone, web, NodeJS, J2EE. Language bindings provide APIs in a language-appropriate
style, making integration with JSONQ second-nature.

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


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
			function(response) {
				if(response.success) {
					var results = response.payload;
					for (var i=0; i<results.length; i++) {
						var r = results[i];
						console.log(
							"There are " + r.products.length +
							" products in category '" + r.category+"'" );
					}
				} else {
					console.log("An error occurred");
				}
			});

## Java 7

	JsonqStore<Product> products = JSONQ.getStore("Products");

	JSONObject grouping = new JSONObject();
	grouping.put("category", "cat.key");
	grouping.put("products", "cat");

	Callback<JSONObject> callback = new Callback<JSONObject>() {
		public void onResponse(JSONObject response) {
			if(response.getBoolean("success")) {
				JSONArray results = response.getJSONArray("payload");
				for (int i=0; i<results.length(); i++) {
					JSONObject obj = results.getJSONObject(i);
					JSONArray result = obj.getJSONArray("products");
					System.out.println(
							"There are " + result.length() +
							" products in category '" + 
							obj.getString("category") + "'" );
				}
			} else {
				System.out.println("An error occurred");
			}
		}
	};

	products
		.as("p")
		.group("p.category", "cat")
		.select(grouping, cb);

## Java 8

	JsonqStore<Product> products = JSONQ.getStore("Products");

	JSONObject grouping = new JSONObject();
	grouping.put("category", "cat.key");
	grouping.put("products", "cat");

	products
		.as("p")
		.group("p.category", "cat")
		.select(
				grouping,
				(JSONObject response) -> {
					if(response.getBoolean("success")) {
						JSONArray results = response.getJSONArray("payload");
						for (int i=0; i<results.length(); i++) {
							JSONObject obj = results.getJSONObject(i);
							JSONArray result = obj.getJSONArray("products");
							System.out.println(
									"There are " + result.length() +
									" products in category '" + 
									obj.getString("category") + "'" );
						}
					} else {
						System.out.println("An error occurred");
					}
				});

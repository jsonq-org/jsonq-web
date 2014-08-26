{
	"title": "JSONQ"
}

# What is JSONQ?

JSONQ is a JSON-based specification for data  access and storage. All operations are, fundamentally,
able to be represented as [JSON][] documents.

There are two main pathways to use JSONQ: provisioning and data access.

## Provisioning

Provisioning is governed by a schema, which defines an object store. The schema is itself a [JSON][]
object. For more details on the schema, see the [JSONQ schema specification][schema].

Provisioned stores may be extended with additional functionality. This functionality is not part of
the JSONQ specification, but it is available at the language binding layer.

## Data access

JSONQ provides facilities for basic data acces ([CRUD][]), but it really shines when it comes to
querying your data. 

### Defining Data

To be able to access data, we must first define what data is. JSONQ is designed to manipulate any
valid [JSON][] document. Here is very simple example document describing a user:

	{
		"username": "thedude",
		"firstName": "Jeff",
		"lastName": "Lebowski"
	}

This document is [valid JSON][], but it is also extremely simple. Let's extend it a bit:

	{
		"username": "thedude",
		"firstName": "Jeff",
		"lastName": "Lebowski",
		"nicknames": ["The Dude", "His Dudeness", "Duder", "El Duderino"]
	}

Again, we have [valid JSON][]. And it is still very simple. Note that we have added a multi-valued
field. This is very possible via JSONQ, but the schema can restrict whether or not a field is
allowed to have multiple values. 

Now, let's extend the example some more:

	{
		"username": "thedude",
		"firstName": "Jeff",
		"lastName": "Lebowski",
		"nicknames": ["The Dude", "His Dudeness", "Duder", "El Duderino"],
		"emailAddresses": [
			{
				"type": "home",
				"value": "the.dude@gmail.com"
			},
			{
				"type": "work",
				"value": "jeff.lebowski@examplecorp.com"
			}
		],
		"phoneNumbers": [
			{
				"type": "mobile",
				"value": "+1 303 555 5555"
			},
			{
				"type": "work",
				"value": "+1 619 555 5555"
			},
			{
				"type": "work_fax",
				"value": "+1 619 555 5556"
			}
		],
		"password": "{SHA256}A7CCB907F7E20BCA162A19957E114A225095DB2C5E5B4372A806E5EE9996E3D2",
		"securityQuestion": "What is my favorite drink?",
		"securityAnswer": "Caucasian"
	}

Now you may be thinking, "Who uses a fax line anymore?", but the important thing to note here is
that you can store (and query) nested objects via JSONQ. Also, fax was still fairly prevalent in 1998.

Due to the fact that JSONQ stores may be backed by database engines which are inefficient at 
storing nested trees, **it is recommended you keep your objects simple when it comes to nesting**.

## Basic CRUD

JSONQ specifies CRUD, but it does not stick to the conventional names, eschewing them for some
friendlier verbs, but leaving an acronym without a vowel!

### Save

Now that we have a valid data structure to store, let's store it.

	{
		"store": "User",
		"save":
		{
			"username": "thedude",
			"firstName": "Jeff",
			"lastName": "Lebowski",
			"nicknames": ["The Dude", "His Dudeness", "Duder", "El Duderino"],
			"emailAddresses": [
				{
					"type": "home",
					"value": "the.dude@gmail.com"
				},
				{
					"type": "work",
					"value": "jeff.lebowski@examplecorp.com"
				}
			],
			"phoneNumbers": [
				{
					"type": "mobile",
					"value": "+1 303 555 5555"
				},
				{
					"type": "work",
					"value": "+1 619 555 5555"
				},
				{
					"type": "work_fax",
					"value": "+1 619 555 5556"
				}
			],
			"password": "{SHA256}A7CCB907F7E20BCA162A19957E114A225095DB2C5E5B4372A806E5EE9996E3D2",
			"securityQuestion": "What is my favorite drink?",
			"securityAnswer": "Caucasian"
		}
	}

As you can see, saving data is as simple as wrapping it in an object specifying the operation
(`save`) to perform and the store (`User`) on which to perform it. 

#### Create vs. update

You may have noticed the example above uses the verb `save` rather than `create` or `update`. JSONQ
requires each store have a unique key. It also requires store providers generate this key if it is
not present. If the key field is not present or an object with the specified key does not exist in
the store, the `save` is a `create`. Otherwise, it is an `update`. You can read more about keys in
[the schema page][schema_keys].

### Fetch

While retrieving a specific object is just a specific form of a query, JSONQ provides the shortcut
syntax for `fetch`: 

	{
		"store": "User",
		"fetch": "thedude"
	}

This example assumes the `username` field is specified as the key for the `User` store. Again, you
can find more information about keys on [the schema page][schema_keys].

### Delete

`delete` uses the same simplified syntax as `fetch`, matching the key of the object to delete:

	{
		"store": "User",
		"delete": "thedude"
	}



 [schema]: /schema "JSONQ Schema"
 [schema_keys]: /schema#toc\_2 "JSONQ Schema | Keys"
 [JSON]: http://www.json.org "JSON"
 [valid JSON]: http://www.jsonlint.org "JSON Lint"
 [CRUD]: https://en.wikipedia.org/wiki/CRUD "Create, read, update, and delete"


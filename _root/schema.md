{
	"title": "Schema"
}

# JSONQ Schema

To provision a JSONQ store, you must provide a schema describing the store's contents. This is where
you can specify whether a field is multi-valued, indexed, or required.

Here's an example schema. We'll walk through each line below.

	{
		"docType": "schema"
		"name": "Customer",
		"provider": "mem",
		"key": "guid",
		"fields": [
			"firstName",
			"lastName",
			{
				"name": "email",
				"index": true,
			}
			"address",
			"city",
			"region",
			"postalCode",
			"country",
			{
				"name": "phone",
				"multi": true,
			},
			"fax",
		]
	}

## Store information

The attributes specify information about the store itself. We give the store a name
(`Customer`) and specify which provider to use (in this case, `mem` represents a RAM-backed store).

### Keys
The `key` attribute specifies the name of the field to be used as a unique identifier for this
store. This is an optional field; if it is not specified, it will default to `guid`. This field is
automatically configured with the following constraints:

	{
		"ignoreCase": true,
		"index": true,
		"multi": false,
		"required": true,
		"unique": "YES"
	}

If the `key` attribute is not provided, the store provider will create one prior to storing the
object.

### Fields

The final attribute in a JSONQ schema is the `fields` attribute. This is an array of fields which
may be stored on objects in this store. **This list must be fully-formed to be able to store data via
JSONQ. Attempting to store any fields which are not specified will result in a failure.**

The specification for each field can be as simple as a string:

	"fields": [
		...
		"firstName",
		...
	]

Or a more-complex JSON object:

	"fields": [
		{
			"name": "email",
			"ignoreCase": true,
			"index": true,
			"multi": true,
			"required": false,
			"unique": "IF_PRESENT"
		}
	]

The complex field definition allows for basic optimization and validation to occur.

#### Field Definition Attributes

Here is a description of all the possible attributes which can be used to describe a field definition.

##### name

`name` is fairly self-explanatory. This is the name of the field being stored. The
value *must* be a valid, non-empty JSON string.

> ***name***: *non-empty JSON string*

##### ignoreCase

`ignoreCase` specifies whether comparisons for this field should be case-sensitive or
not. The value *must* be a boolean.

> ***ignoreCase***: \[*true*|*false*\] (*default*: ***false***)

##### index

`index` causes the provider to index the given field to optimize searches. The value *must* be a boolean.

> ***index***: \[*true*|*false*\] (*default*: ***false***)

##### multi

`multi` specifies whether the field can contain multiple values or not. The value *must* be a boolean.

> ***multi***: \[*true*|*false*\] (*default*: ***false***)

##### required

`required` specifies whether the field must be present. The value *must* be a boolean.

> ***required***: \[*true*|*false*\] (*default*: ***false***)

##### unique

`unique` specifies whether the field is unique in the store or not. The value *must* be one of
`YES`, `NO`, or `IF_PRESENT`. 

 - `YES` means the field is fully unique. Only one object may be stored with no value for the field.
 - `NO` means that duplicates are allowed for any value, including `null`
 - `IF_PRESENT` means the field must be unique if there is a value, but any number of objects may have `null` as the value for this field

> ***required***: \[*YES*|*NO*|*IF_PRESENT*\] (*default*: *NO*)

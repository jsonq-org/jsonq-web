{
	"title": "Transactions"
}

There are two ways to initiate transactional boundaries in JSONQ: explicit and implicit.

# explicit transactions

Explicit transactions follow the *start..execute..commit* process. Since all JSONQ commands are
serializable as JSON, this method can easily span multiple messages. The engine will simply queue
the commands until the `commit` message arrives.

## starting a transaction

To start a transaction, a simple command must be sent:

	{
		"startTxn": "My Transaction"
	}

The provided string can be `null` - it is simply used as a nice name for debugging purposes. This
command will result in a transaction ID being issued. **This ID must be included in all messages
pertaining to the transaction.**

	{
		"txnId": "xxx",
		"save": { ... }
	}

Or:

	{
		"txnId": "xxx",
		"delete": "yyy"
	}

## Committing a transaction

Once all commands are issued for the transaction, you may commit the transaction with a final
message:

	{
		"commit": "xxx"
	}

A response message will be generated with the transaction ID inside it when the transaction fails or
succeeds.


# implicit transactions

In some cases, it may be more convenient to not worry about `start` and `commit`. In this case, you
can simply send a JSON document containing an array of changes to be made. These changes will then be
wrapped in a transactional boundary automatically and executed in order.

    [
	    {
		    "save": { ... }
		},
		{
		    "delete": "GUID"
		},
		{
		    "delete": {
				"query": { ... }
			}
		},
	]

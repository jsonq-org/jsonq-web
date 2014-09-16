{
	"title": "virtDB"
}

# What is virtDB?

To facilitate JSON/q adoption, we have created an abstraction layer called virtDB. Since JSON/q is
simply a specification, virtual layers can easily be integrated. VirtDB allows building drivers for
any data source which does not have native JSON/q support.

At its most basic, virtDB is a pair of APIs: `DatabaseProvider` and `StoreProvider`. These describe
the interaction between JSON/q messages and the underlying storage system.

## DatabaseProvider

The *DatabaseProvider* accepts a JSON/q message, returns a transaction ID, and fires a callback
(containing a JSON/q response) when the operation is complete. Remember, all JSON/q operations 
are message-based, so the APIs should be asynchronous where possible.

*DatabaseProvider* is responsible for parsing the JSON/q request, assembling results from the
store(s), and returning results to the caller. The results are in the form of a JSON/q message, and
can contain either data or an error, depending on whether or not the operation succeeded.

## StoreProvider

The *StoreProvider* is an internal API to be used by the *DatabaseProvider*. It allows the
*DatabaseProvider* to provision it, query capabilities, and perform basic CRUD operations. Based on the
capabilities of the *StoreProvider*, other operations including searching, indexing, and transaction
management may be provided.

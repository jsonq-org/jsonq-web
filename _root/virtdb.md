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

# Examples

In its most basic application, virtDB simply sits on top of an existing data source, complying
with the JSON/q specification.

<div class='example'>
<img src='{{urls.media}}/simple.jpg' />
</div>

When we say any data source, we mean it. You can reduce the friction prototyping your app by using a
simple RAM-backed *StoreProvider*. Using the virtDB layer ensures you don't have to change your
application code when the time comes to move beyond prototyping and use a real database.

<div class='example'>
<img src='{{urls.media}}/prototype.jpg' />
</div>

With the JSON/q interface in front, the actual implementation of the store doens't matter. It can
easily be a remote store. The *StoreProvider* needs to know how to interact with its counterpart 
on the remote end, but this is all behind the scenes. The *StoreProvider* can communicate with the
real data source via [IPoAC][], and the you are still insulated by the JSON/q specification and
virtDB layer.

<div class='example'>
<img src='{{urls.media}}/proxy.jpg' />
</div>


 [IPoAC]: https://en.wikipedia.org/wiki/IP_over_Avian_Carriers

{
	"title": "messaging"
}

JSON/q is a message-based specification. This enables it to be easily ported to many platforms, as
there is no need to deal with streaming I/O, additional connection protocols, etc.

Basic JSON/q operations follow a Request-Response model. Responses may be generated at any stage in
the pipeline while handling a request. In the client-server case, this includes both the client and
the server.

## Request

A JSON/q request **must** contain the following attributes:

 - ID
 - type
 - payload

### ID

The *ID* is a unique identifier for the request. This field is used to correlate responses with
requests and fire the proper response handler.

### Type

The *type* field specifies what type of operation is to be performed. Examples include *save*,
*delete*, and *query*.

### Payload

The *payload* field is any payload required by the operation. In the case of a *save*, this would
contain the object to be saved; with a *query*, the actual query object.

* * *

The request may contain other fields, depending on the capabilities of the *DatabaseProvider*. These
include, but are not limited to, *txn_id* and *args*.

## Response

A JSON/q response **must** contain the following attributes:

 - request_id
 - success
 - payload

### request_id

The *request_id* field is the ID of the request to which this response belongs. This is used 
for correlating the response with the correct request.

### Success

The *success* field is a boolean field representing whether or not the operation was a success. If
`true`, the *payload* field contains results; if it is `false`, the *payload* field will contain an
error.

### Payload

This field holds the payload to be returned to the requestor. Depending on the *status* field, it
will either be results from the operation or an error.

* * *

The response may contain other fields, depending on the capabilities of the *DatabaseProvider*. These
include, but are not limited to, *txn_id*.

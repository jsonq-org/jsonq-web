{
	"title": "JSONQ Messages"
}

# Messaging

JSONQ uses a message-based infrastructure for communicating commands. This allows us to provide a
flexible specification that is easily implemented in a variety of languages.

There are two interface points which must be implemented:
	- execute: used to send messages to the JSONQ engine
	- onMessage: Handler registered to be called when a message comes back from the engine

## execute

The `execute` endpoint accepts a JSON string representing a JSONQ document. This document can be a
single command to execute, or it can be an array of commands to execute.

### single command

A single command is simply one JSON object:

	{
		"save": { ... }
	}

### multiple commands

Multiple commands are represented by an array of JSON objects:

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

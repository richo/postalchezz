This is a turn based app that will be hosted on Google App Engine.

BUGS
----

The kludginess around wrapping `include` in `emit` inside a template upsets me.
On the other hand if you make `include` talk directly to the response you end
up with race condition issues.. it's almost like I should have used a big boy
templating engine

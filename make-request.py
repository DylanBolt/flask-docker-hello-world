# ~~~ make-request.py ~~~

# route 1 -- ping
def call_ping_route():
  r = ___ # make the request
  return r

# route 2 -- random word
def call_random_word_route():
  r = ___ # make the request
  return r

# route 3 -- string count
def call_string_count():
  r = ___ # make the request
  return r

route_callers = [
  call_ping_route
  call_random_word_route
  call_string_count
  ]

for call_route in route_callers:
  r = call_route()
  ___ # first, check r for errors
  data = r.json()
  print(data) # print the response

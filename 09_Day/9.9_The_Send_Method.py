def smart_consumer():
    print("Consumer started")
    x = yield "Ready"  # প্রথম পজ এখানে
    print(f"Received: {x}")
    y = yield "Waiting" # দ্বিতীয় পজ এখানে
    print(f"Received y: {y}")
g = smart_consumer()
print(next(g))
print(g.send(10))
# print(next(g))
# print(g.send(0))
g.send(0)
# try:
#     # print(next(g))
#     print(g.send(0))
#     raise ValueError('Sorry, Value Error')
# except ValueError as e:
#     print(f'The generator is end .{e}')

from channels import include

channel_routing = [
    include("pconsumer.routing.channel_one", path=r"^/chat/"),
    include("pconsumer.routing.channel_two", path=r"^/chat1/"),
]
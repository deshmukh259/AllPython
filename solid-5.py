class AA():
    def request(self, url: str, options: dict) -> str:
        pass


class NodeHttpService(AA):
    def request(self, url: str):
        print("NodeHttpService")


class NodeHttpService1():
    def request(self, url: str, options: dict) -> str:
        print("-->",url)
        print("NodeHttpService1")


class A(NodeHttpService1, NodeHttpService):
    def __int__(self):
        print ("A obje")


if __name__ == "__main__":
    c = A()
    b = c.request("urlssss", {"1": "1"})
    print("sssss")
    print(b)

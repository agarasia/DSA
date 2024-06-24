class StockSpanner:
    def __init__(self) -> None:
        self.stack = []

    def next(self, price:int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append([price, span])

        return span
    
ss = StockSpanner()
print(ss.next(100))

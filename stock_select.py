import gugu as gg

class Stock_strategy():
    def __init__(self):
        pass

    def select_by_topcount(self,topcount):
        """
        龙虎榜次数选股
        :param topcount: 龙虎榜出现次数
        :return: 股票代码列表
        """
        StockClass = gg.BillBoard()
        StockList = StockClass.countTops(topcount)
        SelectedStock = StockList.sort_values(by="count", ascending=False).head(5)
        stockcode = SelectedStock['code'].values
        return stockcode





class pageManager:
    def __init__(self ):
        self.total_page = 0
        self.page_list = []

    def GetTotalPageList(self, total_cnt, rows):
        
        self.page_list = []

        if ((total_cnt % rows) == 0):
            self.total_page = total_cnt // rows
        else:
            self.total_page = (total_cnt // rows) + 1

        print ('home total_cnt', self.total_page)
        print ('home total_cnt type', type(self.total_page))

        for j in range(self.total_page):
            self.page_list.append(j+1)
        
        return self.page_list
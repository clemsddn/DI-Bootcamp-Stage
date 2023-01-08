

class Pagination:
    alphabetList =list("abcdefghijklmnopqrstuvwxyz")
    def __init__(self,pageSize,items=alphabetList):
        self.items=items
        self.pageSize=int(pageSize)
        self.index=0
        self.tmp=self.pageSize
        self.lenght=len(self.items)
    
    def getVisibleItems(self):
        if self.index<self.lenght:
            return self.items[self.index:self.pageSize]
        else:
            return f'Error: index{self.index} output in range.'

    def nextPage(self):
        if self.pageSize < self.lenght:
            self.pageSize +=self.tmp
            if not self.index:
                self.index += self.tmp
            else:
                self.index += self.tmp
        
        
    def prevPage(self):
        if self.index<5 :
            self.index=0
            self.pageSize=4
        else:
            self.index -= self.tmp
        
            self.pageSize -=self.tmp
    def firstPage(self):
        self.index=0
        self.pageSize=self.tmp
    def lastPage(self):
        self.index=self.lenght-self.tmp+(self.tmp-self.lenght%self.tmp)
        self.pageSize=self.lenght
        
    def goToPage(self,pageNum):
        self.index=pageNum
        self.pageSize=self.tmp+pageNum

      
        

page=Pagination(4)
print(*page.getVisibleItems())
page.nextPage()
print("=>",*page.getVisibleItems())
page.nextPage()
print(*page.getVisibleItems())
page.nextPage()
print(*page.getVisibleItems())
page.nextPage()
print(*page.getVisibleItems())
page.nextPage()
print(*page.getVisibleItems())
page.nextPage()
print(*page.getVisibleItems())

page.prevPage()
print(*page.getVisibleItems(),"<=")
page.prevPage()
print(*page.getVisibleItems())
page.firstPage()
print('firstPage:',*page.getVisibleItems())
page.lastPage()
print('lastPage:',*page.getVisibleItems())
page.goToPage(18)
print('pageJumping:',page.getVisibleItems())
page.goToPage(30)
print('pageJumping:',page.getVisibleItems())

"""
print(*page.getVisibleItems())"""
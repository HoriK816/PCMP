class SystemSetting:
    search_path : str
    sort_order : str
    sort_order_candidate = ["alphabetical"]

    def __init__(self):
        #self.search_path = "./materials/" #for test
        #self.sort_order = self.sort_order_candidate[0] #default

        self._load_setting()

    def _load_setting(self):
        """ load setting from the file"""

        with open("./setting.txt","r") as f:
            values = f.readlines()
            self.search_path = values[0][:-1]
            self.sort_order = self.sort_order_candidate[int(values[1][:-1])]


    def change_search_path(self, new_path:str) -> None:
        """ change search path of music """ 
        self.search_path = new_path 

        # update the setting file
        values = []
        with open("./setting.txt","r") as f:
            values = f.readlines()
        values[0] = new_path+'\n'
        with open("./setting.txt","w") as f:
           f.writelines(values)

    def change_sort_order(self, new_sort_order:int):
        """ change sort order of loaded music"""
        self.sort_order = sort_order_candidate(new_sort_order)

        # update the setting file
        values = [] 
        with open("./setting.txt","r") as f:
            values = f.readlines()
        values[1] = new_sort_order
        with open("./setting.txt","w") as f:
            f.writelines(values)

if __name__ == "__main__":
    setting = SystemSetting()
    print(setting.search_path)
    print(setting.sort_order)


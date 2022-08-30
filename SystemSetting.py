class SystemSetting:
    search_path : str
    sort_order : str
    sort_order_candidate = ["alphabetical"]

    def __init__(self) -> None:
        self.search_path = "./materials/" #for test
        self.sort_order = self.sort_order_candidate[0] #default

    def change_search_path(self, new_path:str) -> None:
        self.search_dir = new_path 

    def change_sort_order(self, new_sort_order:int):
        self.sort_order = sort_order_candidate(new_sort_order)

if __name__ == "__main__":
    setting = SystemSetting()
    print(setting.search_path)
    print(setting.sort_order)


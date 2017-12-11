class container:
    def __init__(self, width, height, parent, childs, split_factor, splid_mode, container_id, leav, leav_id):
        self.width = width
        self.height = height
        self.parent = parent
        self.childs = childs
        self.windows = windows
        self.splid_mode = splid_mode
        self.count = count
        self.split_factor = split_factor
        self.set_Percentage()
        self.leav = leav
        self.leav_id = leav_id

    def set_Percentage():
        for i in self.childs:
            if self.splid_mode = 0:
                #Horrizontal Split
                i.height = self.height
                i.width = self.width * i.split_factor
            else:
                #Vertikal Split
                i.width = self.width
                i.height = self.height * i.split_factor

    def reset_child_Percentage():
        for i in childs:
            i.split_factor = 1/self.childs.count()
        set_Percentage()


    def change_Split_Mode():
        if self.splid_mode == 0
            self.splid_mode = 1
        else:
            self.splid_mode = 0
        self.reset_child_Percentage()

    def add_container(container):
        self.childs.append(container)
        set_Percentage()

    def add_Part_To_Other_Childs(part_value):
        part_to_add = part_value/self.childs.count()
        for i in self.childs:
            i.split_factor += part_to_add

    def kill_container(container_id):
        #ToDo
        counter = 0
        for i in self.childs:
            if i.container_id == container_id:
                self.childs.pop(counter)

                break
            counter++

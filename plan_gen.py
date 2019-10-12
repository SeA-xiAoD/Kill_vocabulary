import datetime

class PlanGenerator:

    """
    用于记录单词书总list数，每天背几个list以及开始时间，并生成相应背单词计划表
    """

    _list_count = None
    _list_per_day = None
    _start_time = None
    calendar = None

    def __init__(self, list_count, list_per_day, start_time):

        """
        list_count: int，单词书总list数
        list_per_day: int，每天背几个list
        start_time: string，开始日期（8位年月日，如20190520）
        """

        self.set_generator(list_count, list_per_day, start_time)


    def set_generator(self, list_count, list_per_day):

            """
            list_count: int，单词书总list数
            list_per_day: int，每天背几个list
            """

            temp_list_count = int(list_count)
            temp_list_per_day = int(list_per_day)

            # 一系列判断
            if temp_list_count <= 0:
                raise Exception("好好学习，天天向上！")
            
            if temp_list_per_day <= 0:
                raise Exception("好好学习，天天向上！")
        
            if temp_list_per_day > temp_list_count:
                raise Exception("不能一口吃成个胖子！")
            
            self._list_count = temp_list_count
            self._list_per_day = temp_list_per_day


    def set_generator(self, start_time):

            """
            start_time: string，开始日期（8位年月日，如20190520）
            """
            
            if len(start_time) != 8:
                raise Exception("请输入8位年月日，如20190520！")

            temp_year = int(start_time[:4])
            temp_month = int(start_time[4:6])
            temp_day = int(start_time[7:])
            try:
                self._start_time = datetime.date(temp_year, temp_month, temp_day)
            except:
                raise Exception("请输入有效8位年月日，如20190520！")

        
    def set_generator(self, list_count, list_per_day, start_time):

        """
        list_count: int，单词书总list数
        list_per_day: int，每天背几个list
        start_time: string，开始日期（8位年月日，如20190520）
        """

        temp_list_count = int(list_count)
        temp_list_per_day = int(list_per_day)

        # 一系列判断
        if temp_list_count <= 0:
            raise Exception("好好学习，天天向上！")
        
        if temp_list_per_day <= 0:
            raise Exception("好好学习，天天向上！")
    
        if temp_list_per_day > temp_list_count:
            raise Exception("不能一口吃成个胖子！")
        
        self._list_count = temp_list_count
        self._list_per_day = temp_list_per_day
        
        if len(start_time) != 8:
            raise Exception("请输入8位年月日，如20190520！")

        temp_year = int(start_time[:4])
        temp_month = int(start_time[4:6])
        temp_day = int(start_time[7:])
        try:
            self._start_time = datetime.date(temp_year, temp_month, temp_day)
        except:
            raise Exception("请输入有效8位年月日，如20190520！")


    def generate_calendar(self):
        
        """
        根据开始背诵时间生成总体时间表，总共有list_count+30天
        """

        self.calendar = {}

        # 初始化时间表
        for i in range((self._list_count + 1) // self._list_per_day + 29):
            self.calendar[str(self._start_time + datetime.timedelta(i))] = []

        # 添加list序号进入时间表
        list_number = 1 # 记录现在是第几个list
        day_number = 0 # 记录现在是第几天开始的list，作为一个偏移量        
        while list_number <= self._list_count:
            
            if list_number < 10:
                temp_list_number = "0" + str(list_number)
            else:
                temp_list_number = str(list_number)

            # 分配list
            self.calendar[str(self._start_time + datetime.timedelta(day_number))].append("*" + temp_list_number)
            self.calendar[str(self._start_time + datetime.timedelta(day_number) + datetime.timedelta(7))].append(temp_list_number)
            self.calendar[str(self._start_time + datetime.timedelta(day_number) + datetime.timedelta(3))].append(temp_list_number)
            self.calendar[str(self._start_time + datetime.timedelta(day_number) + datetime.timedelta(1))].append(temp_list_number)
            self.calendar[str(self._start_time + datetime.timedelta(day_number) + datetime.timedelta(29))].append(temp_list_number)
            self.calendar[str(self._start_time + datetime.timedelta(day_number) + datetime.timedelta(14))].append(temp_list_number)
            
            # 更新参数
            if list_number % self._list_per_day == 0:
                day_number += 1
            list_number += 1

        # 排序
        for (key, value) in self.calendar.items():
            self.calendar[key] = sorted(value)


    def output_txt(self, file_path):

        """
        输出为txt格式
        file_path: string, 输出文件路径
        """

        if self.calendar is None:
            raise Exception("请先生成时间表！")

        output_file = open(file_path, "w")
        output_file.write("背单词时间计划表\n\n")
        output_file.write("(注：带*表示之前没有背过的新list)\n")
        output_file.write("===============================================\n\n")
        for (date, lists) in self.calendar.items():
            output_file.write(date + ":\t")

            for list_number in  lists:
                output_file.write(list_number + "\t")

            output_file.write("\n")

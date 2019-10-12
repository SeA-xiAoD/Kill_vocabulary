from plan_gen import PlanGenerator

if __name__ == "__main__":

    print("请输入单词书list总数：")
    list_count = input()
    print("请输入每天背的list数：")
    list_per_day = input()
    print("请输入开始时间：")
    start_time = input()
    print("请输入输出文件地址：")
    output_file_path = input()


    plan_gen = PlanGenerator(list_count, list_per_day, start_time)
    plan_gen.generate_calendar()
    plan_gen.output_txt(output_file_path)
        
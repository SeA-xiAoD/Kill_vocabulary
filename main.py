from plan_gen import PlanGenerator
from pdf_gen import PDF_generator

if __name__ == "__main__":

    print("请输入单词书list总数：")
    list_count = input()
    print("请输入每天背的list数：")
    list_per_day = input()
    print("请输入开始时间：")
    start_time = input()
    print("请输入输出文件名称：")
    output_file_name = input()
    print("请输入输出文件格式（txt 或 pdf）：")
    output_file_format = input().lower()

    print("\n\n================= 开始生成 ==================\n\n")

    plan_gen = PlanGenerator(list_count, list_per_day, start_time)
    calendar = plan_gen.generate_calendar()

    if output_file_format == "txt":
        plan_gen.output_txt(output_file_name)
    elif output_file_format == "pdf":
        pdf_gen = PDF_generator()
        pdf_gen.output_pdf(calendar, output_file_name)
    else:
        print("请输入正确的输出文件名和文件格式!")
    
    print("\n\n================= 生成结束 ==================\n\n")

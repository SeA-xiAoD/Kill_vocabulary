# Kill_vocabulary

### 背单词计划生成器！让我们干掉单词！四六级、IELTS、TOFEL、GRE统统去死！

本项目用于生成背单词计划，根据新东方杨鹏老师《17天搞定GRE单词》的背单词法则生成背单词计划。本书P26指出，背单词每天背过的单词最重要的是按时复习，并给出需要在当天晚上，以及1天、2天、4天、7天、15天、30天后进行复习，从而得到P27所示单词复习计划表。我认为这个复习方法如能有效利用应该是科学合理的，但是无奈每个人的复习周期、学习能力、日学习时间甚至买的单词书都不慎相同，所以我想完成这个项目，大家可以自行根据自己的实际情况调整生成自己的单词背诵计划表，打印出来根据计划背单词。

------------------
### 用法
```
# 命令行版本用法很简单啦，输入以下命令根据提示正确输入就好
python main.py


# 如果是PDF版本，需安装 pdfkit 和 wkhtmltopdf
pip iustall pdfkit

# Debian/Ubuntu
apt-get install wkhtmltopdf

# Redhat/CentOS
yum install wkhtmltopdf

# Mac OS X
brew install Caskroom/cask/wkhtmltopdf
```

------------------
### 依赖
* python==3.7.3

(PDF版本)
* pdfkit==0.6.1
* wkhtmltopdf==0.12.3.2

------------------
### 计划
- [x] 命令行输入，输出TXT文件
- [x] 命令行输入，输出PDF文件

------------------

## 坚持才是胜利，其他都是废话！
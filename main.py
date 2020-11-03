import multiprocessing
import time


# 带有参数的任务
def task(count):
    for i in range(count):
        print("任务执行中..")
        time.sleep(0.2)
    else:
        print("任务执行完成")


while True:
    task(5)

if __name__ == '__main__':
    # 创建子进程
    # args: 以元组的方式给任务传入参数
    sub_process = multiprocessing.Process(target=task, args=(5,))
    sub_process.start()
# -*- coding:utf-8 -*-

 
import xlwt
 
 
 
def writer_into_excel_onlyval(excel_path, 
                              loss_train_list, 
                              acc_train_list, 
                              val_acc1_list, 
                              val_acc5_list = None, 
                              dataset_name:str=""):
    workbook = xlwt.Workbook(encoding='utf-8')  # 设置一个workbook，其编码是utf-8
    worksheet = workbook.add_sheet("sheet1", cell_overwrite_ok=True)  # 新增一个sheet
    worksheet.write(0, 0, label='Train_loss')
    worksheet.write(0, 1, label='Train_acc')
    worksheet.write(0, 2, label='Val_acc_1')
    if dataset_name == "CIFAR-100":
        worksheet.write(0, 3, label='Val_acc_5')
 
    if dataset_name == "CIFAR-10":
        for i in range(len(loss_train_list)):  # 循环将a和b列表的数据插入至excel
            worksheet.write(i + 1, 0, label=loss_train_list[i])  # 切片的原来是传进来的Imgs是一个路径的信息
            worksheet.write(i + 1, 1, label=acc_train_list[i])
            worksheet.write(i + 1, 2, label=val_acc1_list[i])
    elif dataset_name == "CIFAR-100":
        for i in range(len(loss_train_list)):  # 循环将a和b列表的数据插入至excel
            worksheet.write(i + 1, 0, label=loss_train_list[i])  # 切片的原来是传进来的Imgs是一个路径的信息
            worksheet.write(i + 1, 1, label=acc_train_list[i])
            worksheet.write(i + 1, 2, label=val_acc1_list[i])
            worksheet.write(i + 1, 3, label=val_acc5_list[i])
    else:
        raise ValueError("Invalid dataset name")



 
    workbook.save(excel_path + str(dataset_name) +".xls")  # 这里save需要特别注意，文件格式只能是xls，不能是xlsx，不然会报错
    print('save success!   .')
 
 
 
import json
import re
import xlrd
import os
import datetime

import xlwt
from django.db.models import Count
from rest_framework import exceptions

from authentication.models import UserInfoRemark, StudentScoreDetail, UserInfo, User
from common.models import SalesManUser
from coupon.models import UserCoupon, Coupon
from order.models import OrderChartRelation, ShoppingChart, OrderPayment, Order, UserCourse
from operate_history.models import OrderOperateHistory
from source.models import ProjectCourseFee, Project, CourseProject


def clear_user_info(user_id):
    # 清除用户基本信息
    user_info_obj = UserInfo.objects.filter(user_id=user_id).first()
    UserInfoRemark.objects.filter(user_info=user_info_obj).delete()
    UserInfo.objects.filter(user_id=user_id).delete()
    StudentScoreDetail.objects.filter(user_id=user_id).delete()
    UserCoupon.objects.filter(user_id=user_id).delete()
    SalesManUser.objects.filter(user_id=user_id).delete()

    # 清除订单与购物车关系
    shopping_queryset = ShoppingChart.objects.filter(user_id=user_id)
    OrderChartRelation.objects.filter(chart__in=shopping_queryset).delete()
    # 清除购物车
    ShoppingChart.objects.filter(user_id=user_id).delete()

    order_queryset = Order.objects.filter(user_id=user_id)
    # 清除支付信息
    OrderPayment.objects.filter(order__in=order_queryset).delete()
    # 清除订单记录
    OrderOperateHistory.objects.filter(source__in=order_queryset).delete()
    # 清除用户选课信息
    UserCourse.objects.filter(user_id=user_id).delete()
    # 清除用户订单
    Order.objects.filter(user_id=user_id).delete()
    # 清除用户
    User.objects.filter(id=user_id).delete()
    print('====== 清除成功,用户ID：%s ======' % user_id)
    return '已清除 ！'


def get_mail():
    # from xlutils.copy import copy
    # mail_book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    # mail_sheet = mail_book.add_sheet('邮件', cell_overwrite_ok=True)
    #
    # count_book = xlrd.open_workbook(file_path)
    # r_sheet = count_book.sheet_by_index(0)
    #
    # all_row = r_sheet.nrows
    # user_list = []
    # for row in range(1, all_row):
    #     user_id = int(r_sheet.row_values(row, 0, 1)[0])
    #     if user_id in user_list:
    #         continue
    #     user_list.append(user_id)
    #     obj = UserInfo.objects.filter(user_id=user_id, student_status='TO_CHOOSE_COURSE').values_list('user_id', 'name',
    #                                                                                                   'email',
    #                                                                                                   'wechat').first()
    #     if not obj:
    #         continue
    #     mail_sheet.write(row, 0, obj[0])
    #     mail_sheet.write(row, 1, obj[1])
    #     mail_sheet.write(row, 2, obj[2])
    #     mail_sheet.write(row, 3, obj[3])

    # mail_book.save(r'C:\Users\555\Desktop\mail.xlsx')
    ################################################################################

    file_path = r'C:\Users\555\Desktop\180522BC学员课程情况.xls'
    count_book = xlrd.open_workbook(file_path)
    r_sheet = count_book.sheet_by_index(0)
    all_row = r_sheet.nrows

    write_book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    write_sheet = write_book.add_sheet('学生课程', cell_overwrite_ok=True)
    write_sheet.write(0, 0, '序号')
    write_sheet.write(0, 1, '学生ID')
    write_sheet.write(0, 2, '姓名')
    write_sheet.write(0, 3, '课程')
    c = 1
    user_list = []
    for row in range(1, all_row):
        user_id = int(r_sheet.row_values(row, 1, 2)[0])
        course_set = UserCourse.objects.filter(user_id=user_id).values('user__userinfo__name', 'course__name')
        for course in course_set:
            write_sheet.write(c, 0, c)

            if user_id not in user_list:
                write_sheet.write(c, 1, user_id)
                write_sheet.write(c, 2, course.get('user__userinfo__name'))
            write_sheet.write(c, 3, course.get('course__name'))
            user_list.append(user_id)
            c += 1
    write_book.save(r'C:\Users\555\Desktop\course3.xlsx')
    return


def get_chose_course_number():
    # mail_book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    # mail_sheet = mail_book.add_sheet('课程选课人数', cell_overwrite_ok=True)
    # mail_sheet.write(0, 0, '序号')
    # mail_sheet.write(0, 1, '学生ID')
    # mail_sheet.write(0, 2, '姓名')
    # mail_sheet.write(0, 3, 'CC')
    # mail_sheet.write(0, 4, '项目')
    # mail_sheet.write(0, 5, '课程')
    #
    # user_queryset = UserInfo.objects.filter(
    #     student_status__in=['TO_CHOOSE_COURSE', 'PICKUP_COURSE', 'TO_CONFIRMED']) \
    #     .values('name', 'sales_man', 'user_id')
    # row = 1
    # for user in user_queryset:
    #     order_queryset = Order.objects.filter(status='CONFIRMED', user_id=user.get('user_id')).values(
    #         'id', 'orderchartrelation__chart__project_id')
    #     project_list = [[item.get('orderchartrelation__chart__project_id'), item.get('id')] for item in order_queryset]
    #
    #     for item in project_list:
    #         order_id = item[1]
    #         project_id = item[0]
    #         if project_id in [17, 18, 19]:
    #             continue
    #         # for project in order.get('orderchartrelation__chart__project_id'):
    #         course_list = UserCourse.objects.filter(user_id=user.get('user_id'), order_id=order_id,
    #                                                 project_id=project_id).values(
    #             'course__name', 'project__campus__name', 'project__name')
    #
    #         course_str = '***'.join([item.get('course__name') for item in course_list])
    #         if course_list:
    #             project_name = course_list.first().get('project__campus__name') + course_list.first().get(
    #                 'project__name')
    #         else:
    #             project = Project.objects.filter(id=project_id).values('campus__name', 'name').first()
    #             project_name = project.get('campus__name') + '-' + project.get('name')
    #             course_str = '未选课'
    #         mail_sheet.write(row, 0, row)
    #         mail_sheet.write(row, 1, user.get('user_id'))
    #         mail_sheet.write(row, 2, user.get('name'))
    #         mail_sheet.write(row, 3, user.get('sales_man'))
    #         mail_sheet.write(row, 4, project_name)
    #         mail_sheet.write(row, 5, course_str)
    #         row += 1
    # mail_book.save(r'C:\Users\555\Desktop\course6.xlsx')
    # return
    ################################################################################################################

    mail_book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    mail_sheet = mail_book.add_sheet('课程选课人数', cell_overwrite_ok=True)
    mail_sheet.write(0, 0, '序号')
    mail_sheet.write(0, 1, '学生ID')
    mail_sheet.write(0, 2, '姓名')
    mail_sheet.write(0, 3, 'CC')
    mail_sheet.write(0, 4, '项目')
    mail_sheet.write(0, 5, '课程')
    mail_sheet.write(0, 6, '微信')
    mail_sheet.write(0, 7, '邮箱')

    project_queryset = Project.objects.all()
    row = 1
    user_list = []
    for project in project_queryset:
        # if project.id != 17:
        #     continue
        course_queryset = UserCourse.objects.filter(project=project).distinct().values('course__name', 'course')
        for course in course_queryset:
            course_set = UserCourse.objects.filter(project=project, course_id=course['course']).values(
                'user__userinfo__name', 'user__userinfo__sales_man', 'user__userinfo__email', 'user__userinfo__wechat')
            course_count = len(course_set)
            if course_count == 0:
                continue
            c = 1
            for item in course_set:
                if item.get('user__userinfo__name') == '123':
                    continue
                # if item.get('user__userinfo__wechat') in user_list:
                #     continue
                user_list.append(item.get('user__userinfo__wechat'))
                mail_sheet.write(row, 0, project.campus.name + '-' + project.name)
                mail_sheet.write(row, 1, course['course__name'])
                if c == 1:
                    mail_sheet.write(row, 2, course_count)
                mail_sheet.write(row, 3, item.get('user__userinfo__name'))
                mail_sheet.write(row, 4, item.get('user__userinfo__sales_man'))
                mail_sheet.write(row, 5, item.get('user__userinfo__email'))
                mail_sheet.write(row, 6, item.get('user__userinfo__wechat'))
                row += 1
                c = 0
        print(project.campus.name + '-' + project.name)
    mail_book.save(r'C:\Users\555\Desktop\course6.xlsx')
    return


def clear_refund_order():
    file_path = r'C:\Users\555\PycharmProjects\StuSystem\StuSystem\admin\test.xlsx'
    count_book = xlrd.open_workbook(file_path)
    r_sheet = count_book.sheet_by_index(0)
    all_row = r_sheet.nrows
    for row in range(1, all_row):
        try:
            user_id = int(r_sheet.row_values(row, 0, 1)[0])
            UserCoupon.objects.filter(user_id=user_id).delete()

            # 清除订单与购物车关系
            shopping_queryset = ShoppingChart.objects.filter(user_id=user_id)
            OrderChartRelation.objects.filter(chart__in=shopping_queryset).delete()
            # 清除购物车
            ShoppingChart.objects.filter(user_id=user_id).delete()

            order_queryset = Order.objects.filter(user_id=user_id)
            # 清除支付信息
            OrderPayment.objects.filter(order__in=order_queryset).delete()
            # 清除订单记录
            OrderOperateHistory.objects.filter(source__in=order_queryset).delete()
            # 清除用户选课信息
            UserCourse.objects.filter(user_id=user_id).delete()
            # 清除用户订单
            Order.objects.filter(user_id=user_id).delete()
            UserInfo.objects.filter(user_id=user_id).update(student_status='ADDED_CC')
            print('====== 清除成功,用户ID：%s ======' % user_id)
        except Exception as e:
            print(e)


def get_confirm_university():
    mail_book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    mail_sheet = mail_book.add_sheet('审课', cell_overwrite_ok=True)
    mail_sheet.write(0, 0, '姓名')
    mail_sheet.write(0, 1, '审课大学')
    mail_sheet.write(0, 2, '课程')
    user_set = UserInfoRemark.objects.filter(remark__istartswith='#审课大学').distinct().values('remark',
                                                                                            'user_info__user_id')
    row = 1
    for user in user_set:
        university = user.get('remark')[6:]
        # print(university)
        user_id = user.get('user_info__user_id')
        usercourse_set = UserCourse.objects.filter(user_id=user_id).values('user__userinfo__name', 'course__name')
        if not usercourse_set:
            name = UserInfo.objects.filter(user_id=user_id).values('name').first().get('name')
            course_name = '未选课'
        else:
            name = usercourse_set.first().get('user__userinfo__name')

        mail_sheet.write(row, 0, name)
        mail_sheet.write(row, 1, university)
        for course in usercourse_set:
            if usercourse_set:
                course_name = course.get('course__name')
            mail_sheet.write(row, 2, course_name)
            row += 1
    mail_book.save(r'C:\Users\555\Desktop\审课.xlsx')


def get_order():
    order_currency = dict(Order.CURRENCY)
    order_payment = dict(Order.PAYMENT)
    order_status = dict(Order.STATUS)
    mail_book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    mail_sheet = mail_book.add_sheet('订单', cell_overwrite_ok=True)
    mail_sheet.write(0, 0, '学生编号')
    mail_sheet.write(0, 1, '学生姓名')
    mail_sheet.write(0, 2, '币种')
    mail_sheet.write(0, 3, '标准金额')
    mail_sheet.write(0, 4, '创建时间')
    mail_sheet.write(0, 5, '实际金额')
    mail_sheet.write(0, 6, '支付方式')
    mail_sheet.write(0, 7, '所属CC')
    mail_sheet.write(0, 8, '订单状态')
    order_queryset = Order.objects.filter(status='CONFIRMED').values(
        'user_id', 'user__userinfo__name', 'currency', 'standard_fee', 'create_time',
        'pay_fee', 'payment', 'user__userinfo__sales_man', 'status', )
    row = 1
    for order in order_queryset:
        mail_sheet.write(row, 0, order['user_id'])
        mail_sheet.write(row, 1, order['user__userinfo__name'])
        mail_sheet.write(row, 2, order_currency[order['currency']])
        mail_sheet.write(row, 3, order['standard_fee'])
        mail_sheet.write(row, 4, str(order['create_time']))
        mail_sheet.write(row, 5, order['pay_fee'])
        mail_sheet.write(row, 6, order_payment[order['payment']])
        mail_sheet.write(row, 7, order['user__userinfo__sales_man'])
        mail_sheet.write(row, 8, order_status[order['status']])
        row += 1
    mail_book.save(r'C:\Users\555\Desktop\订单.xlsx')


def update_user_info(coupon_list, user_id, course_num, standard_fee, project_id, currency, payment, pay_fee, pay_day):
    # 清除录入学生的自行提交的待确认订单。
    order_queryset = Order.objects.filter(user_id=user_id)
    course_status = UserCourse.objects.filter(user_id=user_id).exists()
    if course_status:
        print('============ 此用户已选课程：用户ID%s ============' % user_id)
        return
    # 获取优惠卷列表
    if coupon_list:
        coupon_list = [int(float(coupon_id)) for coupon_id in coupon_list.split('+')]
    for order in order_queryset:
        OrderChartRelation.objects.filter(order=order).delete()
        ShoppingChart.objects.filter(orderchartrelation__order=order).delete()
        OrderPayment.objects.filter(order=order).delete()
        OrderOperateHistory.objects.filter(source=order).delete()
        UserCourse.objects.filter(order=order, user_id=user_id)
        order.delete()
    # 分配优惠券
    for coupon_id in coupon_list:
        UserCoupon.objects.create(operator=1, user_id=int(user_id), coupon_id=coupon_id, status='USED')
    # 生成购物车信息
    chart = ShoppingChart.objects.create(course_num=course_num, course_fee=standard_fee, status='PAYED',
                                         project_id=project_id, user_id=user_id)
    # 生成订单号
    order_count = Order.objects.all().count()
    order_number = '%s%s%s' % (datetime.datetime.now().strftime('%Y%m%d%H%M%S'), user_id, order_count)
    # 创建订单
    order = Order.objects.create(order_number=order_number, currency=currency, payment=payment, status='CONFIRMED',
                                 standard_fee=standard_fee,
                                 pay_fee=pay_fee, coupon_list=json.dumps(coupon_list), user_id=user_id)
    # 创建支付信息
    pay_date = '-'.join([pay_day[0:4], pay_day[4:6], pay_day[6:8]])
    OrderPayment.objects.create(pay_date=pay_date, img='order/order_payment/default.jpg', order=order)
    # 创建订单与购物车关系
    OrderChartRelation.objects.create(chart=chart, order=order)
    # 更新用户状态
    UserInfo.objects.filter(user_id=user_id,
                            student_status__in=['NEW', 'PERSONAL_FILE', 'ADDED_CC', 'SUPPLY_ORDER',
                                                'PAYMENT_CONFIRM']).update(student_status='TO_CHOOSE_COURSE')
    print('============ 添加成功：用户ID%s ============' % user_id)
    return


def update_project(course_num, order, project_id, user_id):
    standard_fee = ProjectCourseFee.objects.filter(project_id=project_id, course_number=course_num).values(
        'course_fee').first().get('course_fee')
    chart = ShoppingChart.objects.create(course_num=course_num, course_fee=int(standard_fee), status='PAYED',
                                         project_id=project_id, user_id=user_id)
    OrderChartRelation.objects.create(chart=chart, order=order)
    print('============ 用户新增项目成功：用户ID%s ============' % user_id)
    return


def insert_user_info():
    # file_path = r'C:\Users\555\Desktop\students\canada\小助手系统导入0510.xlsx'
    file_path = r'D:\project\StuSystem\StuSystem\admin\test.xlsx'
    count_book = xlrd.open_workbook(file_path)
    r_sheet = count_book.sheet_by_index(0)
    all_row = r_sheet.nrows

    for row in range(1, all_row):
        try:
            user_id = int(r_sheet.row_values(row, 0, 1)[0])
            project_id = int(r_sheet.row_values(row, 4, 5)[0])
            course_num = int(r_sheet.row_values(row, 5, 6)[0])
            order = Order.objects.filter(status='CONFIRMED', user_id=user_id).first()
            if order:
                update_project(course_num, order, project_id, user_id)
                continue
            payment = r_sheet.row_values(row, 6, 7)[0]
            standard_fee = int(r_sheet.row_values(row, 7, 8)[0])
            pay_fee = int(r_sheet.row_values(row, 8, 9)[0])
            pay_day = str(int(r_sheet.row_values(row, 11, 12)[0]))
            coupon_list = str(r_sheet.row_values(row, 10, 11)[0])
            if not all([user_id, project_id, course_num, pay_fee, payment, standard_fee]):
                print('**************** 参数缺失:第%s行 *****************' % row)
                continue
            elif re.search('PAY_PAL|PAYPAL|paypal|Paypal', payment):
                payment = 'PAY_PAL'
                currency = 'FOREIGN_CURRENCY'
            elif re.search('国外', payment):
                payment = 'BANK'
                currency = 'FOREIGN_CURRENCY'
            elif re.search('微信|支付宝', payment):
                payment = 'ALI_PAY'
                currency = 'RMB'
            elif re.search('银行', payment):
                payment = 'BANK'
                currency = 'RMB'
            else:
                print('**************** 参数错误:第%s行 *****************' % row)
                continue
            if not User.objects.filter(id=user_id).exists():
                raise exceptions.NotAuthenticated('用户ID%s不存在 ！' % user_id)
            update_user_info(coupon_list, int(user_id), course_num, standard_fee, project_id, currency, payment,
                             pay_fee, pay_day)
        except Exception as e:
            print(user_id)
            print(e)
    return


def check_user_detail():
    user_info_list = UserInfo.objects.all()
    for user_info in user_info_list:
        print(user_info.user_id)
        # i = StudentScoreDetail.objects.get_or_create(**{'user_id': user_info.user_id, 'is_active': 1})
        li = UserCourse.objects.filter(user_id=user_info.user_id).values('project').annotate(count=Count(1)).values(
            'project', 'count')

        lii = Order.objects.filter(user_id=user_info.user_id, status='CONFIRMED').values(
            'orderchartrelation__chart__project', 'orderchartrelation__chart__course_num')
        if not lii or not li:
            continue
        if len(li) != len(lii):
            # if li[0].get('project') == lii[0].get('orderchartrelation__chart__project') and li[0].get('count') == lii[
            #     0].get('orderchartrelation__chart__course_num'):
            print(li, lii)
    return


def get_user_list():
    gender_dict = dict(UserInfo.GENDER)
    grade_dict = dict(UserInfo.GRADE)
    # file_path = r'C:\Users\kimye\Desktop\20180706-BC待注册学员信息-截止0629已缴费学员.xlsx'
    # count_book = xlrd.open_workbook(file_path)
    # r_sheet = count_book.sheet_by_index(0)
    # all_row = r_sheet.nrows

    mail_book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    mail_sheet = mail_book.add_sheet('信息', cell_overwrite_ok=True)
    mail_sheet.write(0, 0, '序号')
    mail_sheet.write(0, 1, '学生ID')
    mail_sheet.write(0, 2, '姓名')
    mail_sheet.write(0, 3, '邮箱')
    mail_sheet.write(0, 4, '英文名')
    mail_sheet.write(0, 5, '学号')
    mail_sheet.write(0, 6, '性别')
    mail_sheet.write(0, 7, '身份证')
    mail_sheet.write(0, 8, '微信')
    mail_sheet.write(0, 9, '手机号')
    mail_sheet.write(0, 10, '学校')
    mail_sheet.write(0, 11, '专业')
    mail_sheet.write(0, 12, '年级')
    mail_sheet.write(0, 13, 'GPA')
    mail_sheet.write(0, 14, '意向校区')
    mail_sheet.write(0, 15, '生日')
    mail_sheet.write(0, 16, '课程顾问')
    mail_sheet.write(0, 17, '托福/雅思')
    mail_sheet.write(0, 18, '课表')
    mail_sheet.write(0, 19, '课表')
    mail_sheet.write(0, 20, '课表')
    mail_sheet.write(0, 21, '课表')
    mail_sheet.write(0, 22, '课表')
    ########################
    # for row in range(1, all_row):
    #     try:
    #         user_id = r_sheet.row_values(row, 1, 2)[0]
    user_queryset = UserInfo.objects.filter(
        student_status__in=["TO_CHOOSE_COURSE", "PICKUP_COURSE", "TO_CONFIRMED", "CONFIRMED_COURSE", "AFTER_SCORE",
                            "SWITCH_CREDIT", "SWITCHED_COURSE"],
        user__shoppingchart__status__in=['PAYED', 'ORDERED']).distinct()
    all_count = user_queryset.count()
    row = 1
    for user_info in user_queryset:
        # try:
        s_id = str(user_info.student_id)
        if not re.findall('[0-9]', s_id):
            flag = True
        elif not user_info.student_id:
            flag = True
        elif len(s_id) <= 6:
            flag = True
        else:
            flag = False
        if not flag:
            continue
        user_course = UserCourse.objects.filter(user_id=user_info.user_id)
        mail_sheet.write(row, 0, row)
        mail_sheet.write(row, 1, user_info.user_id)
        mail_sheet.write(row, 2, user_info.name)
        mail_sheet.write(row, 3, user_info.email)
        mail_sheet.write(row, 4, user_info.english_name)
        mail_sheet.write(row, 5, user_info.student_id)
        mail_sheet.write(row, 6, gender_dict.get(user_info.gender))
        mail_sheet.write(row, 7, user_info.id_number)
        mail_sheet.write(row, 8, user_info.wechat)
        mail_sheet.write(row, 9, user_info.phone)
        mail_sheet.write(row, 10, user_info.cschool)
        mail_sheet.write(row, 11, user_info.major)
        mail_sheet.write(row, 12, grade_dict.get(user_info.grade))
        mail_sheet.write(row, 13, user_info.gpa)
        mail_sheet.write(row, 14, json.loads(user_info.wcampus) if user_info.wcampus else None)
        mail_sheet.write(row, 15, str(user_info.birth_date) if user_info.birth_date else None)
        mail_sheet.write(row, 16, user_info.sales_man)
        mail_sheet.write(row, 17, user_info.ielts_scores)
        if user_course:
            count = 18
            for course in user_course:
                mail_sheet.write(row, count, course.course.name + "(" + course.project.name + ")")
                count += 1
        # except:
        #     print(user_info.user_id,user_info.name)
        print(row, "/", all_count)
        row += 1
    mail_book.save(r'C:\Users\kimye\Desktop\学生信息20180730.xlsx')


def get_user_info():
    status_dict = dict(UserInfo.STUDENT_STATUS)
    user_queryset = UserInfo.objects.filter(ielts_scores__isnull=True,
                                            student_status__in=['PICKUP_COURSE', 'TO_CONFIRMED', 'CONFIRMED_COURSE'])
    # user_queryset = UserInfo.objects.filter(email__endswith='gmail.com')
    mail_book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    mail_sheet = mail_book.add_sheet('信息', cell_overwrite_ok=True)
    # mail2_sheet = mail_book.add_sheet('信息2', cell_overwrite_ok=True)
    mail_sheet.write(0, 0, '学生ID')
    mail_sheet.write(0, 1, '姓名')
    mail_sheet.write(0, 2, 'CC')
    mail_sheet.write(0, 3, '微信')
    mail_sheet.write(0, 4, '状态')
    c = 1
    for user in user_queryset:
        mail_sheet.write(c, 0, user.id)
        mail_sheet.write(c, 1, user.name)
        mail_sheet.write(c, 2, user.sales_man)
        mail_sheet.write(c, 3, user.wechat)
        mail_sheet.write(c, 4, status_dict[user.student_status])

        c += 1
    # mail_book.save(r'C:\Users\kimye\Desktop\GMAIL学生.xlsx')

    # c = 1
    # for user in user_queryset:
    #     mail2_sheet.write(c, 0, user.id)
    #     mail2_sheet.write(c, 1, user.name)
    #     mail2_sheet.write(c, 2, user.sales_man)
    #     mail2_sheet.write(c, 3, user.wechat)
    #     c += 1
    mail_book.save(r'C:\Users\kimye\Desktop\学生信息.xlsx')


def get_course():
    """20180707"""
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    all_sheet = book.add_sheet('总名单', cell_overwrite_ok=True)
    all_row_name = ['系统ID', '姓名', '所在大学', '邮箱', '微信号', '就读项目1', '就读项目2', '就读项目3', '就读项目4', '课程ID1', '课程名1', '分数', '等级',
                    '课程ID2', '课程名2', '分数', '等级', '课程ID3', '课程名3', '分数', '等级', '课程ID4', '课程名4', '分数', '等级', '课程ID5',
                    '课程名5', '分数', '等级']
    row_name = ['系统ID', '姓名', '所在大学', '邮箱', '微信号', '课程ID1', '课程名1', '分数', '等级', '课程ID2', '课程名2', '分数',
                '等级', '课程ID3', '课程名3', '分数', '等级']
    c = 0
    for name in all_row_name:
        all_sheet.write(0, c, name)
        c += 1

    project_queryset = Project.objects.all()
    project_list = {}
    for project in project_queryset:
        sheet = book.add_sheet(project.campus.name + project.name, cell_overwrite_ok=True)
        c = 0
        for name in row_name:
            sheet.write(0, c, name)
            c += 1
        project_list[project.id] = {'count': 1, 'sheet': sheet, 'pro': project.id}
        # project_list['count'] = 1

    user_queryset = UserInfo.objects.filter(
        student_status__in=["TO_CHOOSE_COURSE", "PICKUP_COURSE", "TO_CONFIRMED", "CONFIRMED_COURSE", "AFTER_SCORE",
                            "SWITCH_CREDIT", "SWITCHED_COURSE"])
    all_count = user_queryset.count()
    c = 1
    for user in user_queryset[:30]:
        all_sheet.write(c, 0, user.user_id)
        all_sheet.write(c, 1, user.name)
        all_sheet.write(c, 2, user.cschool)
        all_sheet.write(c, 3, user.email)
        all_sheet.write(c, 4, user.wechat)
        user_course_list = UserCourse.objects.filter(user_id=user.user_id)
        r = 5
        p_name = []

        for course in user_course_list:
            if course.project.campus.name + course.project.name in p_name:
                continue
            p_name.append(course.project.campus.name + course.project.name)
            all_sheet.write(c, r, course.project.campus.name + course.project.name)
            r += 1
        r = 9
        w = 1
        rr = 5

        for course in user_course_list:
            all_sheet.write(c, r, course.id)
            all_sheet.write(c, r + 1, course.course.name + '(' + course.project.campus.name + course.project.name + ')')
            all_sheet.write(c, r + 2, course.score)
            all_sheet.write(c, r + 3, course.score_grade)

            # count = c
            # write_sheet = project_list[course.project.id]['sheet']
            # if w:
            #     write_sheet.write(count, 0, user.user_id)
            #     write_sheet.write(count, 1, user.name)
            #     write_sheet.write(count, 2, user.cschool)
            #     write_sheet.write(count, 3, user.email)
            #     write_sheet.write(count, 4, user.wechat)
            #     project_list[course.project.id]['count'] += 1
            #
            #     w = 0
            # write_sheet.write(count, rr,
            #                   course.course.name + '(' + course.project.campus.name + course.project.name + ')')
            # write_sheet.write(count, rr + 1, course.score)
            # write_sheet.write(count, rr + 2, course.score_grade)
            # rr +=3
            r += 4

        print('第 %s/%s 行' % (c, all_count))
        c += 1

        for pro in project_list:
            u_list = UserCourse.objects.filter(project_id=pro, user_id=user.user_id)
            if not u_list:
                continue
            count = project_list[pro]['count']
            write_sheet = project_list[pro]['sheet']
            write_sheet.write(count, 0, user.user_id)
            write_sheet.write(count, 1, user.name)
            write_sheet.write(count, 2, user.cschool)
            write_sheet.write(count, 3, user.email)
            write_sheet.write(count, 4, user.wechat)
            rr = 5

            for u in u_list:
                write_sheet.write(count, rr, u.id)

                write_sheet.write(count, rr + 1,
                                  u.course.name + '(' + u.project.campus.name + u.project.name + ')')
                write_sheet.write(count, rr + 2, u.score)
                write_sheet.write(count, rr + 3, u.score_grade)
                rr += 4

            project_list[pro]['count'] = project_list[pro]['count'] + 1

        # user_project = ShoppingChart.objects.filter(status='PAYED', user_id=user.user_id)
        # for pro in user_project:
        #     count = project_list[pro.project.id]['count']
        #     write_sheet = project_list[pro.project.id]['sheet']
        #     write_sheet.write(count, 0, user.id)
        #     write_sheet.write(count, 1, user.name)
        #     write_sheet.write(count, 2, user.cschool)
        #     write_sheet.write(count, 3, user.email)
        #     write_sheet.write(count, 4, user.wechat)
        #     rr = 5
        #     user_course_lists = UserCourse.objects.filter(user_id=user.user_id, project_id=pro.project.id)
        #
        #     for user_course in user_course_lists:
        #         write_sheet.write(count, rr,
        #                           user_course.course.name + '(' + user_course.project.campus.name + user_course.project.name + ')')
        #         write_sheet.write(count, rr + 1, user_course.score)
        #         write_sheet.write(count, rr + 2, user_course.score_grade)
        #         rr += 3
        #     project_list[pro.project.id]['count'] = project_list[pro.project.id]['count'] + 1

    book.save(r'C:\Users\kimye\Desktop\20180707选课信息.xlsx')


def get_course1():
    """20180718"""
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    all_sheet = book.add_sheet('总名单', cell_overwrite_ok=True)
    all_row_name = ['系统ID', '姓名', '性别', '身份证', '学校', '课程ID1', '课程名1', '分数', '等级', '课程ID2', '课程名2', '分数', '等级', '课程ID3',
                    '课程名3', '分数', '等级', '课程ID4', '课程名4', '分数', '等级', '课程ID5', '课程名5', '分数', '等级']
    c = 0
    for name in all_row_name:
        all_sheet.write(0, c, name)
        c += 1

    project_queryset = Project.objects.filter(id=19)
    user_queryset = UserInfo.objects.filter(
        student_status__in=["TO_CHOOSE_COURSE", "PICKUP_COURSE", "TO_CONFIRMED", "CONFIRMED_COURSE", "AFTER_SCORE",
                            "SWITCH_CREDIT", "SWITCHED_COURSE"], user__shoppingchart__project__in=project_queryset,
        # user__shoppingchart__status='PAYED'
    ).distinct()
    all_count = user_queryset.count()
    c = 1
    gender_dict = dict(UserInfo.GENDER)
    for user in user_queryset:
        user_course_list = UserCourse.objects.filter(user_id=user.user_id)
        if not user_course_list:
            continue
        all_sheet.write(c, 0, user.user_id)
        all_sheet.write(c, 1, user.name)
        all_sheet.write(c, 2, gender_dict.get(user.gender))
        all_sheet.write(c, 3, user.id_number)
        all_sheet.write(c, 4, user.cschool)

        r = 5
        for course in user_course_list:
            # if course.project not in project_queryset:
            #     continue
            all_sheet.write(c, r, course.id)
            all_sheet.write(c, r + 1, course.course.name + '(' + course.project.campus.name + course.project.name + ')')
            all_sheet.write(c, r + 2, course.score)
            all_sheet.write(c, r + 3, course.score_grade)
            r += 4

        print('第 %s/%s 行' % (c, all_count))
        c += 1

    book.save(r'C:\Users\kimye\Desktop\20180809选课信息.xlsx')


def get_some_course():
    """20180718"""

    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    all_sheet = book.add_sheet('总名单', cell_overwrite_ok=True)
    all_row_name = ['系统ID', '姓名', '性别', '身份证', '学校', '课程ID1', '课程名1', '分数', '等级', '课程ID2', '课程名2', '分数', '等级', '课程ID3',
                    '课程名3', '分数', '等级', '课程ID4', '课程名4', '分数', '等级', '课程ID5', '课程名5', '分数', '等级']
    c = 0
    for name in all_row_name:
        all_sheet.write(0, c, name)
        c += 1

    project_queryset = Project.objects.all()
    # user_queryset = UserInfo.objects.filter(
    #     student_status__in=["TO_CHOOSE_COURSE", "PICKUP_COURSE", "TO_CONFIRMED", "CONFIRMED_COURSE", "AFTER_SCORE",
    #                         "SWITCH_CREDIT", "SWITCHED_COURSE"], user__shoppingchart__project__in=project_queryset,
    #     user__shoppingchart__status='PAYED').distinct()
    # all_count = user_queryset.count()
    c = 1
    gender_dict = dict(UserInfo.GENDER)

    file_path = r'D:\project\StuSystem\StuSystem\admin\BC一二期学生名单.xlsx'
    count_book = xlrd.open_workbook(file_path)
    r_sheet = count_book.sheet_by_index(0)
    all_row = r_sheet.nrows
    for row in range(1, all_row):
        user_name = r_sheet.row_values(row, 1, 2)[0]
        user = UserInfo.objects.filter(name=user_name.strip()).first()
        if not user:
            print(user_name)
            continue
        all_sheet.write(c, 0, user.user_id)
        all_sheet.write(c, 1, user.name)
        all_sheet.write(c, 2, gender_dict.get(user.gender))
        all_sheet.write(c, 3, user.id_number)
        all_sheet.write(c, 4, user.cschool)
        user_course_list = UserCourse.objects.filter(user_id=user.user_id)

        r = 5
        for course in user_course_list:
            if course.project not in project_queryset:
                continue
            all_sheet.write(c, r, course.id)
            all_sheet.write(c, r + 1, course.course.name + '(' + course.project.campus.name + course.project.name + ')')
            all_sheet.write(c, r + 2, course.score)
            all_sheet.write(c, r + 3, course.score_grade)
            r += 4

        print('第 %s/%s 行' % (c, 55))
        c += 1

    book.save(r'C:\Users\kimye\Desktop\20180724选课信息.xlsx')


def insert_scores():
    file_path = r'C:\Users\kimye\Desktop\2018-07-18网课二期成绩录入（ZR - RGD）.xlsx'
    count_book = xlrd.open_workbook(file_path)
    r_sheet = count_book.sheet_by_index(0)
    all_row = r_sheet.nrows
    for row in range(1, all_row):
        user_id = r_sheet.row_values(row, 0, 1)[0]
        print(user_id)
        try:
            course_id1 = int(r_sheet.row_values(row, 5, 6)[0])
            score1 = int(r_sheet.row_values(row, 7, 8)[0])
            score_grade1 = str(r_sheet.row_values(row, 8, 9)[0])
            UserCourse.objects.filter(id=course_id1).update(**{'score': score1, 'score_grade': score_grade1})
        except Exception as e:
            print(e)
        try:
            course_id2 = int(r_sheet.row_values(row, 9, 10)[0])
            score2 = int(r_sheet.row_values(row, 11, 12)[0])
            score_grade2 = str(r_sheet.row_values(row, 12, 13)[0])
            UserCourse.objects.filter(id=course_id2).update(**{'score': score2, 'score_grade': score_grade2})
        except:
            continue
        try:
            course_id3 = int(r_sheet.row_values(row, 13, 14)[0])
            score3 = int(r_sheet.row_values(row, 15, 16)[0])
            score_grade3 = str(r_sheet.row_values(row, 16, 17)[0])
            UserCourse.objects.filter(id=course_id3).update(**{'score': score3, 'score_grade': score_grade3})

        except:
            continue
        try:
            course_id4 = int(r_sheet.row_values(row, 17, 18)[0])
            score4 = int(r_sheet.row_values(row, 19, 20)[0])
            score_grade4 = str(r_sheet.row_values(row, 20, 21)[0])
            UserCourse.objects.filter(id=course_id4).update(**{'score': score4, 'score_grade': score_grade4})
        except:
            continue


def get_user_detail():
    user_list = UserInfo.objects.filter(
        student_status__in=["TO_CHOOSE_COURSE", "PICKUP_COURSE", "TO_CONFIRMED", "CONFIRMED_COURSE", "AFTER_SCORE",
                            "SWITCH_CREDIT", "SWITCHED_COURSE"]).values('name', 'student_id',
                                                                        'cschool', 'sales_man',
                                                                        'user__studentscoredetail__city',
                                                                        'user__studentscoredetail__country',
                                                                        'user__studentscoredetail__province',
                                                                        'user__studentscoredetail__address',
                                                                        'user__studentscoredetail__detail_address')
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    all_sheet = book.add_sheet('总名单', cell_overwrite_ok=True)
    all_row_name = ['序列', '姓名', '学号', '学校', 'CC', '邮箱', '国家', '州', '城市', '地址一', '地址二']
    c = 0
    for name in all_row_name:
        all_sheet.write(0, c, name)
        c += 1
    c = 1
    for user in user_list:
        all_sheet.write(c, 0, c)
        all_sheet.write(c, 1, user.get('name'))
        all_sheet.write(c, 2, user.get('student_id'))
        all_sheet.write(c, 3, user.get('cschool'))
        all_sheet.write(c, 4, user.get('sales_man'))
        # all_sheet.write(c, 5, user.get('sales_man'))

        all_sheet.write(c, 6, user.get('user__studentscoredetail__country'))
        all_sheet.write(c, 7, user.get('user__studentscoredetail__province'))
        all_sheet.write(c, 8, user.get('user__studentscoredetail__city'))
        all_sheet.write(c, 9, user.get('user__studentscoredetail__address'))
        all_sheet.write(c, 10, user.get('user__studentscoredetail__detail_address'))
        c += 1

    book.save(r'C:\Users\kimye\Desktop\201800809寄送地址.xlsx')
